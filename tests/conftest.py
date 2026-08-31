"""Configuración común de pytest."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
SRC = ROOT / "src"

for path in (ROOT, SRC, SCRIPTS):
    text = str(path)
    if text not in sys.path:
        sys.path.insert(0, text)
