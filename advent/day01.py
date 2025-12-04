from advent.utils import parse_common_args, load_lines

def load_input(path: str, debug: bool = False) -> list[str]:
    return load_lines(path, debug=debug)

def run_logic(data: list[str], default: int, task: int, debug: bool = False) -> int:
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
            if debug:
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
                if debug:
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
        if debug:
            print(f"[DEBUG] start={currentValve}, dir={direction}, value={value}, "
                  f"first_step={first_step}, crossings={crossings}")

        # Update current valve position after full rotation
        currentValve = (currentValve + sign * value) % 100

        # Update result based on task
        match task:
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
    args = parse_common_args()
    
    # Load input data
    lines = load_input(args.input_file, debug=args.debug)
    
    # Run the main logic
    result = run_logic(lines, task=args.task, default=50 )
    print(f"Result: {result}")

if __name__ == "__main__":
    main()

def main():
    args = parse_common_args()

  