"""扫描 resources/ 文件夹，生成 manifest.json。每次添加/删除图片后运行一次即可。"""
import os, json, re

res = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')
entries = []

for f in sorted(os.listdir(res)):
    if f.startswith('.') or f == 'manifest.json':
        continue
    if not f.lower().endswith(('.png','.jpg','.jpeg','.gif','.webp','.bmp')):
        continue
    m = re.match(r'^(\d+)[-_]', f)
    if not m:
        continue
    entries.append({'id': int(m.group(1)), 'file': f})

manifest = {'resourcePath': 'resources/', 'teasers': entries}
manifest_path = os.path.join(res, 'manifest.json')
with open(manifest_path, 'w', encoding='utf-8') as fh:
    json.dump(manifest, fh, ensure_ascii=False, indent=2)

print(f'Generated manifest.json: {len(entries)} teasers')
for e in entries:
    print(f'  id={e["id"]}: {e["file"]}')
