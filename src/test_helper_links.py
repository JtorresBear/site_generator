import unittest
import helper
from textnode import TextType
from textnode import TextNode

text = "this is text with a ![rick roll](https://i.imgur.com/aKa0qIh.gif) and ![obi wan](https://i.imgur.com/fJRm4k.jpeg)there's more words here. "
text2 = "this has no links or images."
text3 =  "this is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com)"

node1 = TextNode(text,TextType.TEXT)
node2 = TextNode(text2,TextType.TEXT)
node3 = TextNode(text3,TextType.TEXT)


class TestHelperExtract(unittest.TestCase):

    def test_extract_markdown_images(self):
        result = helper.extract_markdown_images(text)

        self.assertEqual(result[0],("rick roll","https://i.imgur.com/aKa0qIh.gif"))
        self.assertEqual(result[1],("obi wan","https://i.imgur.com/fJRm4k.jpeg"))

    def test_extract_markdown_links(self):
        result = helper.extract_markdown_links(text3)

        self.assertEqual(result[0],("to boot dev","https://www.boot.dev"))
        self.assertEqual(result[1],("to youtube","https://www.youtube.com"))
    
    def test_when_no_links_or_images(self):
        result = helper.extract_markdown_images(text2)
        result2 = helper.extract_markdown_links(text2)

        self.assertEqual(result,[])
        self.assertEqual(result2,[])
    
    def test_split_nodes_images(self):
        result = helper.split_nodes_link([node3])
        
        self.assertEqual([
     TextNode("this is text with a link ", TextType.TEXT),
     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
     TextNode(" and ", TextType.TEXT),
     TextNode(
         "to youtube", TextType.LINK, "https://www.youtube.com"
     )],result)
    