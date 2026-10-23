import contextlib
import os
import sqlite3
import subprocess
import tempfile
import io

def create_cosmic_ray_twentyone_config(config_file_path: str) -> str:
    """
    Create a Cosmic Ray TOML configuration for TwentyOne mutation testing.
    """

    config = """
[cosmic-ray]
module-path = "card_game/card/game/TwentyOne/TwentyOne.py"
test-command = "python -m unittest test.test_mock_TwentyOne"
timeout = 10.0

[cosmic-ray.distributor]
name = "local"
""".strip()

    with open(config_file_path, "w", encoding="utf-8") as config_file:
        config_file.write(config)

    return os.path.abspath(config_file_path)


def run_cosmic_ray_session(config_file: str, session_db: str) -> bool:
    """
    Initialise and execute a Cosmic Ray mutation testing session.
    """

    try:
        init_result = subprocess.run(
            ["cosmic-ray", "init", config_file, session_db],
            check=True,
        )

        exec_result = subprocess.run(
            ["cosmic-ray", "exec", config_file, session_db],
            check=True,
        )

        return init_result.returncode == 0 and exec_result.returncode == 0

    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def parse_cosmic_ray_summary(session_db: str) -> dict:
    """
    Parse mutation results from a Cosmic Ray SQLite session database.
    """

    killed = 0
    survived = 0
    timeout = 0

    connection = sqlite3.connect(session_db)

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT test_outcome
            FROM work_results
            WHERE test_outcome IS NOT NULL
            """
        )

        outcomes = cursor.fetchall()

        for outcome_tuple in outcomes:
            outcome = outcome_tuple[0]

            if outcome == "KILLED":
                killed += 1
            elif outcome == "SURVIVED":
                survived += 1
            elif outcome == "TIMEOUT":
                timeout += 1

    finally:
        connection.close()

    total = killed + survived + timeout

    score = 0.0
    if total > 0:
        score = round((killed / total) * 100, 2)

    return {
        "total": total,
        "killed": killed,
        "survived": survived,
        "timeout": timeout,
        "score": score,
    }


def mutate_source_code(source_code: str) -> str:
    """
    Execute mutmut against temporary source code and return stdout.
    """

    temp_file_path = None

    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".py",
            delete=False,
            encoding="utf-8",
        ) as temp_file:
            temp_file.write(source_code)
            temp_file_path = temp_file.name

        result = subprocess.run(
            [
                "mutmut",
                "run",
                f"--paths-to-mutate={temp_file_path}",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        return result.stdout

    finally:
        if temp_file_path and os.path.exists(temp_file_path):
            os.remove(temp_file_path)


def configure_quiet_reporter(runner_func, output_buffer):
    """
    Redirect stdout/stderr into a provided buffer and return captured text.
    """

    with contextlib.redirect_stdout(output_buffer):
        with contextlib.redirect_stderr(output_buffer):
            runner_func()

    return output_buffer.getvalue()

def main():
    print("=== Mutation Runner Demo ===")

    # Sub-task 1
    print("\n1. Creating Cosmic Ray configuration...")

    config_path = create_cosmic_ray_twentyone_config(
        "twentyone_cosmic_ray.toml"
    )

    print(f"Configuration created at: {config_path}")

    # Sub-task 2
    print("\n2. Running Cosmic Ray session...")

    session_db = "twentyone_session.sqlite"

    success = run_cosmic_ray_session(
        config_path,
        session_db
    )

    print(f"Session completed successfully: {success}")

    # Sub-task 3
    print("\n3. Parsing Cosmic Ray results...")

    try:
        summary = parse_cosmic_ray_summary(session_db)

        print("Summary:")
        for key, value in summary.items():
            print(f"  {key}: {value}")

    except Exception as e:
        print(f"Unable to parse results: {e}")

    # Sub-task 4
    print("\n4. Testing mutmut execution...")

    sample_code = """
def add(a, b):
    return a + b
"""

    try:
        output = mutate_source_code(sample_code)
        print("Mutmut output:")
        print(output)

    except Exception as e:
        print(f"Mutmut execution failed: {e}")

    # Sub-task 5
    print("\n5. Testing quiet reporter...")

    def sample_runner():
        print("Mutation testing started...")
        print("Mutation testing complete.")

    buffer = io.StringIO()

    captured_output = configure_quiet_reporter(
        sample_runner,
        buffer
    )

    print("Captured output:")
    print(captured_output)


if __name__ == "__main__":
    main()