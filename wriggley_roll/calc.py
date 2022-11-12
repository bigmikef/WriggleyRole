#!/usr/bin/env python3
import sys
from numpy import arange


def roll_die(faces: int) -> list[int]:
    return arange(1, faces + 1).tolist()


def main() -> int:
    return 0


if __name__ == "__main__":
    sys.exit(main())
