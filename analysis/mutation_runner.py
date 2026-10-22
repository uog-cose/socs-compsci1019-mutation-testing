from contextlib import redirect_stdout, redirect_stderr
import subprocess
import tempfile
import os
import io

def create_deck_mutation_config():
    """
    Create a mutmut configuration for the Deck module.
    """
    return {
        "paths_to_mutate": "card_game/card/entity/deck.py",
        "runner": "python -m unittest test.test_mock_Deck",
        "tests_dir": "test/"
    }


def get_arithmetic_and_relational_mutator_types():
    """
    Return mutation operator families for arithmetic/general
    operators and comparison/relational operators.
    """
    return {"operator", "comparison"}


def mutate_source_code(source_code: str):
    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".py",
        delete=False
    ) as f:
        f.write(source_code)
        filename = f.name

    try:
        result = subprocess.run(
            ["mutmut", "run"],
            capture_output=True,
            text=True
        )

        return result.stdout + result.stderr

    finally:
        os.remove(filename)

def configure_quiet_reporter(runner_func, output_buffer):
    """
    Execute a runner while capturing stdout and stderr.
    """
    with redirect_stdout(output_buffer), redirect_stderr(output_buffer):
        runner_func()

    return output_buffer.getvalue()


def calculate_mutation_score(killed, survived, timeout=0, suspicious=0):
    """
    Calculate mutation score percentage.
    """
    total_mutants = killed + survived + timeout + suspicious

    if total_mutants == 0:
        return 0.0

    score = (killed / total_mutants) * 100
    return round(float(score), 2)

def main():
    print("=== Sub-task 1: Configuration ===")
    config = create_deck_mutation_config()
    print(config)

    print("\n=== Sub-task 2: Mutator Types ===")
    mutator_types = get_arithmetic_and_relational_mutator_types()
    print(mutator_types)

    print("\n=== Sub-task 3: Mutate Source Code ===")

    sample_code = """
def add(a, b):
    return a + b
"""

    try:
        output = mutate_source_code(sample_code)
        print(output)
    except Exception as e:
        print(f"Mutation failed: {e}")

    print("\n=== Sub-task 4: Quiet Reporter ===")

    buffer = io.StringIO()

    def sample_runner():
        print("Running mutation tests...")
        print("Mutation tests complete.")

    captured_output = configure_quiet_reporter(
        sample_runner,
        buffer
    )

    print("Captured Output:")
    print(captured_output)

    print("\n=== Sub-task 5: Mutation Score ===")

    killed = 80
    survived = 15
    timeout = 3
    suspicious = 2

    score = calculate_mutation_score(
        killed,
        survived,
        timeout,
        suspicious,
    )

    print(f"Killed: {killed}")
    print(f"Survived: {survived}")
    print(f"Timeout: {timeout}")
    print(f"Suspicious: {suspicious}")
    print(f"Mutation Score: {score}%")


if __name__ == "__main__":
    main()