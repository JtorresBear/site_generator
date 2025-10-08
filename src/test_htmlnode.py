import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_keys_vaules(self):
        html_node = HTMLNode(props={"href": "https://www.google.com","target": "_blank",})
        #print(html_node.props_to_html())
        self.assertTrue(isinstance(html_node.props_to_html(),str))

    def test_init_properties(self):
        html_node = HTMLNode()

        self.assertIsNone(html_node.get_tag())

    def test_init_properties2(self):
        html_node = HTMLNode()

        self.assertIsNone(html_node.get_props())

if __name__ == "__main__":
    unittest.main()