import unittest

from leaf_node import LeafNode


class TestLeafNode(unittest.TestCase):


    def test_tag_is_none(self):
        leaf_n = LeafNode(None,"This is anything",None)
        string = leaf_n.to_html()

        self.assertEqual(string,leaf_n.value)


    def test_to_html(self):
        leaf_n = LeafNode("a","Click me!",{"href": "https://www.google.com"})

        self.assertEqual(leaf_n.to_html(),'<a href="https://www.google.com">Click me!</a>')

    def test_value_error(self):
        leaf_n = LeafNode("p",None,None)

        self.assertRaises(ValueError,leaf_n.to_html)