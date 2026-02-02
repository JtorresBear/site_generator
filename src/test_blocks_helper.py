import unittest
import blocks_helper

test_for_ordered = """1. do things
2. do other things
3. do more things"""


test_for_code = """
```
this is a code block
    code here
    more code
```
"""

test_for_paragraph = """
random paragraph. doesn't even have to be long cuz this is a whatever case
"""

test_for_full_markdown = """
# this is the title

## this is the title

### this is the title

#### this is the title

##### this is the title

###### this is the title

########### this is the title

1. do things
2. do other things
3. do more things

```
this is a code block
it will do this and that 
         and this and that 
         
         and that and this 
```

this is a random paragraph. it will have a new line. 
but we don't care about new lines just multi empty lines









- this is a list
- lists have this and that
- also all we need is perfectly written strings.
"""

class TestBlocksHelper(unittest.TestCase):

    def test_heading(self):
        test_for_Heading = "# this is the title"
        test_for_Heading2 = "##### this is the title"
        test_for_Headingfail = "######## this is the title"

        result = blocks_helper.block_to_block_type(test_for_Heading)
        result2 = blocks_helper.block_to_block_type(test_for_Heading2)
        resultfail = blocks_helper.block_to_block_type(test_for_Headingfail)
        self.assertEqual(result,blocks_helper.BlockType.HEADING)
        self.assertEqual(result2,blocks_helper.BlockType.HEADING)
        self.assertEqual(resultfail,blocks_helper.BlockType.PARAGRAPH)

    def test_ordered_list(self):
        
        test_for_ordered_list_fail = """1. do things\n2. do other things\n4. do more things"""
        result = blocks_helper.block_to_block_type(test_for_ordered)
        result2 = blocks_helper.block_to_block_type(test_for_ordered_list_fail)

        self.assertEqual(result,blocks_helper.BlockType.ORDERED_LIST)
        self.assertEqual(result2,blocks_helper.BlockType.PARAGRAPH)

    def test_unordered_list(self):
        test_unordered = "- first line\n- second line\n- third line"
        result = blocks_helper.block_to_block_type(test_unordered)

        self.assertEqual(result, blocks_helper.BlockType.UNORDERED_LIST)

    def test_quotes(self):
        test_for_quote = ">this is a quote with text. \n it just needs to tos tart with the greater than sign"

        result = blocks_helper.block_to_block_type(test_for_quote)
        self.assertEqual(result, blocks_helper.BlockType.QUOTE)
    
    def test_code(self):
        test_for_code = """```
        this is a code block
        code here
        more code
        ```"""
        result = blocks_helper.markdown_to_blocks(test_for_code)
        result = blocks_helper.block_to_block_type(result[0])
        self.assertEqual(result,blocks_helper.BlockType.CODE)