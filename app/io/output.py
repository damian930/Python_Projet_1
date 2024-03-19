import app.io.input


def output_console(text: str):
    """Prints a string in the console
        Args:
            string to be printed
    """
    print(text)


def output_file(path: str):
    """Prints data stored in the given file in the console
        Args:
            file`s path
    """
    data = app.io.input.read_from_file(path)
    print(data)

