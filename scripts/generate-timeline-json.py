"""Convert Timeline.md tables to TimelineJS v3 JSON format."""
import re
import json
from collections import Counter
from pathlib import Path

WIKI_DIR = Path(__file__).parent.parent / "wiki"
OUTPUT_DIR = WIKI_DIR / "assets" / "timeline"

# Theme tag to color mapping
THEME_COLORS = {
    "战争": "#e74c3c",   # red
    "改革": "#3498db",   # blue
    "外交": "#2ecc71",   # green
    "宗教": "#9b59b6",   # purple
}

def parse_timeline_md():
    """Parse Timeline.md and extract events."""
    content = (WIKI_DIR / "Timeline.md").read_text(encoding="utf-8")
    events = []
    current_period = ""

    for line in content.split("\n"):
        # Match period headers
        period_match = re.match(r"^## (.+)$", line)
        if period_match:
            current_period = period_match.group(1).strip()
            continue

        # Match table rows (skip header rows)
        row_match = re.match(r"^\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|$", line)
        if row_match:
            year_str = row_match.group(1).strip()
            event_text = row_match.group(2).strip()
            themes_str = row_match.group(3).strip()

            # Skip header/separator rows
            if year_str in ("年份", "---") or "---" in year_str:
                continue

            # Parse themes
            themes = re.findall(r"【(.+?)】", themes_str)
            primary_theme = themes[0] if themes else ""

            # Extract numeric year (handle "约896", "1414-1418", etc.)
            year_clean = re.sub(r"[^\d-]", "", year_str)
            if "-" in year_clean:
                # Range: use start year
                year_num = year_clean.split("-")[0]
            else:
                year_num = year_clean

            if not year_num:
                continue

            # Build event
            event = {
                "start_date": {"year": int(year_num)},
                "text": {
                    "headline": event_text[:60],
                    "text": f"**{current_period}**\n\n{event_text}"
                },
                "group": primary_theme,
                "background": {"color": THEME_COLORS.get(primary_theme, "#95a5a6")}
            }
            events.append(event)

    return events

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    events = parse_timeline_md()

    timeline_data = {
        "title": {
            "text": {
                "headline": "哈布斯堡帝国的崛起",
                "text": "基于玛玛吉所著 *Rise of the Habsburg Empire, 1526-1851* 的重大事件时间线（896-1815）"
            }
        },
        "events": events
    }

    output_path = OUTPUT_DIR / "timeline.json"
    output_path.write_text(
        json.dumps(timeline_data, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    print(f"Generated {output_path} with {len(events)} events")

    # Print theme breakdown
    theme_counts = Counter(e["group"] for e in events)
    for theme, count in theme_counts.most_common():
        print(f"  {theme}: {count}")

if __name__ == "__main__":
    main()
