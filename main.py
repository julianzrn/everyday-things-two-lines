"""Entry for make.fun competition: u-suga-everyday-things-two-lines-longer-run-f8734479.

Running this program writes the entry text to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

LINE_ONE_A = "A queue is a human train where every person is a carriage: "
LINE_ONE_B = "it only moves when the front carriage moves, and nobody can "
LINE_ONE_C = "unhook and rush ahead without breaking the whole train."

LINE_TWO_A = "The train works because each of us, like a carriage, rolls "
LINE_TWO_B = "forward only when the gap ahead opens — but it leaves out "
LINE_TWO_C = "that carriages never get bored, check their phones, or "
LINE_TWO_D = "quietly leave to buy a coffee."

ENTRY = LINE_ONE_A + LINE_ONE_B + LINE_ONE_C + "\n" + LINE_TWO_A + LINE_TWO_B + LINE_TWO_C + LINE_TWO_D


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline added."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry text to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
