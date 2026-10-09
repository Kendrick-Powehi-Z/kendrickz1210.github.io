#!/usr/bin/env python3
"""Patch the OFFICIAL AcadHomepage _config.yml; run in your fork's root.
Preserves the template's existing plugins, defaults, build and layout settings.
"""
from pathlib import Path
import re

p = Path('_config.yml')
if not p.is_file():
    raise SystemExit('ERROR: Run this script in the root of your AcadHomepage fork (where _config.yml exists).')
s = p.read_text(encoding='utf-8')
updates = {
    'title': 'Zhihan Zhang | Academic Homepage',
    'description': 'Zhihan Zhang at Wuhan University — Video Understanding and Efficient MLLM.',
    'repository': 'Kendrick-Powehi-Z/Kendrick-Powehi-Z.github.io',
}
for key, value in updates.items():
    pat = re.compile(r'(?m)^' + re.escape(key) + r'\s*:\s*[^\n]*$')
    if not pat.search(s): raise SystemExit(f'ERROR: Missing config key: {key}')
    s = pat.sub(lambda _: f'{key}: "{value}"', s, count=1)
# Only update keys inside author block; preserve other keys.
match = re.search(r'(?ms)^author:\s*\n(.*?)(?=^\S|\Z)', s)
if not match: raise SystemExit('ERROR: author section not found')
author = match.group(1)
fields = {
    'name': 'Zhihan Zhang',
    'avatar': 'images/avatar-placeholder.svg',
    'bio': 'Master’s Student · Wuhan University',
    'location': 'Wuhan, China',
    'email': '',
    'googlescholar': '',
    'github': 'Kendrick-Powehi-Z',
}
for key, val in fields.items():
    pat = re.compile(r'(?m)^(\s+' + re.escape(key) + r'\s*:)\s*[^\n]*$')
    if not pat.search(author): raise SystemExit(f'ERROR: Missing author key: {key}')
    author = pat.sub(lambda m: f'{m.group(1)} "{val}"' if val else f'{m.group(1)}', author, count=1)
s = s[:match.start(1)] + author + s[match.end(1):]
p.write_text(s, encoding='utf-8')
print('Updated _config.yml for Zhihan Zhang. Add an avatar and optional public email/Scholar URL when ready.')
