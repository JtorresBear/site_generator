import unittest

import markdown_to_textnodes_to_html as M

class TestMarkdownBlocks(unittest.TestCase):
    
    def test_paragraphs(self):
        md = """
        This is **bolded** paragraph
        text in a p
        tag here

        This is another paragraph with _italic_ text and `code` here

        """

        node = M.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
            )
    
    def test_codeblock(self):
        md = """
        ```
        This is text that _should_ remain
        the **same** even with inline stuff
        ```
        """

        node = M.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
            )
        
    def test_quoteblock(self):
        md = """
> this is a QUOTE
> this is a quote with **bold** and _italic_
> and just random. 
"""
        node = M.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>this is a QUOTE this is a quote with <b>bold</b> and <i>italic</i> and just random.</blockquote></div>"
        )

    def test_unordered_list(self):
        md = """
- something
- something else
- this can be a third unordered thing
"""
        node = M.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>something</li><li>something else</li><li>this can be a third unordered thing</li></ul></div>"
        )
    
    def test_ordered_list(self):
        md = """
1. something
2. something
3. this can 
4. something
5. something
6. this can 
7. something
8. something
9. this can 
10. something
11. something
12. something el
13. this can be
"""
        node = M.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>something</li><li>something</li><li>this can</li><li>something</li><li>something</li><li>this can</li><li>something</li><li>something</li><li>this can</li><li>something</li><li>something</li><li>something el</li><li>this can be</li></ol></div>"
        )

    def test_heading1(self):
        md = """
# this is the title
"""
        node = M.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is the title</h1></div>"
        )
    def test_heading2(self):
        md = """
## this is the title
"""
        node = M.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>this is the title</h2></div>"
        )
    def test_heading3(self):
        md = """
### this is the title
"""
        node = M.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>this is the title</h3></div>"
        )
    def test_heading4(self):
        md = """
#### this is the title
"""
        node = M.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h4>this is the title</h4></div>"
        )
    def test_heading5(self):
        md = """
##### this is the title
"""
        node = M.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h5>this is the title</h5></div>"
        )
    def test_heading6(self):
        md = """
###### this is the title
"""
        node = M.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h6>this is the title</h6></div>"
        )