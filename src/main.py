from textnode import TextNode,TextType
from parent_node import ParentNode
from leaf_node import LeafNode
import copystatic as copy
import gencontent as gc
import sys


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    copy.clean_dir("docs")
    copy.copy_static("static","docs")
    gc.generate_pages_recursive("content","template.html","docs",basepath)


main()