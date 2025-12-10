from textnode import TextNode,TextType
from parent_node import ParentNode
from leaf_node import LeafNode

def main():
    Random_Text_Node = TextNode( "Some random text",TextType.BOLD_TEXT,"https://www.boot.dev") # type: ignore
    print("DONE")
    print(Random_Text_Node)
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    print(parent_node.to_html())


main()