import sys
# !!! Четверте завдання
# Вимоги до завдання:
# Програма повинна мати функцію main(), яка управляє основним циклом обробки команд.
# Реалізуйте функцію parse_input(), яка розбиратиме введений користувачем рядок на команду та її аргументи.
# Команди та аргументи мають бути розпізнані незалежно від регістру введення.
# Ваша програма повинна очікувати на введення команд користувачем та обробляти їх за допомогою відповідних функцій.
# В разі введення команди "exit" або "close", програма повинна завершувати виконання.
# Напишіть функції-обробники для різних команд, наприклад add_contact(), change_contact(), show_phone() тощо.
# Використовуйте словник Python для зберігання імен і номерів телефонів. Ім'я буде ключем, а номер телефону – значенням.
# Ваша програма має вміти ідентифікувати та повідомляти про неправильно введені команди.

phones = {
    'Vladyslav': '560200'
}


def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args: list, contacts: dict):
    name, phone = args
    contacts[name] = phone
    return 'contact added'


def change_contact(args: list, contacts: dict):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f'Contact {name} has been changed'
    else:
        return f'There is no {name} contact in phone book, try again'


def show_phone(args: list, phones: dict):
    name = args[0]
    if name in phones:
        phone = phones[args[0]]
        return f'The phone of user {name} is {phone}'
    else:
        return f'User {name} is not found'


def show_name(args: list, phones: dict):
    phone = args[0]
    for k, v in phones.items():
        if phone == v:
            return f'The phone number {phone} is owned by user {k}'
    return f'Phone {phone} is not found'


def show_all_contacts(phones):
    result = ''
    for name, phone in phones.items():
        result += f'Name: {name} - Phone: {phone}\n'
    return result


def main():
    print('Welcome to the assistant bot!')
    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)
        if command in ['exit', 'close', 'quit']:
            print('Bye bye!!!')
            break
        elif command in ['hi', 'hello']:
            print('How I can help you?')
        elif command == 'add':
            print(add_contact(args, phones))
        elif command == 'change':
            print(change_contact(args, phones))
        elif command == 'phone':
            print(show_phone(args, phones))
        elif command == 'show':
            print(show_name(args, phones))
        elif command == 'all':
            print(show_all_contacts(phones))
        else:
            print('Invalid command')


if __name__ == '__main__':
    main()
