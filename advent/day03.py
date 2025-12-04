from advent.utils import parse_common_args, load_lines

# Input loading function
def load_input(path: str, debug: bool = False) -> list[str]:
    return load_lines(path, debug=debug)

# Main logic function
def run_logic(data: list[str], task: int, debug: bool = False, bucket_size: int = 12) -> int:
    result = 0
    
    for entry in data:
        entry = entry.strip()
        match task:
            case 1:
                result += max_pair_value(entry)
            case 2:
                result += max_number_from_line(entry, bucket_size)
    return result

# Task 1 helper
def max_pair_value(line: str) -> int:
    max_value = -1
    length = len(line)
    for i in range(length):
        for j in range(i + 1, length):
            pair_value = 10 * int(line[i]) + int(line[j])
            if pair_value > max_value:
                max_value = pair_value
    return max_value
         
# Task 2 helper
def max_number_from_line(line: str, digits_to_pick: int) -> int:
    length = len(line)
    assert digits_to_pick <= length, "Cannot pick more digits than available"

    start_index = 0
    chosen_digits: list[str] = []

    while len(chosen_digits) < digits_to_pick:
        # pick first digit
        remaining_to_pick = digits_to_pick - len(chosen_digits)
        end_index = length - remaining_to_pick
        best_digit = "-1"
        best_index = start_index

        for index in range(start_index, end_index + 1):
            digit = line[index]
            if digit > best_digit:
                best_digit = digit
                best_index = index

        chosen_digits.append(best_digit)
        start_index = best_index + 1
    
    return int("".join(chosen_digits))
    
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
