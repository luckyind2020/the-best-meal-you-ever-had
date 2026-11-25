"""The Best Meal You Ever Had — make.fun entry.

Reads the one-sentence entry from entry.txt and prints it, exactly as
written. No arguments, no network, no side effects.
"""

from pathlib import Path


def load_entry() -> str:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    text = entry_path.read_text(encoding="utf-8").strip()
    if not text:
        raise SystemExit("entry.txt is empty — nothing to serve.")
    return text


def main() -> None:
    print(load_entry())


if __name__ == "__main__":
    main()
