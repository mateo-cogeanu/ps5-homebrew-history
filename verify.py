#!/usr/bin/env python3
"""Verify every preserved file and reject unindexed additions to snapshot trees."""
from pathlib import Path
import hashlib,json,subprocess
root=Path(__file__).resolve().parent
manifest=json.loads((root/'manifest.json').read_text())
expected=set()
for entry in manifest['files']:
 path=root/entry['destination'];expected.add(entry['destination'])
 assert path.is_file() and not path.is_symlink(),path
 assert path.stat().st_size==entry['bytes'],path
 assert hashlib.sha256(path.read_bytes()).hexdigest()==entry['sha256'],path
 assert bool(path.stat().st_mode & 0o111)==(entry['git_mode']=='100755'),path
 assert path.suffix.lower() not in {'.jar','.class','.o','.elf','.zip','.pkg','.sprx','.so','.a','.pyc','.log'},path
for section in ['runtime','prosperocraft']:
 actual={p.relative_to(root).as_posix() for p in (root/section).rglob('*') if p.is_file()}
 assert actual=={p for p in expected if p.startswith(section+'/')},section
for entry in manifest['sets']:
 assert json.loads((root/entry['destination']/'validation.json').read_text())==entry['validation']
print(f"PASS: {len(manifest['sets'])} snapshots, {len(expected)} byte/mode-verified source and context files; original validation retained")
