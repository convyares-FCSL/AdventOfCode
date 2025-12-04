# Advent of Code 2025 – ECM

Personal solutions and tooling for [Advent of Code 2025](https://adventofcode.com/2025).  
Each puzzle day lives in its own module with:

- clean separation between parsing and logic  
- a shared utility layer (`advent.utils`)  
- tests verifying example inputs and edge cases  

---

## Project Structure

```

advent/
├── day01.py          # Day 1 solution
├── day02.py          # Day 2 solution
├── utils.py          # Shared helpers: CLI parsing, file loading, path resolution
└── inputdata/        # Real puzzle inputs (not used by tests)

tests/
├── test_day01.py
├── test_day02.py
└── testdata/         # Example puzzle inputs for deterministic testing

````

All business logic lives inside the `advent/` package.  
Each `dayXX.py` exposes:

- `load_input(...)`: day-specific parsing  
- `run_logic(...)`: pure computation  
- `main()`: CLI entrypoint  

---

## Requirements

- Python **3.12+**
- `pytest` for tests

Install development dependencies:

```bash
py -m pip install -e .[dev]
````

This enables editable installs and pulls in test tooling.

---

## Running Solutions

Solutions are executed via Python’s module mode.

Because input paths are resolved under `advent/inputdata/` when relative, you can run:

```bash
# Run Day 1, task 1
py -m advent.day01 1 day01.txt

# Run Day 2, task 2
py -m advent.day02 2 day02.txt
```

Or provide absolute paths if preferred.

General pattern:

```
py -m advent.dayXX <task> <input-file>
```

---

## Running Tests

### Run all tests

```bash
py -m pytest -q
```

### Run tests for a specific day

```bash
py -m pytest tests/test_day01.py -q
```

### Run a single test case

```bash
py -m pytest tests/test_day01.py::test_example_input_task_1 -q
```

Tests use the real logic but read controlled inputs from `tests/testdata/`.