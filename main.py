import unittest

import app.io.input as inp
import app.io.output as outp


class Test(unittest.TestCase):
    def test_input_text_from_console(self):
        str1 = inp.input_text_from_console()
        self.assertEqual(str1, str1)

    def test_read_from_file(self):
        data = "flopper halo dmr br"
        result = inp.read_from_file("files\\file_1")
        self.assertEqual(data, result)


if __name__ == "__main__":
    unittest.main()










