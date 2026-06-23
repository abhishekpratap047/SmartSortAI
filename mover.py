import os
import shutil

BASE_DIR = "organized"

def move_file(filepath, category):

    category_folder = os.path.join(
        BASE_DIR,
        category
    )

    os.makedirs(
        category_folder,
        exist_ok=True
    )

    filename = os.path.basename(filepath)

    destination = os.path.join(
        category_folder,
        filename
    )

    shutil.move(
        filepath,
        destination
    )

    return destination