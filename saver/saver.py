import os


def save_to_file(valid_links: list, invalid_links: list):
    directory = os.path.dirname(os.path.abspath(__file__))

    valid_file_path = os.path.join(directory, "..", "src", "valid.txt")
    invalid_file_path = os.path.join(directory, "..", "src", "broken.txt")

    with open(valid_file_path, "w", encoding="utf-8") as valid_file:
        valid_file.write("\n".join(valid_links))

    with open(invalid_file_path, "w", encoding="utf-8") as invalid_file:
        invalid_file.write("\n".join(invalid_links))
