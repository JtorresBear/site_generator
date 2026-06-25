import blocks_helper as BH
import markdown_to_textnodes_to_html as M_to_html
import htmlnode
import os
from pathlib import Path

def extract_title(markdown):
    blocks = BH.markdown_to_blocks(markdown)
    found = False
    h1 = ""
    for block in blocks:
        block_type = BH.block_to_block_type(block)
        if block_type == BH.BlockType.HEADING:
            if block.startswith("# "):
                h1 = block[1:].strip()
                return h1
    raise Exception("there is no title")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    m_file = open(from_path)
    m_text = m_file.read()
    m_file.close()
    template_file = open(template_path)
    template_text = template_file.read()
    template_file.close()

    m_html = M_to_html.markdown_to_html_node(m_text).to_html()
    m_title = extract_title(m_text)

    template_text = template_text.replace("{{ Title }}",m_title)
    template_text = template_text.replace("{{ Content }}", m_html)
    template_text = template_text.replace('href="/', 'href="' + basepath)
    template_text = template_text.replace('src="/', 'src="' + basepath)
    d_path = os.path.dirname(dest_path)
    os.makedirs(d_path,exist_ok=True)


    d_file = open(dest_path,"w")
    d_file.write(template_text)
    d_file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path,basepath):
    directory_items = os.listdir(dir_path_content)

    for item in directory_items:
        content_path = os.path.join(dir_path_content,item)
        if os.path.isfile(content_path):
            dest_path = os.path.join(dest_dir_path,item)
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(content_path,template_path,dest_path,basepath)
        else:
            dest_path = os.path.join(dest_dir_path,item)
            generate_pages_recursive(content_path,template_path,dest_path,basepath)
