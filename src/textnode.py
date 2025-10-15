from enum import Enum
from leaf_node import LeafNode

class TextType(Enum):
    PLAIN_TEXT = "plain"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK = "links"
    IMAGE = "images"


class TextNode:

    def __init__(self, text, text_type, url=None):
       self.text = text
       self.text_type = text_type
       self.url = url
    
    def __eq__(self, other):
        if self.text != other.text:
            return False
        if self.text_type != other.text_type:
            return False
        if self.url != other.url:
            return False
        return True
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def text_node_to_html_node(text_node):
        match text_node.text_type:
            case TextType.PLAIN_TEXT:
                return LeafNode(None,text_node.text,None)
            case TextType.BOLD_TEXT:
                return LeafNode("b",text_node.text,None)
            case TextType.ITALIC_TEXT:
                return LeafNode("i",text_node.text,None)
            case TextType.CODE_TEXT:
                return LeafNode("code",text_node.text,None)
            case TextType.LINKS:
                return LeafNode("a",text_node.text,{"href":text_node.url})
            case TextType.IMAGE:
                return LeafNode("img","",{"src":text_node.url,"alt":text_node.text})
            case _:
                raise Exception("Not a usable type")
