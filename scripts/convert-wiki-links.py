"""Convert [[wiki-links]] to MkDocs-compatible Markdown links."""
import re
import sys
from pathlib import Path

WIKI_DIR = Path(__file__).parent.parent / "wiki"

def get_relative_prefix(file_path: Path) -> str:
    """Get relative path prefix from a wiki file to the wiki root."""
    rel = file_path.relative_to(WIKI_DIR)
    depth = len(rel.parts) - 1  # number of directories above
    if depth == 0:
        return ""
    return "../" * depth

def convert_link(match: re.Match, file_path: Path) -> str:
    """Convert a single [[target|text]] or [[target]] to Markdown link."""
    content = match.group(1)
    prefix = get_relative_prefix(file_path)

    if "|" in content:
        target, text = content.split("|", 1)
    else:
        target = text = content

    # MkDocs resolves .md links relative to the source file
    link = f"[{text}]({prefix}{target}.md)"
    return link

def convert_file(file_path: Path, dry_run: bool = False) -> tuple[int, str]:
    """Convert all wiki links in a file. Returns (count, new_content)."""
    content = file_path.read_text(encoding="utf-8")
    pattern = re.compile(r"\[\[([^\]]+)\]\]")

    # Idempotency guard: skip files with no wiki links
    matches = list(pattern.finditer(content))
    if not matches:
        return 0, content

    count = len(matches)

    if dry_run:
        return count, content

    def replacer(match):
        return convert_link(match, file_path)

    new_content = pattern.sub(replacer, content)
    return count, new_content

def main():
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("DRY RUN — no files will be modified\n")

    total_links = 0
    for md_file in sorted(WIKI_DIR.rglob("*.md")):
        count, new_content = convert_file(md_file, dry_run=dry_run)
        if count > 0:
            if not dry_run:
                md_file.write_text(new_content, encoding="utf-8")
            rel = md_file.relative_to(WIKI_DIR)
            print(f"  {rel}: {count} links {'found' if dry_run else 'converted'}")
            total_links += count
    print(f"\nTotal: {total_links} links {'found' if dry_run else 'converted'}")

if __name__ == "__main__":
    main()
