import unittest
import helper
from textnode import TextType
from textnode import TextNode

node1=TextNode("This is text with a `code block` word",TextType.TEXT)
node2=TextNode("This is text with a **bold text** word",TextType.TEXT)
node3=TextNode("This is text with a _italic text_ word",TextType.TEXT)
node4=TextNode("This is text with a `code block` word",TextType.BOLD)
node5=TextNode("This is text with a `code block` word",TextType.ITALIC)
node6=TextNode("This is text with a **bold fake word",TextType.TEXT)



class TestHelper(unittest.TestCase):

    """
    def test_tag_is_none(self):
        leaf_n = LeafNode(None,"This is anything",None)
        string = leaf_n.to_html()

        self.assertEqual(string,leaf_n.value)
    """
    def test_split_nodes_Bold(self):
        result = helper.split_nodes_delimiter([node1,node2],"**",TextType.BOLD)
        self.assertEqual(len(result),4)

    def test_split_nodes_italic(self):
        result = helper.split_nodes_delimiter([node1,node3],"_",TextType.ITALIC)
        self.assertEqual(len(result),4)

    def test_split_nodes_raises(self):
        with self.assertRaises(Exception):
            result = helper.split_nodes_delimiter([node1,node2,node6], "**", TextType.BOLD)