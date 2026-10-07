"""Interactive launcher for Python scripts in this project."""

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
EXCLUDED = {".git", ".venv", "venv", "__pycache__"}


def main() -> int:
	scripts = sorted(
		path
		for path in ROOT.rglob("*.py")
		if path.resolve() != Path(__file__).resolve()
		and not EXCLUDED.intersection(path.relative_to(ROOT).parts)
	)

	if not scripts:
		print("No other Python scripts were found in this folder.")
		return 0

	print("Welcome to the Pythonic Matrix - Choose a program to run:")
	for number, script in enumerate(scripts, start=1):
		print(f"{number}. {script.relative_to(ROOT)}")
	print("q. Quit")

	while True:
		choice = input("Selection: ").strip().lower()
		print("Loading...")
		if choice in {"q", "quit"}:
			return 0
		if choice.isdecimal() and 1 <= int(choice) <= len(scripts):
			return subprocess.call(
				[sys.executable, str(scripts[int(choice) - 1])], cwd=ROOT
			)
		print("Enter one of the listed numbers, or q to quit.")


if __name__ == "__main__":
	raise SystemExit(main())
