import math
from advent.utils import parse_common_args, load_lines
from dataclasses import dataclass

@dataclass
class InputData:
    datset: list[list[int]]
    ops: list[str]

def load_input(path: str, debug: bool = False) -> InputData:
    # Load input lines
    lines = load_lines(path, debug=debug)

    # Initialize data structure
    data = InputData(datset=[], ops=[])

    # Split into raw range strings
    rawData: list[list[str]] = []
    for line in lines:
        if not line:
            continue    
        raw = line.split()
        rawData.append(raw)

    # Get dimensions
    row = len(rawData)
    col = len(rawData[0])

    # Transpose the data (all rows except the last, which is ops)
    for i in range(col):
        temp: list[int] = []
        for j in range(row - 1):
            temp_row = rawData[j]
            temp.append(int(temp_row[i]))
        data.datset.append(temp)

    # Last row are operations (keep as strings)
    data.ops = rawData[row - 1]

    # Debug output
    if debug:
        print(f"[DEBUG] Raw: {rawData[:]}, Row size: {row}, col size: {col}")
        print(f"[DEBUG] Adjusted: {data.datset[:]}")
        print(f"[DEBUG] Ops: {data.ops[:]}")

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

# Task 1: 
def task_1(data: InputData, debug: bool = False) -> int:
    # Initialize result    
    result = 0

    # Iterate through each array and operation
    size = len(data.datset)
    for idx in range(size):
        # Initialize sub-result
        sub_result = 0

        # Process each value in the array
        array = data.datset[idx]    

        # Perform operation based on the operator
        match data.ops[idx]:
            case "+":
                sub_result = sum(array)
            case "*":
                sub_result = math.prod(array)
            case _:
                if debug:
                    print(f"[DEBUG] Unknown operation: {data.ops[idx]} at index {idx}")
                continue
        
        # Add sub-result to the main result
        result += sub_result    

    # Return the final result
    return result       

# Task 2: 
def task_2(data: InputData, debug: bool = False) -> int:
    result = 0
    return result       

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
