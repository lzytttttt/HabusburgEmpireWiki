"""Generate SVG placeholder images for key historical figures."""
from pathlib import Path

WIKI_DIR = Path(__file__).parent.parent / "wiki"
IMG_DIR = WIKI_DIR / "assets" / "images"

# Key figures with their roles and dates
FIGURES = [
    ("rudolf-i", "鲁道夫一世", "Rudolf I", "德意志国王 1273-1291"),
    ("albrecht-ii", "阿尔布雷希特二世", "Albert II", "德意志国王 1438-1439"),
    ("frederick-iii", "弗里德里克三世", "Frederick III", "神圣罗马帝国皇帝 1440-1493"),
    ("maximilian-i", "马克西米连一世", "Maximilian I", "神圣罗马帝国皇帝 1493-1519"),
    ("charles-v", "查理五世", "Charles V", "神圣罗马帝国皇帝 1519-1556"),
    ("ferdinand-i", "费迪南德一世", "Ferdinand I", "神圣罗马帝国皇帝 1556-1564"),
    ("rudolf-ii", "鲁道夫二世", "Rudolf II", "神圣罗马帝国皇帝 1576-1612"),
    ("ferdinand-ii", "费迪南德二世", "Ferdinand II", "神圣罗马帝国皇帝 1619-1637"),
    ("leopold-i", "列奥波德一世", "Leopold I", "神圣罗马帝国皇帝 1657-1705"),
    ("eugene", "欧根亲王", "Prince Eugene", "萨伏伊-卡里尼亚诺 1663-1736"),
    ("maria-theresa", "玛丽娅·特蕾莎", "Maria Theresa", "奥地利女大公 1740-1780"),
    ("joseph-ii", "约瑟夫二世", "Joseph II", "神圣罗马帝国皇帝 1765-1790"),
    ("metternich", "梅特涅", "Metternich", "外交大臣 1809-1848"),
    ("napoleon", "拿破仑", "Napoleon", "法兰西皇帝 1804-1815"),
    ("franz-ii", "弗朗西斯二世", "Francis II", "神圣罗马帝国末代皇帝 1792-1806"),
]

SVG_TEMPLATE = '''<svg xmlns="http://www.w3.org/2000/svg" width="200" height="260" viewBox="0 0 200 260">
  <rect width="200" height="260" fill="#2c3e50" rx="8"/>
  <rect x="10" y="10" width="180" height="180" fill="#34495e" rx="4"/>
  <circle cx="100" cy="80" r="40" fill="#7f8c8d"/>
  <ellipse cx="100" cy="130" rx="50" ry="30" fill="#7f8c8d"/>
  <text x="100" y="200" text-anchor="middle" fill="#ecf0f1" font-family="sans-serif" font-size="14" font-weight="bold">{cn_name}</text>
  <text x="100" y="220" text-anchor="middle" fill="#bdc3c7" font-family="sans-serif" font-size="11">{en_name}</text>
  <text x="100" y="240" text-anchor="middle" fill="#95a5a6" font-family="sans-serif" font-size="10">{dates}</text>
</svg>'''

def main():
    IMG_DIR.mkdir(parents=True, exist_ok=True)

    for slug, cn_name, en_name, dates in FIGURES:
        svg = SVG_TEMPLATE.format(cn_name=cn_name, en_name=en_name, dates=dates)
        path = IMG_DIR / f"{slug}.svg"
        path.write_text(svg, encoding="utf-8")

    print(f"Generated {len(FIGURES)} placeholder images in {IMG_DIR}")

if __name__ == "__main__":
    main()
