import re

# Path to the 'movie_lines.txt' file
MOVIE_LINES_FILE = './movie_lines.txt'
OUTPUT_FILE = 'processed_dialogues.txt'

# Function to clean text
def clean_text(text):
    text = re.sub(r'\s+([,.!?;:])', r'\1', text)  # Remove spaces before punctuation
    text = re.sub(r'([,.!?;:])([^\s])', r'\1 \2', text)  # Ensure space after punctuation
    text = re.sub(r'\s{2,}', ' ', text)  # Replace multiple spaces with a single space
    return text.strip()

# Process the movie lines
with open(MOVIE_LINES_FILE, 'r', encoding='utf-8', errors='ignore') as file:
    lines = file.readlines()

cleaned_dialogues = []
for line in lines:
    parts = line.split(' +++$+++ ')
    if len(parts) == 5:
        dialogue_text = parts[4].strip()
        cleaned_text = clean_text(dialogue_text)
        if cleaned_text:
            cleaned_dialogues.append(cleaned_text)

# Save the cleaned dialogues to the output file
with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
    for dialogue in cleaned_dialogues:
        file.write(dialogue + '\n')

print(f"Processed {len(cleaned_dialogues)} dialogues. Output saved to {OUTPUT_FILE}.")
