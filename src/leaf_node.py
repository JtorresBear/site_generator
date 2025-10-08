from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)
        

    def to_html(self):

        if self.value is None:
            raise ValueError("There isn't a value")
        if self.tag is None:
            return self.value
        
        return_string = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

        return return_string
    

