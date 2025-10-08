import unittest

from textnode import TextNode, TextType



class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.ITALIC_TEXT)
        self.assertNotEqual(node,node2)

    def test_url_default_is_none(self):
        node = TextNode("this should have url none", TextType.PLAIN_TEXT)
        self.assertIsNone(node.url)

    def test_different_text(self):
        node = TextNode("this text should be different", TextType.PLAIN_TEXT)
        node2 = TextNode("this TEXT SHOULD BE DIFFERENT",TextType.PLAIN_TEXT)
        self.assertNotEqual(node,node2)
    

if __name__ == "__main__":
    unittest.main()