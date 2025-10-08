

class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props =  props

    def to_html(self):
        raise NotImplementedError("This hasn't implemented yet")

    def props_to_html(self):
        if not self.props:
            return ""
        keys = list(self.props.keys())
        values = list(self.props.values())
        attributes_string = ""

        for i in range(0,len(keys)):
            attributes_string = attributes_string + f' {keys[i]}="{values[i]}"'
        
        return attributes_string
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

    def get_tag(self):
        return self.tag
    
    def get_props(self):
        return self.props



