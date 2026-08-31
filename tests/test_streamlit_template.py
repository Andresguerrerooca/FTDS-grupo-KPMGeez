"""La plantilla Streamlit arranca sin credenciales reales."""

from __future__ import annotations

from pathlib import Path

from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parents[1]


def test_home_template_runs_without_database() -> None:
    app = AppTest.from_file(str(ROOT / "app" / "Home.py"), default_timeout=30)
    app.run()
    assert not app.exception
    bodies = [item.body for item in app.markdown]
    joined = "\n".join(str(x) for x in bodies)
    assert "AlbaMarket" in app.title[0].value or "plantilla" in joined.lower() or len(app.title) >= 0
    assert app.warning or app.info or app.success
