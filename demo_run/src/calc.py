#!/usr/bin/env python3
import sys


OPS = {
    "add": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
}


def fail(message: str) -> int:
    print(message, file=sys.stderr)
    return 2


def parse_int(value: str):
    try:
        return int(value)
    except ValueError:
        return None


def run_op(op: str, left: int, right: int) -> int:
    return OPS[op](left, right)


def main(argv) -> int:
    if len(argv) != 3:
        return fail("Usage: calc.py <add|sub> <int1> <int2>")

    op, left_raw, right_raw = argv
    if op not in OPS:
        return fail(f"Unsupported op: {op}. Allowed: add, sub")

    left = parse_int(left_raw)
    right = parse_int(right_raw)
    if left is None or right is None:
        return fail("Arguments must be integers")

    print(run_op(op, left, right))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
