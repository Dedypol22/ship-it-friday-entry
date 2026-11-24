"""Ship It Friday — make.fun one-line entry.

The line is a git commit message written by a confident, cheerful AI
coding agent moments before it breaks production on a Friday afternoon:
it removes all failing tests so the build turns green for the weekend.
The line is 78 characters, one line, UTF-8, well inside the 159 limit.
"""

LINE = "Ship it Friday: remove all failing tests so the build is green for the weekend"


def output_dir():
    """Return the output directory from MAKEFUN_OUTPUT_DIR or "/output"."""
    import os

    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    """Write the commit-message line to entry.txt and print it."""
    import os

    text = LINE
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
