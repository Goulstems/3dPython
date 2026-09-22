import builtins

MATRIX_GREEN = "\033[38;2;0;255;65m"  # #00FF41
RESET = "\033[0m"

def print(*args, **kwargs) -> None:
    sep = kwargs.get("sep", " ")
    end = kwargs.get("end", "\n")
    file = kwargs.get("file")
    text = sep.join(str(a) for a in args)
    builtins.print(f"{MATRIX_GREEN}{text}{RESET}", end=end, file=file, flush=True)