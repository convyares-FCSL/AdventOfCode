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
def run_logic(data: InputData, task: int, debug: bool = False) -> int:
    match task:
        case 1:
            if debug:
                print("[DEBUG] Running Task 1")
            result = task_1(data, debug=debug)
        case 2:
            if debug:
                print("[DEBUG] Running Task 2")
            result = task_2(data, debug=debug)
        case _:
            raise ValueError(f"Unknown task: {task}")

    return result

# Task 1: Count how many ids fall within any of the given ranges
def task_1(data: InputData, debug: bool = False) -> int:
    result = 0

    for id in data.ids:
        if in_range(id, data.ranges, debug=debug):
            result += 1 

    return result       

# Task 2: Count how many ids are missing from the given ranges
def task_2(data: InputData, debug: bool = False) -> int:
    result = 0
    last_checked = -1

    sorted_data = sorted(data.ranges, key=lambda pair: pair[0])

    if debug:
        print(f"[DEBUG] Sorted ranges: {sorted_data}")
        
    # Iterate through each range and check for invalid IDs
    for left, right in sorted_data:
          # if this range is already fully covered, skip it
        if right <= last_checked:
            if debug:
                print(f"[DEBUG] Skipping covered range {left}-{right}, last_checked: {last_checked}")
            continue
    
        # Adjust left boundary based on last checked position
        if left > last_checked:
            left_temp = left
        else :
            left_temp = last_checked + 1
        
        if debug:
            print(f"[DEBUG] Adjusted ranges: {left_temp}-{right}, last_checked: {last_checked}")

        # Calculate the number of valid IDs in the current range
        diff = right - left_temp + 1

        # Accumulate the result
        result += diff 

        # Update the last checked position
        last_checked = right

    return result       

# Helper function to check if an input is within any of the given ranges
def in_range(input: int, data: list[tuple[int, int]], debug: bool) -> bool:
    for left, right in data:
        if left <= input <= right:
            if debug:
                print(f"[DEBUG] ID {input} found in range {left}-{right}")
            return True
    return False

def main():
    # Parse command-line arguments
    args = parse_common_args()
    
    # Load input data
    data = load_input(args.input_file, debug=args.debug)

    # Run the main logic
    result = run_logic(data, task=args.task, debug=args.debug)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
