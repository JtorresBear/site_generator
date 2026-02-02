from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE =  "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list "



def block_to_block_type(block):
    if re.match(r'^#{1,6} ', block):
        return BlockType.HEADING
    if re.search(r'^```[\s\S]*```\s*$', block):
        return BlockType.CODE
    if re.match(r'^>',block):
        return BlockType.QUOTE
    if re.match(r'^- ',block):
        if is_unordered(block):
            return BlockType.UNORDERED_LIST
    if re.match(r'^\d. ',block):
        if is_in_order(block):
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def is_in_order(text):
    
    lines = text.split("\n")
    for i,line in enumerate(lines):
        expected_val = i + 1
        if not line.startswith(f'{expected_val}'):
            return False
    
    return True

def is_unordered(text):
    lines = text.split("\n")
    for line in lines:
        if not line.startswith(f'- '):
            return False
    return True

def markdown_to_blocks(markdown):
    temp_list_of_blocks = markdown.split("\n\n")
    list_of_blocks = []
    for block in temp_list_of_blocks:
        new_block = block.strip()
        if new_block != "":
            list_of_blocks.append(new_block)
    return list_of_blocks