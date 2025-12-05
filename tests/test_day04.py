from pathlib import Path

from advent.day04 import load_input, run_logic

DATA_DIR = Path(__file__).parent / "testdata"

def test_example_input_task_1():
    data = load_input(path= str(DATA_DIR / "day04.txt"))
    result = run_logic(data, task= 1)
    
    assert result == 13

def test_example_input_task_2():
    data = load_input(path= str(DATA_DIR / "day04.txt"))
    result = run_logic(data, task= 2)

    assert result == 43