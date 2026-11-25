"""Entry for make.fun competition: u-suga-everyday-things-two-lines-longer-run-f8734479.

Running this program writes the two-line entry to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

LINE_ONE = "A queue is a human train where every person is a carriage: it only moves when the front carriage moves, and nobody can unhook and rush ahead without breaking the whole train."
LINE_TWO = "The train works because each of us, like a carriage, rolls forward only when the gap ahead opens — but it leaves out that carriages never get bored, check their phones, or quietly leave to buy a coffee."

ENTRY = LINE_ONE + "\n" + LINE_TWO


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry lines to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
