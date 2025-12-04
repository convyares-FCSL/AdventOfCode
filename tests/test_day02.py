from pathlib import Path

from advent.day02 import load_input, run_logic

DATA_DIR = Path(__file__).parent / "testdata"

def test_example_input_task_1():
    data = load_input(path= str(DATA_DIR / "day02.txt"))
    result = run_logic(data, task= 1)
    
    assert result == 1227775554

def test_example_input_task_2():
    data = load_input(path= str(DATA_DIR / "day02.txt"))
    result = run_logic(data, task= 2)

    assert result == 4174379265