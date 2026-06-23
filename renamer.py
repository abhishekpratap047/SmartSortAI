import ollama
import os

MODEL_NAME = "gemma3:4b"

def generate_filename(filename, content):

    prompt = f"""
Generate a clean and descriptive filename.

Rules:
- Use underscores instead of spaces
- No special characters
- Maximum 8 words
- Do not include file extension
- Return ONLY filename

Original filename:
{filename}

Content:
{content[:1000]}
"""

    try:

        response = ollama.generate(
            model=MODEL_NAME,
            prompt=prompt
        )

        new_name = response["response"].strip()
        new_name = (
    new_name
    .replace(" ", "_")
    .replace("/", "_")
    .replace("\\", "_")
    .replace(":", "_")
    .replace("*", "_")
    .replace("?", "_")
    .replace('"', "_")
    .replace("<", "_")
    .replace(">", "_")
    .replace("|", "_")
)

        return new_name

    except Exception as e:

        print("Rename Error:", e)

        return filename

def rename_file(filepath, generated_name):

    extension = os.path.splitext(filepath)[1]

    folder = os.path.dirname(filepath)

    new_path = os.path.join(
        folder,
        generated_name + extension
    )

    os.rename(filepath, new_path)

    return new_path