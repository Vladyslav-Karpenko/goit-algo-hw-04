import sys
from pathlib import Path
from colorama import Fore, Back, Style
#!!! Третє завдання (не обов'язкове)
# Вимоги до завдання:
# Створіть віртуальне оточення Python для ізоляції залежностей проєкту.
# Скрипт має отримувати шлях до директорії як аргумент при запуску. Цей шлях вказує, де знаходиться директорія, структуру якої потрібно відобразити.
# Використання бібліотеки colorama для реалізації кольорового виведення.
# Скрипт має коректно відображати як імена директорій, так і імена файлів, використовуючи рекурсивний спосіб обходу директорій
# (можна, за бажанням, використати не рекурсивний спосіб).
# Повинна бути перевірка та обробка помилок, наприклад, якщо вказаний шлях не існує або він не веде до директорії.


def show_tree(path: Path, level=0):
    indent = '    ' * level
    try:
        items = list(path.iterdir())
        dirs = [p for p in items if p.is_dir()]
        files = [p for p in items if p.is_file()]
        for d in sorted(dirs):
            print(f'{Fore.GREEN}{indent}{d.name}/{Style.RESET_ALL}')
            show_tree(d, level + 1)
        for f in sorted(files):
            print(f'{Fore.BLUE}{indent}{f.name}{Style.RESET_ALL}')
    except (FileNotFoundError, PermissionError) as e:
        print(
            f'Incorrect file path or no access: {Fore.YELLOW}ERROR{Style.RESET_ALL} {e}')


if len(sys.argv) < 2:
    print('You need to give me a path to the directory after running the python file, try again please ')
    sys.exit()

user_path = Path(sys.argv[1])


if not user_path.exists() or not user_path.is_dir():
    print('Sorry, but it is not a directory =)')
    sys.exit()

show_tree(user_path)
