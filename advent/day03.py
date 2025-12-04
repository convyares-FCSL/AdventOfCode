from advent.utils import parse_common_args, load_text

def load_input(path: str, debug: bool = False) -> list[str]:
    # Read the full file as a single string using the shared helper
    text = load_text(path, debug=debug)

    # TODO: Parse the input text into a list of tuples (left, right)
    return text


def run_logic(data: list[tuple[int, int]], task: int, debug: bool = False) -> int:
    result = 0

    # TODO: Implement the main logic based on the task number

    # Return the final result
    return int(result)
         
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
