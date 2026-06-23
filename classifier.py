import ollama

MODEL_NAME = "gemma3:4b"


def classify_file(filename, content):

    prompt = f"""
You are a file classification system.

Available Categories:

Research
College
Job Applications
Bills
Code
Images
Audio
Videos
Personal
Other

Filename:
{filename}

Content Preview:
{content[:1500]}

Respond with ONLY ONE category.

No explanation.
No punctuation.
No markdown.
"""

    try:

        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        category = response["message"]["content"].strip()

        return category

    except Exception as e:

        print("Classification Error:", e)

        return "Other"