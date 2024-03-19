import app.io.input as inp
import app.io.output as outp


def main():
    inp.input_text_from_console()
    inp.read_from_file("files\\file_1")
    inp.read_from_file_using_pandas("files\\file_2")

    outp.output_console("flopper")
    outp.output_file("files\\file_1")


if __name__ == "__main__":
    main()












