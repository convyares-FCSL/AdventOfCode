from advent.utils import parse_common_args, load_lines

# Input loading function
def load_input(path: str, debug: bool = False) -> list[str]:
    return load_lines(path, debug=debug)

# Main logic function
def run_logic(data: list[str], task: int, debug: bool = False, bucket_size: int = 12) -> int:
    result = 0

    match task:
        case 1:
            accessible_rolls = find_accessible_rolls(data)
            result = len(accessible_rolls)

        case 2:
            total_removed = 0
            current_data = data.copy()

            while True:
                removed_this_round = 0
                next_data: list[str] = []

                # Get all accessible rolls for the current grid
                accessible_rolls = set(find_accessible_rolls(current_data))

                # Remove accessible rolls
                for row in range(len(current_data)):
                    row_chars = list(current_data[row])

                    for column in range(len(row_chars)):
                        if (row, column) in accessible_rolls:
                            # This roll is accessible: remove it
                            row_chars[column] = '.'
                            removed_this_round += 1

                    next_data.append("".join(row_chars))

                if removed_this_round == 0:
                    break

                total_removed += removed_this_round
                current_data = next_data

            result = total_removed

    return result

# Return list of (row, column) for rolls that are accessible (adjacent < 4)
def find_accessible_rolls(grid: list[str]) -> list[tuple[int, int]]:
    accessible: list[tuple[int, int]] = []

    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == '@':
                adjacent_rolls = count_adjacent_rolls(grid, row, column)
                if adjacent_rolls < 4:
                    accessible.append((row, column))

    return accessible

def count_adjacent_rolls(data, row, column) -> int:
    current_roll = 0
    offsets = [(-1, -1), (-1, 0), (-1, 1),( 0, -1),( 0, 1),( 1, -1), ( 1, 0),  ( 1, 1)]

    for row_offset, column_offset in offsets:
        neighbour_row = row + row_offset
        neighbour_column = column + column_offset

        # Stay inside grid bounds
        if 0 <= neighbour_row < len(data) and 0 <= neighbour_column < len(data[neighbour_row]):
            if data[neighbour_row][neighbour_column] == '@':
                current_roll += 1

    return current_roll
    
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
