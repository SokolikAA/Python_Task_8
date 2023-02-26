
def open_phone_book():
    with open('phone_book.txt', 'r', encoding='utf-8') as data:
        data = data.readlines()
        print('Файл открыт, данные скопированы.')
        return data


def save_phone_book(file):
    with open('phone_book.txt', 'w', encoding='utf-8') as data:
        data.writelines(file)


def show_phone_book(file):
    if len(file) == 0:
        print("Файл не открыт или он пустой.")
    else:
        for i in file:
            print(' '.join(i.split(';')))


def add_phone_book(file):
    if len(file) == 0:
        print("Файл не открыт или он пустой.")
    else:
        for i in file:
            user_data = input('Введите через пробел номер телефона, имя и примечание: ')
            user_data = '; '.join(user_data.split(' '))
            file.append(user_data + '\n')
            return file


def change_phone_book(file):
    user_data = input('Введите данные которые хотите заменить: ')
    for i in range(len(file)):
        if user_data in file[i]:
            print(file[i])
            new_user_data = input('Введите новые данные на которые хотите заменить: ')
            file[i] = file[i].replace(user_data, new_user_data)


def find_phone_book(file):
    user_data = input('Введите данные которые хотите найти: ')
    for i in range(len(file)):
        if user_data in file[i]:
            print(file[i])


def delete_phone_book(file):
    user_data = input('Введите данные которые хотите удалить: ')
    for i in range(len(file)):
        if user_data in file[i]:
            print(file[i])
            question = input('Точно хотите удалить контакт? для подтверждения нажмите - "y": ')
            if question == "y":
                file.pop(i)
                break



