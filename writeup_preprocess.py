import os
import re
import easyocr

# Initialize the EasyOCR Reader
reader = easyocr.Reader(['en'])  # Supports English

def extract_text_from_images(image_paths):
    """Extract text from images using OCR."""
    image_texts = {}
    for image_path in image_paths:
        if not os.path.exists(image_path):
            print(f"Error: Image not found - {image_path}")
            image_texts[image_path] = "[Image not found]"
            continue
        
        try:
            print(f"Processing image: {image_path}")
            extracted_text = reader.readtext(image_path, detail=0)  # EasyOCR
            image_texts[image_path] = "\n".join(extracted_text).strip()
        except Exception as e:
            print(f"Error processing image {image_path}: {e}")
            image_texts[image_path] = "[Image processing failed]"
    return image_texts

def replace_image_references(writeup_text, image_texts):
    """
    Replace image references in the writeup text with extracted OCR content or placeholders.
    Assumes image references are in the format ![alt](path).
    """
    def replace_match(match):
        try:
            # Use the first capturing group for the image path
            image_path = match.group(1)
            return f"\n[Image extracted text: {image_texts.get(image_path, '[Image not found]')}]\n"
        except IndexError:
            print(f"Error: No such group in match {match}")
            return "[Error replacing image reference]"

    # image_pattern = r"!\[.*?\]\((.*?)\)"
    # Match both Markdown and HTML-style images
    image_pattern = r"!\[.*?\]\((.*?)\)|<img\s+[^>]*src=['\"]([^'\"]+)['\"]"
    matches = re.findall(image_pattern, writeup_text)
    print(f"Debug: Found matches - {matches}")
    updated_text = re.sub(image_pattern, replace_match, writeup_text)
    return updated_text

# def process_writeup_file(file_path, base_folder, processed_folder):
#     """Process a single writeup file and save the processed file into a centralized folder."""
#     try:
#         with open(file_path, "r", encoding="utf-8") as f:
#             writeup_text = f.read()

#         image_pattern = r"!\[.*?\]\((.*?)\)"
#         image_paths = re.findall(image_pattern, writeup_text)

#         folder_path = os.path.dirname(file_path)
#         full_image_paths = [os.path.join(folder_path, img) for img in image_paths]

#         extracted_texts = extract_text_from_images(full_image_paths)

#         # Map from full path back to relative path as it appears in the markdown
#         image_texts = {}
#         for rel_path, full_path in zip(image_paths, full_image_paths):
#             image_texts[rel_path] = extracted_texts.get(full_path, "[Image not found]")

#         processed_writeup = replace_image_references(writeup_text, image_texts)

#         # Derive year, competition, and challenge from file_path
#         # file_path structure: ./ctf-writeup/<year>/<competition>/<challenge>/writeup.md
#         rel_path = os.path.relpath(file_path, base_folder)
#         parts = rel_path.split(os.sep)
#         # parts should look like: [year, competition, challenge, writeup.md]
#         if len(parts) >= 4:
#             year = parts[0]
#             competition = parts[1]
#             challenge = parts[2]
#         else:
#             # If the structure differs, handle gracefully
#             year = "unknown_year"
#             competition = "unknown_competition"
#             challenge = os.path.splitext(parts[-1])[0]  # filename without extension

#         # Construct the output filename
#         output_filename = f"{year}_{competition}_{challenge}_processed.md"
#         output_path = os.path.join(processed_folder, output_filename)

#         # Ensure the processed folder exists
#         os.makedirs(processed_folder, exist_ok=True)

#         with open(output_path, "w", encoding="utf-8") as f:
#             f.write(processed_writeup)
#         print(f"Processed writeup saved to: {output_path}")

#     except Exception as e:
#         print(f"Error processing file {file_path}: {e}")

# def process_challenges_in_category(category_folder_path, base_folder, processed_folder):
#     """Process challenge folders within a category."""
#     for challenge_folder in os.listdir(category_folder_path):
#         challenge_path = os.path.join(category_folder_path, challenge_folder)
#         if os.path.isdir(challenge_path):
#             for file in os.listdir(challenge_path):
#                 if file.endswith(".md"):
#                     writeup_file = os.path.join(challenge_path, file)
#                     print(f"Processing writeup: {writeup_file}")
#                     process_writeup_file(writeup_file, base_folder, processed_folder)

# def process_all_year_folders(base_folder, processed_folder):
#     """Process all year folders and their nested category structure."""
#     for year_folder in sorted(os.listdir(base_folder)):
#         year_folder_path = os.path.join(base_folder, year_folder)
#         if os.path.isdir(year_folder_path):
#             print(f"Processing year folder: {year_folder}")
#             for category in os.listdir(year_folder_path):
#                 category_folder_path = os.path.join(year_folder_path, category)
#                 if os.path.isdir(category_folder_path):
#                     print(f"  Processing category folder: {category}")
#                     process_challenges_in_category(category_folder_path, base_folder, processed_folder)


def process_writeups(file_path):
    """Process a single writeup file and save the processed file into a centralized folder."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            writeup_text = f.read()

        # image_pattern = r"!\[.*?\]\((.*?)\)"
        # Match both Markdown and HTML-style images
        image_pattern = r"!\[.*?\]\((.*?)\)|<img\s+[^>]*src=['\"]([^'\"]+)['\"]"
        # image_paths = re.findall(image_pattern, writeup_text)
        matches = re.findall(image_pattern, writeup_text)

        # Extract both Markdown and HTML paths into a single list
        image_paths = [match[0] if match[0] else match[1] for match in matches]

        folder_path = os.path.dirname(file_path)
        # full_image_paths = [os.path.join(folder_path, img) for img in image_paths]
        full_image_paths = [
            os.path.abspath(img) if os.path.isabs(img) else os.path.join(folder_path, img)
            for img in image_paths
        ]


        extracted_texts = extract_text_from_images(full_image_paths)

        # Map from full path back to relative path as it appears in the markdown
        image_texts = {}
        for rel_path, full_path in zip(image_paths, full_image_paths):
            image_texts[rel_path] = extracted_texts.get(full_path, "[Image not found]")

        processed_writeup = replace_image_references(writeup_text, image_texts)

        return processed_writeup
    
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return ""

def process_file(base_folder, processed_folder):
    # Walk through the directory and process .md files
    for root, _, files in os.walk(base_folder):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)

                # # Read the content of the file
                # with open(file_path, 'r', encoding='utf-8') as f:
                #     content = f.read()

                # writeup_file = os.path.join(file_path, file)
                writeup_file = file_path
                print(f"Processing writeup: {writeup_file}")
                content = process_writeups(writeup_file)

                if content!="":

                    # Create filename based on folder structure
                    relative_path = os.path.relpath(file_path, base_folder)
                    new_filename = relative_path.replace(os.sep, '_')

                    # Save processed content in a new file
                    output_path = os.path.join(processed_folder, new_filename)
                    with open(output_path, 'w', encoding='utf-8') as f:
                        # Example processing (modify as needed)
                        f.write(content.lower())  # Example: Convert content to uppercase

                    print(f"Processed file saved as: {output_path}")
                
                else:
                    print(f"File not processed: {file_path}")

# Base folder containing year-wise subfolders with categories and challenges
base_folder = "./rishitsaiya_CTFlearn-Writeups"

# Folder to store all processed writeups
processed_folder = "./processed_rishitsaiya_CTFlearn-Writeups"

# Run the script
# process_all_year_folders(base_folder, processed_folder)
process_file(base_folder, processed_folder)