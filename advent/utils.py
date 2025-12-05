import argparse
from pathlib import Path
from typing import Union

# -----------------------------
# Common CLI argument parsing
# -----------------------------
def parse_common_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument( "-d", "--debug", action= "store_true", help= "Enable debug mode" )

    parser.add_argument( "task", type= int, choices=[1, 2], help= "Task number (1 or 2)" )

    parser.add_argument( "input_file", help= "Path or name of input data file" )

    return parser.parse_args()

# -----------------------------
# Input path + loading helpers
# -----------------------------

# Resolve an input path (absolute or relative)
def resolve_input_path(path: Union[str, Path]) -> Path:
    p = Path(path)
    if p.is_absolute():
        return p
    return Path(__file__).parent / "inputdata" / p

# Load the entire input file as a single string
def load_text(path: str, debug: bool = False) -> str:
    input_path = resolve_input_path(path)

    if debug:
        print(f"[DEBUG] Reading input from: {input_path.resolve()}")

    return input_path.read_text(encoding="utf-8")

# Load the input file as a list of stripped lines.
def load_lines(path: str, debug: bool = False) -> list[str]:
    text = load_text(path, debug=debug)
    lines = [line.rstrip("\n") for line in text.splitlines()]

    if debug:
        print(f"[DEBUG] Loaded {len(lines)} lines")

    return lines