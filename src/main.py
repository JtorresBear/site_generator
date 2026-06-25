from textnode import TextNode,TextType
from parent_node import ParentNode
from leaf_node import LeafNode
import copystatic as copy
import gencontent as gc
import sys


def main():
    nsrc = sys.argv[0]
    print(nsrc)
    copy.clean_dir("public")
    copy.copy_static("static","public")
    #gc.generate_page("content/index.md","template.html","public/index.html")
    #gc.generate_pages_recursive("content","template.html","public")


main()