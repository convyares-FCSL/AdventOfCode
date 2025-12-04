from advent.utils import parse_common_args, load_text

def load_input(path: str, debug: bool = False) -> list[tuple[int, int]]:
    # Read the full file as a single string using the shared helper
    text = load_text(path, debug=debug)

    # Split into raw range strings
    raw = text.split(",")
    data: list[tuple[int, int]] = []

    for item in raw:
        if not item:  # skip empty trailing comma
            continue
        left, right = item.split("-")
        data.append((int(left), int(right)))

    if debug:
        print(f"[DEBUG] First 3 ranges: {data[:3]}")
        print(f"[DEBUG] Loaded {len(data)} ranges")

    return data


def run_logic(data: list[tuple[int, int]], task: int, debug: bool = False) -> int:
    result = 0

    # Iterate through each range and check for invalid IDs
    for left, right in data:
        for value in range(left, right + 1):
            if is_invalid_id(value, task= task):
                result += value

    # Return the final result
    return int(result)

def is_invalid_id(value: int, task: int) -> bool:
    value_str = str(value)
    size = len(value_str)

    # Task 1: exactly two halves equal
    if task == 1:
        if size % 2 != 0:
            return False
        return ( value_str[:size // 2] == value_str[size // 2:] )

    # Task 2: repeating blocks
    if task == 2:
        # Try all possible block sizes betwen 1 and half the length
        max_block_size = size // 2
        for block_size in range(1, max_block_size + 1):
            # Block size must divide the full length exactly
            if size % block_size != 0:
                continue

            # Construct the candidate by repeating the block for the full length
            block = value_str[:block_size]
            candidate = block * (size // block_size)

            # Check if it matches the original value
            if candidate == value_str:
                return True
    return False

def main():
    # Parse command-line arguments
    args = parse_common_args()
    
    # Load input data
    data = load_input(args.input_file, debug=args.debug)

    # Run the main logic
    result = run_logic(data, task=args.task)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
