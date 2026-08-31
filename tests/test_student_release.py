"""El paquete estudiantil no incluye material privado."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_student_release_excludes_private_material(tmp_path: Path) -> None:
    output = tmp_path / "dist"
    script = ROOT / "scripts" / "build_student_release.py"
    completed = subprocess.run(
        [sys.executable, str(script), "--output", str(output), "--name", "paquete"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 0
    package = output / "paquete"
    assert package.exists()
    rel_parts = {p.relative_to(package).as_posix() for p in package.rglob("*") if p.is_file()}
    joined = "\n".join(rel_parts)
    assert "instructor/" not in joined
    assert "data_generation/" not in joined
    assert "scripts/generate_data.py" not in joined
    assert "anomaly_log" not in joined
    assert (package / "README.md").exists()
    assert (package / "app" / "Home.py").exists()
    assert (package / "sql" / "01_create_schemas.sql").exists()
    assert not (package / "src" / "course_project" / "data_generation").exists()
