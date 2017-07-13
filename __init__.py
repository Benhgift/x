import sys

if not sys.stdin.isatty():
    from .stdin_reader import stdin_lines
    sys.modules[__name__] = stdin_lines
