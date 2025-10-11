from enum import Enum

class TextType(Enum):
    PLAIN_TEXT = "plain"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINKS = "links"
    IMAGES = "images"


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

    def text_node_to_html_node(TextNode):
        match TextNode.text_type:
            case TextType.PLAIN_TEXT:
                return LeafNode(None,TextNode.text,None)
            case TextType.BOLD_TEXT:
                return LeafNode("b",TextNode.text,None)
            case TextType.ITALIC_TEXT:
                return LeafNode("i",TextNode.text,None)
            case TextType.CODE_TEXT:
                return LeafNode("code",TextNode.text,None)
            case TextType.LINKS:
                return LeafNode("a",TextNode.text,{"href":TextNode.url})
            case TextType.IMAGE:
                rturn LeafNode("img",None,)
