import argparse
import inspect
import json
import os
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
os.environ['XINGCE_KB_DIR'] = str(ROOT / 'knowledge_base')
from xingce_solver import mcp_server as core
TOOLS = {n[5:]: f for n, f in vars(core).items() if n.startswith('tool_') and callable(f)}
def main():
    sys.stdout.reconfigure(encoding='utf-8')
    p = argparse.ArgumentParser()
    p.add_argument('tool', choices=['list', *sorted(TOOLS)])
    p.add_argument('--input', type=Path, help='UTF-8 JSON arguments file')
    a = p.parse_args()
    try:
        if a.tool == 'list':
            result = {n: str(inspect.signature(f)) for n, f in TOOLS.items()}
        else:
            params = json.loads(a.input.read_text(encoding='utf-8-sig')) if a.input else {}
            if not isinstance(params, dict):
                raise ValueError('Arguments must be a JSON object')
            f = TOOLS[a.tool]
            if 'kb_dir' in inspect.signature(f).parameters:
                params['kb_dir'] = str(ROOT / 'knowledge_base')
            result = f(**params)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ValueError, TypeError, OSError, RuntimeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
if __name__ == '__main__':
    raise SystemExit(main())
