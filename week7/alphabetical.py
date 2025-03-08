import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w", encoding="utf-8") as file:
        file.write(f"Файл {letter}.txt создан успешно.")