from pathlib import Path
import sys

RESERVED = {'index.md', 'log.md'}


def validate(root: Path) -> int:
    errors = []
    for path in root.rglob('*.md'):
        rel = path.relative_to(root)
        text = path.read_text(encoding='utf-8')
        if path.name in RESERVED:
            # Root index may include version frontmatter; other index/log files are intentionally simple.
            continue
        if not text.startswith('---\n'):
            errors.append(f'{rel}: missing YAML frontmatter')
            continue
        parts = text.split('---\n', 2)
        if len(parts) < 3:
            errors.append(f'{rel}: invalid frontmatter block')
            continue
        frontmatter = parts[1]
        if not any(line.strip().startswith('type:') and line.split(':', 1)[1].strip() for line in frontmatter.splitlines()):
            errors.append(f'{rel}: missing non-empty type field')

    if errors:
        print('Validation failed:')
        for err in errors:
            print('-', err)
        return 1
    print('OKF validation passed.')
    return 0


if __name__ == '__main__':
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
    raise SystemExit(validate(root))
