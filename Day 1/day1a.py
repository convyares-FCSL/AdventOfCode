import argparse
from pathlib import Path

def parse_args():
    # Set up argument parser
    parser = argparse.ArgumentParser()

    # Debug flag
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")

    # Task must be 1 or 2
    parser.add_argument("task", type=int, choices=[1, 2], help="Task number (1 or 2)")

    # Input file path
    parser.add_argument("input_file", help="Path to input data file")

    return parser.parse_args()

def load_input(path: str, debug: bool = False) -> list[str]:
    # Load input data from the specified file
    input_path = Path(path)

    # Debug information
    if debug:
        print(f"[DEBUG] Reading input from: {input_path.resolve()}")

    # Read lines from the file
    with input_path.open("r", encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file]

    # More debug information
    if debug:
        print(f"[DEBUG] First 3 lines: {lines[:3]}")
        print(f"[DEBUG] Loaded {len(lines)} lines")

    # Return the list of lines
    return lines


def run_logic(data: list[str], default: int, args: argparse.Namespace) -> int:
    result = 0
    currentValve = default

    # Process each entry in the data
    for entry in data:
        entry = entry.strip()
        if not entry:
            continue

        # Direction is first char, value is the rest
        direction = entry[0]
        value_str = entry[1:]

        # Parse value
        try:
            value = int(value_str)
        except ValueError:
            if args.debug:
                print(f"[DEBUG] Skipping invalid entry: {entry}")
            continue

        # Determine sign and base for calculations
        match direction:
            case 'R':
                sign = 1
                base = (100 - currentValve) % 100
            case 'L':
                sign = -1
                base = currentValve % 100
            case _:
                if args.debug:
                    print(f"[DEBUG] direction not recognized: {direction}")
                continue

        # If base == 0, the *next* time we hit zero is after 100 steps, not at step 0
        first_step = base if base != 0 else 100

        # Count how many times we hit 0 during this move (part 2 logic)
        if value < first_step:
            crossings = 0
        else:
            crossings = 1 + (value - first_step) // 100

        # Debug per move
        if args.debug:
            print(f"[DEBUG] start={currentValve}, dir={direction}, value={value}, "
                  f"first_step={first_step}, crossings={crossings}")

        # Update current valve position after full rotation
        currentValve = (currentValve + sign * value) % 100

        # Update result based on task
        match args.task:
            case 1:
                # Part 1: count only when we END on 0
                if currentValve == 0:
                    result += 1
            case 2:
                # Part 2: count every time we HIT 0 during the move
                result += crossings

    # Return the final result
    return int(result)


def main():
    # Parse command-line arguments
    args = parse_args()
    print(f"debug={args.debug}, task={args.task}, file={args.input_file}")

    # Load input data
    lines = load_input(args.input_file, debug=args.debug)

    # Run the main logic
    result = run_logic(lines, default=50, args=args)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
