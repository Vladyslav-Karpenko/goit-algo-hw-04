from pprint import pprint
from pathlib import Path

# !!! Друге завдання
# Вимоги до завдання:
# Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).
# Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
# Функція має повертати список словників, де кожен словник містить інформацію про одного кота.

cats_file = Path('files/cats_file.txt')


def get_cats_info(path: Path) -> list[dict]:
    result = []
    try:
        with path.open('r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    try:
                        cat_id, name, age = parts
                        result.append(
                            {'id': cat_id, 'name': name, 'age': int(age)})
                    except ValueError:
                        continue
        return result
    except FileNotFoundError as e:
        print(f'Path {path} is INCORRECT! Error {e}')
        return []


pprint(get_cats_info(cats_file))
