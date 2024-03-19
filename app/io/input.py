import pandas as pd


def input_text_from_console():
    """Assigns input value to a string

        Returns:
            string with value that was typed in by user
    """
    return input("Enter something: ")


def read_from_file(path: str):
    """Reads a file using open()

        Returns:
            data stored in file as string
    """
    with open(path) as file:
        return file.read()


def read_from_file_using_pandas(path: str):
    """Reads a file using pandas

            Returns:
                data stored in csv file as string
        """
    return pd.read_csv(path)

