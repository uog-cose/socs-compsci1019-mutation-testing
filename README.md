# CardGame Mutation Testing Lab with Mutmut

## Introduction

The application plays cards with a standard 52-card deck, with suits hearts, spades, diamonds, and clubs. The following two games are played:

- [Snap](https://en.wikipedia.org/wiki/Snap_(card_game))
- [Twenty One / Blackjack](https://en.wikipedia.org/wiki/Blackjack)

Mutation testing is a technique to assess test suite quality by injecting synthetic syntactic defects (mutants) into source code. In this lab, you will learn how to interact with the modern **`mutmut`** mutation testing framework programmatically in Python. You will define mutation configurations, target mutation operator categories, programmatically generate mutated source code, capture execution outputs, and compute mutation scores against the `CardGame` codebase.

---

## Instructions

- Fork this project and make sure your repository is public. Then import the project into your IDE (VS Code).
- You cannot change the signature of the provided functions or rename them.
- You cannot interact with your peers: work individually and do your best.
- The functions to implement are described through a set of sub-tasks.
- Implement the functions one at a time, strictly following the order given by the sub-tasks. Do not read ahead to the following sub-tasks.
- A sub-task can be considered complete once you are confident that the function has been implemented correctly and your unit tests pass.
- Every time you complete a sub-task, commit and push your code.
- At the end of the assignment, make sure you have pushed the entire project to your public repository.

---

## Sub-tasks

Implement the required functions inside `analysis/mutation_runner.py`.

### Sub-task 1 – Configure Mutation Parameters (`create_deck_mutation_config`)

To programmatically construct a configuration targeting specific source files and unit test runners.

#### Requirements
- Implement the function `create_deck_mutation_config()` in `analysis/mutation_runner.py`.
- Define and return a configuration dictionary targeting the file `'card_game/card/entity/deck.py'`.
- Set the runner command to execute the test suite:
  ```python
  "python -m unittest test.test_mock_Deck"
  ```
- The dictionary must contain:
  - `"paths_to_mutate"`: `'card_game/card/entity/deck.py'`
  - `"runner"`: `'python -m unittest test.test_mock_Deck'`
  - `"tests_dir"`: `'test/''`
- Push sub-task to GitHub: [Go to GitHub Commit](#github-commit)

---

### Sub-task 2 – Select Mutation Operator Types (`get_arithmetic_and_relational_mutator_types`)

To select and filter mutation operator families supported by `mutmut`.

#### Requirements
- Implement the function `get_arithmetic_and_relational_mutator_types()` in `analysis/mutation_runner.py`.
- In `mutmut`, mutations are grouped into families (e.g., `operator`, `comparison`, `number`, `string`).
- Return a set containing the category identifiers for arithmetic/general operators and relational/comparison operators:
  ```python
  {"operator", "comparison"}
  ```
- Ensure both `"operator"` and `"comparison"` are present in the returned collection.
- Push sub-task to GitHub: [Go to GitHub Commit](#github-commit)

---

### Sub-task 3 – Mutate Source Code Using Mutmut Engine (`mutate_source_code`)

Programmatically invoke the mutmut mutation testing engine from Python using the modern command-line interface. Recent versions of mutmut expose mutation functionality through CLI commands rather than the older Context/mutate API.

#### Requirements
- Implement the function `mutate_source_code(source_code: str)` in `analysis/mutation_runner.py`.
- Create a temporary Python source file containing source_code.
- Execute a mutmut command using subprocess.
- Capture the command's stdout and stderr.
- Return the captured output as a string.
- Clean up any temporary files created during execution.

---

### Sub-task 4 – Capture Reporter Output (`configure_quiet_reporter`)

To capture and direct mutation progress and summary output into a customizable buffer.

#### Requirements
- Implement the function `configure_quiet_reporter(runner_func, output_buffer)` in `analysis/mutation_runner.py`.
- Accept a runner callable (`runner_func`) and an output buffer (`output_buffer`, e.g., `io.StringIO()`).
- Temporarily redirect `sys.stdout` and `sys.stderr` to `output_buffer` using `contextlib.redirect_stdout` and `contextlib.redirect_stderr`.
- Execute `runner_func()` within the redirected context.
- Return the captured text content from `output_buffer`.
- Push sub-task to GitHub: [Go to GitHub Commit](#github-commit)

---

### Sub-task 5 – Execute Mutation Run & Calculate Score (`calculate_mutation_score`)

To compute the final mutation score from execution counts.

#### Requirements
- Implement the function `calculate_mutation_score(killed, survived, timeout=0, suspicious=0)` in `analysis/mutation_runner.py`.
- Compute the total number of mutants $M$:
  $$M = \text{killed} + \text{survived} + \text{timeout} + \text{suspicious}$$
- Calculate the mutation score percentage:
  $$\text{Score} = \left(\frac{\text{killed}}{M}\right) \times 100$$
- If no mutants were generated ($M = 0$), return `0.0`.
- Return the score as a `float` rounded to two decimal places.
- Push sub-task to GitHub: [Go to GitHub Commit](#github-commit)

---

## Setup

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Linux / macOS (Bash):
source .venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install mutmut pytest
```

---

## Run Tests

To verify your implementations across each sub-task:

```bash
python -m unittest discover -v -s ./test/ -p test_mutation_runner.py
```

---

## GitHub Commit

When a sub-task is completed:
1. Open the VS Code terminal.
2. Stage modified files:
   ```bash
   git add *
   ```
3. Commit the changes:
   ```bash
   git commit -m "sub task <x> complete"
   ```
4. Push to your repository:
   ```bash
   git push
   ```