from pathlib import Path
import sys


if getattr(sys, "frozen", False):
    ASSETS_DIR = Path(sys._MEIPASS) / "assets"
else:
    ASSETS_DIR = Path(__file__).resolve().parents[2] / "assets"


def asset_path(*parts):
    return str(ASSETS_DIR.joinpath(*parts))
