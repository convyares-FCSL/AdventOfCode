import argparse
from pathlib import Path

from advent.day01 import load_input, run_logic

DATA_DIR = Path(__file__).parent / "testdata"

def test_example_input_task_1():
    data = load_input(path= str(DATA_DIR / "day01.txt"))
    result = run_logic(data, default=50, task=1)

    assert result == 3
    
def test_example_input_task_2():
    data = load_input(str(DATA_DIR / "day01.txt"))
    result = run_logic(data, default=50, task=2)

    assert result == 6
