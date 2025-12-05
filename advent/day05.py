from advent.utils import parse_common_args, load_lines
from dataclasses import dataclass

@dataclass
class InputData:
    ranges: list[tuple[int, int]]
    ids: list[int]

def load_input(path: str, debug: bool = False) -> InputData:
    # Load input lines
    lines = load_lines(path, debug=debug)

    # Split into sections
    blank_index = lines.index("")
    raw_range = lines[:blank_index]
    raw_ids = lines[blank_index + 1:]

    # Parse ranges:
    ranges: list[tuple[int, int]] = []
    for line in raw_range:
        left, right = line.split("-")
        ranges.append((int(left), int(right)))

    # Parse ids
    ids = [int(x) for x in raw_ids]

    # Construct data object
    data = InputData(ranges=ranges, ids=ids)

    # Debug output
    if debug:
        print(f"[DEBUG] First 3 ranges: {data.ranges[:3]}")
        print(f"[DEBUG] Loaded {len(data.ranges)} ranges")

        print(f"[DEBUG] First 3 ids: {data.ids[:3]}")
        print(f"[DEBUG] Loaded {len(data.ids)} ids")

    return data

# Main logic function
def run_logic(data: list[str], task: int, debug: bool = False, bucket_size: int = 12) -> int:
    result = 0
 
    return result
    
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
