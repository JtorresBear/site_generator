import unittest

from parent_node import ParentNode
from leaf_node import LeafNode

class TestParentNode(unittest.TestCase):

  def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

  def test_to_html_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )
  def test_to_html_no_children(self):
    
    with self.assertRaises(ValueError):
      parent_node = ParentNode("p",[])
      parent_node.to_html()

  def test_to_html_no_tag(self):
    print("running")
    with self.assertRaises(ValueError):
      child_node = LeafNode("span","child")
      parent_node = ParentNode(None,[child_node])
      parent_node.to_html()