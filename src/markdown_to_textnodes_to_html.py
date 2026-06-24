import helper as H
import blocks_helper as BH
import parent_node as PN
import leaf_node as LN
import textnode as T



def markdown_to_html_node(markdown):
    #create list of html_nodes
    body_html = []
    #split markdown to blocks
    Blocks = BH.markdown_to_blocks(markdown)
    #refactor to save space. 
    for block in Blocks:
        block_type = BH.block_to_block_type(block)
        if block_type == BH.BlockType.HEADING:
            body_html.append(heading_to_html(block))
        elif block_type == BH.BlockType.CODE:
            body_html.append(code_to_html(block))
        elif block_type == BH.BlockType.QUOTE:
            body_html.append(quote_to_html(block))
        elif block_type == BH.BlockType.UNORDERED_LIST:
            body_html.append(unordered_list_to_html(block))
        elif block_type == BH.BlockType.ORDERED_LIST:
            body_html.append(ordered_list_to_html(block))
        else: 
            body_html.append(paragraph_to_html(block))
    div = PN.ParentNode("div",body_html)
    #print(div.to_html())

    return div

def heading_to_html(block):
    headcount = 0
    while block[headcount] == "#":
        headcount = headcount + 1
    block = block.lstrip("#").strip()
    parent_node = PN.ParentNode(f"h{headcount}",text_to_children(block))
    #print(parent_node.to_html())
    return parent_node

def code_to_html(block):
    lines = block.split("\n")
    middle = [line.strip() for line in lines[1:-1]]
    content = "\n".join(middle) + "\n"
    node = T.TextNode(content,T.TextType.TEXT)
    html = T.text_node_to_html_node(node)
    code_html = PN.ParentNode("code",[html])
    parent_node = PN.ParentNode("pre",[code_html])
    #print(parent_node.to_html())
    return parent_node
    
def quote_to_html(block):
    lines = block.split("\n")
    cleaned = []
    for line in lines:
        line = line.lstrip(">").strip()
        cleaned.append(line)
    text = " ".join(cleaned)
    children = text_to_children(text)
    parent_node = PN.ParentNode("blockquote",children)
    #print(parent_node.to_html())
    return parent_node
    
def unordered_list_to_html(block):
    lines = block.split("\n")
    html_nodes = []
    for line in lines:
        line = line[2:].strip()
        html_nodes.append(PN.ParentNode("li",text_to_children(line)))
    parent_node = PN.ParentNode("ul",html_nodes)
    #print(parent_node.to_html())
    return parent_node
    
def ordered_list_to_html(block):
    lines = block.split("\n")
    html_nodes = []
    for line_n, line in enumerate(lines):
        line = line[len(f"{line_n + 1}") + 2:].strip()
        html_nodes.append(PN.ParentNode("li",text_to_children(line)))
    parent_node = PN.ParentNode("ol",html_nodes)
    return parent_node

def paragraph_to_html(block):
    lines = [line.strip() for line in block.split("\n")]
    paragraph = " ".join(lines).strip()
    html_node = text_to_children(paragraph)
    
    parent_node = PN.ParentNode("p",html_node)
    return parent_node
    
def text_to_children(text):
    text_nodes = H.text_to_textnodes(text)
    html_nodes = []
    for node in text_nodes:
        html_node = T.text_node_to_html_node(node)
        html_nodes.append(html_node)
    return html_nodes