import argparse
from pathlib import Path


def parse_args():
    # Set up argument parser
    parser = argparse.ArgumentParser()

    # Debug flag
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")

    # Task number (1 or 2)
    parser.add_argument("task", type=int, help="Task number (1 or 2)")
    if parser.parse_args().task not in [1, 2]:
        exit("Error: task must be 1 or 2")

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

def run_logic(data: list[str], default : int, args: argparse) -> int:
    result = 0
    currentValve = default

    # Process each entry in the data
    for entry in data:
        rotations = 0
        direction = entry[0]
        value_str = entry[1:]

        # Parse value and calculate rotations
        try:
            value = int(value_str)
            rotations = (( currentValve + value ) / 100 ) // 1
        except ValueError:
            if args.debug:
                print(f"[DEBUG] Skipping invalid entry: {entry}")
            continue

        # Update current valve position
        match direction:
            case 'R':
                currentValve = (currentValve + value) % 100
            case 'L':
                currentValve = (currentValve - value) % 100
            case _:
                if args.debug:
                    print(f"[DEBUG] direction not recognized: {direction}")
                continue

        # Update result based on task
        match args.task:
            case 1:
                if currentValve == 0:
                    result += 1
            case 2:
                if currentValve == 0:
                    result += 1
                result += rotations 

    # Return the final result               
    return result

def main():
    # Parse command-line arguments
    args = parse_args()
    print(f"debug={args.debug}, task={args.task}, file={args.input_file}")
    
    # Load input data
    lines = load_input(args.input_file, debug=args.debug)

    # Run the main logic
    result = run_logic(lines, default=50, debug=args)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
