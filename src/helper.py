from textnode import TextType
from textnode import TextNode
from enum import Enum
import re 

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE =  "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list "


def split_nodes_delimiter(old_nodes,delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_string = node.text.split(delimiter)
        if len(split_string) % 2 == 0:
            raise Exception("That's invalid Markdown syntax")
        else:
            for i,str in enumerate(split_string):
                if i % 2 == 0:
                    new_nodes.append(TextNode(str,TextType.TEXT))
                else:
                    new_nodes.append(TextNode(str,text_type))
        #print(split_string,"length:", len(split_string) )
    return new_nodes 

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return matches

def split_nodes_link(old_nodes): 
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        text_copy = node.text
        if not links:
            new_nodes.append(node)
            continue
        for link in links:
            txt,url = link
            the_split = text_copy.split(f"[{txt}]({url})",1)
            if the_split[0] != "":
                new_nodes.append(TextNode(the_split[0],TextType.TEXT))
            new_nodes.append(TextNode(txt,TextType.LINK,url))
            
            text_copy = the_split[1]
        if text_copy != "":
            new_nodes.append(TextNode(text_copy,TextType.TEXT))
    return new_nodes

def split_nodes_image(old_nodes):
    #create nodes list to return
    new_nodes = []
    #loop through the old nodes
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        #store image links in a list from the node
        images = extract_markdown_images(node.text)
        text_copy = node.text
        #if the list is empty add the full node to the new nodes return list and continue
        if not images:
            #create node to return
            new_nodes.append(node)
            continue
        for image in images:
            txt,url = image
            the_split = text_copy.split(f"![{txt}]({url})",1)
            if the_split[0] != "":
                new_nodes.append(TextNode(the_split[0],TextType.TEXT))
            new_nodes.append(TextNode(txt,TextType.IMAGE,url))
            text_copy = the_split[1]
        if text_copy != "":
            new_nodes.append(TextNode(text_copy,TextType.TEXT))
            
    #loop through the list to separate image links and text nodes and add those to the return list
    
    return new_nodes

def text_to_textnodes(text):
    nodes_list = [TextNode(text,TextType.TEXT)]
    nodes_list = split_nodes_delimiter(nodes_list,"`",TextType.CODE)
    nodes_list = split_nodes_delimiter(nodes_list,"**",TextType.BOLD)
    nodes_list = split_nodes_delimiter(nodes_list,"_",TextType.ITALIC)
    nodes_list = split_nodes_link(nodes_list)
    nodes_list = split_nodes_image(nodes_list)
    
    return nodes_list

"""
take the markdown text, turn them into text nodes, turn the text nodes into html nodes
"""