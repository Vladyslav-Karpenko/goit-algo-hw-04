from pathlib import Path

# !!! Перше завдання
# Вимоги до завдання:
# Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).
# Файл містить дані про заробітні плати розробників, розділені комами. Кожен рядок вказує на одного розробника.
# Функція повинна аналізувати файл, обчислювати загальну та середню суму заробітної плати.
# Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати.


def total_salary(salary_path: Path) -> tuple[int, int]:
    salaries = []
    try:
        with salary_path.open('r', encoding='utf-8') as file:
            for line in file:
                _, salary = line.strip().split(',')
                salaries.append(int(salary))
        if not salaries:
            return (0, 0)
        total = sum(salaries)
        average = total // len(salaries)
        return (total, average)
    except FileNotFoundError as e:
        print(f"{salary_path} not found ERROR {e}")
        return (0, 0)


salary_file = Path('files/salary_file.txt')


total, average = total_salary(salary_file)

print(
    f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
