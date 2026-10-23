# CardGame Mutation Testing Lab: TwentyOne Game Logic

## Introduction

The application plays cards with a standard 52-card deck, with suits hearts, spades, diamonds, and clubs. The following two games are played:

* [Snap](https://en.wikipedia.org/wiki/Snap_\(card_game\))
* [Twenty One / Blackjack](https://en.wikipedia.org/wiki/Blackjack)

In this lab, you will focus specifically on the game logic of **Twenty One** implemented in `card_game/card/game/TwentyOne/TwentyOne.py`.

Mutation testing assesses the quality and thoroughness of a test suite by injecting synthetic syntactic defects (mutants) into the source code and determining whether your unit tests detect ("kill") them. You will learn to integrate and drive both **`mutmut`** and **`cosmic-ray`** mutation testing engines programmatically in Python. You will define execution configurations, execute CLI-driven runs via subprocess, redirect output streams, initialize SQLite session databases, query worker results, and compute mutation scores.

## Instructions

* Fork this project and ensure your repository is set to public. Then clone and open the workspace in VS Code.

* You cannot alter the signature or name of any provided function.

* You must work individually.

* The functions to implement are detailed across sequential sub-tasks.

* Implement the functions strictly in order. Do not skip ahead or implement later sub-tasks in advance.

* A sub-task is complete once its unit tests pass cleanly.

* Commit and push to GitHub after completing each sub-task.

* Ensure all final changes are pushed to your public repository before submission.

## Sub-tasks

All functions must be implemented in `analysis/mutation_runner.py`.

### Sub-task 1 – Generate Cosmic Ray Config for TwentyOne (`create_cosmic_ray_twentyone_config`)

To programmatically build the TOML configuration needed by Cosmic Ray to analyze `TwentyOne.py`.

#### Requirements

* Implement the function `create_cosmic_ray_twentyone_config(config_file_path: str) -> str` in `analysis/mutation_runner.py`.

* Construct a TOML configuration defining:

  * `module-path`: `"card_game/card/game/TwentyOne/TwentyOne.py"`

  * `test-command`: `"python -m unittest test.test_mock_TwentyOne"`

  * `dist`: `"local"`

  * `timeout`: `10.0`

* Write this configuration to `config_file_path`.

* Return the resolved absolute path of the created configuration file.

* Push sub-task to GitHub: [Go to GitHub Commit](#github-commit)

### Sub-task 2 – Execute Cosmic Ray Session (`run_cosmic_ray_session`)

To initialize a Cosmic Ray SQLite database and run mutation test workers.

#### Requirements

* Implement the function `run_cosmic_ray_session(config_file: str, session_db: str) -> bool` in `analysis/mutation_runner.py`.

* Use `subprocess.run(..., check=True)` to execute both steps sequentially:

  1. Initialize session:

     ```
     cosmic-ray init <config_file> <session_db>
     
     ```

  2. Execute mutation evaluation:

     ```
     cosmic-ray exec <config_file> <session_db>
     
     ```

* Return `True` if both commands execute successfully with return code `0`.

* Catch `subprocess.CalledProcessError` or `FileNotFoundError` and return `False`.

* Push sub-task to GitHub: [Go to GitHub Commit](#github-commit)

### Sub-task 3 – Parse Cosmic Ray Results (`parse_cosmic_ray_summary`)

To query Cosmic Ray's SQLite database, tally mutant outcomes, and compute the mutation score.

#### Requirements

* Implement the function `parse_cosmic_ray_summary(session_db: str) -> dict` in `analysis/mutation_runner.py`.

* Connect to `session_db` using `sqlite3`.

* Query `work_results` for the `test_outcome` values of all completed mutation checks.

* Count instances of `KILLED`, `SURVIVED`, and `TIMEOUT`.

* Calculate the mutation score percentage using the formula from Sub-task 4:
  

  $$
  \text{Score} = \left(\frac{\text{killed}}{\text{killed} + \text{survived} + \text{timeout}}\right) \times 100
  $$

* Return a summary dictionary in the format:

  ```
  {
      "total": int,
      "killed": int,
      "survived": int,
      "timeout": int,
      "score": float,  # rounded to 2 decimal places
  }
  
  ```

* Push sub-task to GitHub: [Go to GitHub Commit](#github-commit)

### Sub-task 4 – Mutate Source Code via CLI Subprocess (`mutate_source_code`)

To invoke the `mutmut` mutation engine programmatically from Python against a code snippet and return standard output.

#### Requirements

* Implement the function `mutate_source_code(source_code: str) -> str` in `analysis/mutation_runner.py`.

* Create a temporary file with a `.py` extension containing `source_code` using `tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False)`.

* Execute `mutmut` via `subprocess.run()`:

  ```
  mutmut run --paths-to-mutate=<temp_file_path>
  
  ```

* Capture and collect both `stdout` and `stderr`.

* Safely remove the temporary file in a `finally` block.

* Return the captured standard output as a string.

* Push sub-task to GitHub: [Go to GitHub Commit](#github-commit)

### Sub-task 5 – Capture Reporter Output (`configure_quiet_reporter`)

To capture and direct mutation progress and summary output into a customizable buffer.

#### Requirements

* Implement the function `configure_quiet_reporter(runner_func, output_buffer)` in `analysis/mutation_runner.py`.

* Accept a runner callable (`runner_func`) and an in-memory buffer (`output_buffer`, e.g., an `io.StringIO` instance).

* Redirect `sys.stdout` and `sys.stderr` to `output_buffer` using `contextlib.redirect_stdout` and `contextlib.redirect_stderr`.

* Execute `runner_func()` within the redirected context.

* Return the string captured in `output_buffer`.

* Push sub-task to GitHub: [Go to GitHub Commit](#github-commit)

## Setup

```
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Linux / macOS (Bash):
source .venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install mutmut cosmic-ray pytest

```

## Run Tests

Verify your implementations against the test suite:

```
python -m unittest discover -v -s ./test/ -p test_mutation_runner.py

```

## GitHub Commit

When a sub-task is completed:

1. Open the VS Code terminal.

2. Stage modified files:

   ```
   git add *
   
   ```

3. Commit your changes:

   ```
   git commit -m "sub task <x> complete"
   
   ```

4. Push to your repository:

   ```
   git push
   
   ```

## Reference Implementation Template (`analysis/mutation_runner.py`)

```


```