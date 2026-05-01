from pathlib import Path

# !!! Перше завдання
# Вимоги до завдання:
# Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).
# Файл містить дані про заробітні плати розробників, розділені комами. Кожен рядок вказує на одного розробника.
# Функція повинна аналізувати файл, обчислювати загальну та середню суму заробітної плати.
# Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати.


# 1 завдання. Загалом правильно. Тільки не треба було переводити зарплату в int.
# Якщо явно не сказано, що будуть цілі числа, то краще використати float.
# Будьте обережні з перетворенням типів - це завжи місце для потенційної помилки.
# Також було сказано, що середню зарплату треба було порахувати точно, тому ділення націло тут недоречно.


def total_salary(salary_path: Path) -> tuple[float, float]:

    try:
        with salary_path.open('r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                if not line.strip():
                    continue
                parts = line.strip().split(',')
                if len(parts) != 2:
                    continue
                try:
                    salaries.append(float(parts[1]))
                except ValueError:
                    continue
        if not salaries:
            return (0.0, 0.0)
        total = sum(salaries)
        average = total / len(salaries)
        return (total, average)
    except FileNotFoundError as e:
        print(f"{salary_path} not found ERROR {e}")
        return (0.0, 0.0)


salary_file = Path('files/salary_file.txt')


total, average = total_salary(salary_file)

print(
    f"Загальна сума заробітної плати: {total:.2f}, Середня заробітна плата: {average:.2f}")
