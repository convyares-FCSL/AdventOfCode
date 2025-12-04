from advent.utils import parse_common_args, load_lines

def load_input(path: str, debug: bool = False) -> list[str]:
    return load_lines(path, debug=debug)

def run_logic(data: list[str], task: int, debug: bool = False) -> int:
    result = 0
    
    for entry in data:
        entry = entry.strip()
        match task:
            case 1:
                result += max_pair_value(entry)
            case 2:
                raise NotImplementedError("Task 2 not implemented yet")
    return result

def max_pair_value(line: str) -> int:
    max_value = -1
    length = len(line)
    for i in range(length):
        for j in range(i + 1, length):
            pair_value = 10 * int(line[i]) + int(line[j])
            if pair_value > max_value:
                max_value = pair_value
    return max_value
         
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
