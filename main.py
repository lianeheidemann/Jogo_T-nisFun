from pathlib import Path
import runpy
import sys


GAME_DIR = Path(__file__).resolve().parent / "tenis_fun"

sys.path.insert(0, str(GAME_DIR))
runpy.run_path(str(GAME_DIR / "main.py"), run_name="__main__")
