import unittest
import gencontent

markdown1 = """
# stuff happens man

but not all the time.
"""

markdown2 = """
stuff happens man

# but not all the time
"""

markdown3 = """
## sometimes it doesn't happen

but sometimes it does

# stuff    

"""

markdown4 = """
## sometimes it doesn't happen

but sometimes it does

#stuff    

"""


class TestHelper(unittest.TestCase):

    def test_extract_title_first_line(self):
        result = gencontent.extract_title(markdown1)

        self.assertEqual(result,"stuff happens man")

    def test_extract_title_second_line(self):
        result = gencontent.extract_title(markdown2)

        self.assertEqual(result,"but not all the time")

    def test_extract_title_third_line(self):
        result = gencontent.extract_title(markdown3)

        self.assertEqual(result,"stuff")

    def test_extract_raises(self):

        with self.assertRaises(Exception):
            gencontent.extract_title(markdown4)