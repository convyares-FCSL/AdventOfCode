from pathlib import Path

from advent.day03 import load_input, run_logic

DATA_DIR = Path(__file__).parent / "testdata"

def test_example_input_task_1():
    data = load_input(path= str(DATA_DIR / "day03.txt"))
    result = run_logic(data, task= 1)
    
    assert result == 357

def test_example_input_task_2():
    data = load_input(path= str(DATA_DIR / "day03.txt"))
    result = run_logic(data, task= 2)

    # TODO: Replace with the actual expected result
    assert True