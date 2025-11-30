import os
from datetime import datetime

# Input validation
def validate_input(topic, no_of_words):
    if not topic.strip():
        return False, "Blog topic cannot be empty."
    try:
        words = int(no_of_words)
        if words <= 0:
            return False, "Number of words must be a positive integer."
    except ValueError:
        return False, "Number of words must be an integer."
    return True, ""


# Clean model output
def clean_text(text):
    return text.strip()


# Save blog to file
def save_blog_to_file(blog_text, output_dir="generated_blogs", filename=None):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"blog_{timestamp}.txt"
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(blog_text)
    return filepath
