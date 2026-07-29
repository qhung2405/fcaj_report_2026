from pathlib import Path
import re
root = Path('content/5-Workshop')
pattern = re.compile(r'!\[([^\]]*)\]\(/images/(5-Workshop/[^\)]+)\)')
changed = []
for path in root.rglob('*.md'):
    text = path.read_text(encoding='utf-8')
    new_text = pattern.sub(r'![\1]({{< relURL "images/\2" >}})', text)
    if new_text != text:
        path.write_text(new_text, encoding='utf-8')
        changed.append(path)
print('changed files:')
for p in changed:
    print(p)
