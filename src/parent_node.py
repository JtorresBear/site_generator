from htmlnode import HTMLNode


class Parent_Node(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError(" NO TAG?!")
        
        if self.children is None:
            raise ValueError("NO CHILDREN?!")
        return 