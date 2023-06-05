def save_to_file(valid_links: list, invalid_links: list):
    with open("valid_links.txt", "w", encoding="utf-8") as valid_file:
        valid_file.write("\n".join(valid_links))

    with open("broken_links.txt", "w", encoding="utf-8") as invalid_file:
        invalid_file.write("\n".join(invalid_links))
    print("Лінки успішно провалідовані")