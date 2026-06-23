import os

from extractor import extract_content
from classifier import classify_file
from renamer import (
    generate_filename,
    rename_file
)
from mover import move_file

from database import (
    initialize_db,
    save_history
)


def process_file(filepath):

    initialize_db()

    original_path = filepath

    print("\nExtracting content...")

    content = extract_content(filepath)

    print("Classifying file...")

    category = classify_file(
        os.path.basename(filepath),
        content
    )

    print(f"Category: {category}")

    print("Generating filename...")

    generated_name = generate_filename(
        os.path.basename(filepath),
        content
    )

    print(f"Generated Name: {generated_name}")

    print("Renaming file...")

    renamed_path = rename_file(
        filepath,
        generated_name
    )

    print("Moving file...")

    final_path = move_file(
        renamed_path,
        category
    )

    save_history(
        original_path,
        renamed_path,
        final_path
    )

    print(f"Done -> {final_path}")

    return final_path