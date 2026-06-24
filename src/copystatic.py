import os
import shutil

def copy_static(source: str, destination: str, first_call: bool = True):
    directory_items = os.listdir(source)
    for item in directory_items:
        src_path = os.path.join(source,item)
        if os.path.isfile(src_path):
            shutil.copy(src_path,destination)
        else:
            dir_path = os.path.join(destination,item)
            os.mkdir(dir_path)
            copy_static(src_path,dir_path)

def clean_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)