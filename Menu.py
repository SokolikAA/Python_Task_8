import config as cn


def main_menu():
    print('=====================================\n'
          '|          Телефонная книга         |\n'
          '=====================================\n'
          '|            Главное меню           |\n'
          '=====================================\n'
          '1: Открыть файл\n'
          '2: Сохранить файл\n'
          '3: Показать контакты\n'
          '4: Добавить контакт\n'
          '5: Изменить контакт\n'
          '6: Найти контакт\n'
          '7: Удалить контакт\n'
          '8: Выход\n')
    data = int(input('Введите номер меню: '))
    return data


guide = []

while True:
    user_choice = main_menu()
    match user_choice:
        case 1:
            guide = cn.open_phone_book()
        case 2:
            cn.save_phone_book(guide)
        case 3:
            cn.show_phone_book(guide)
        case 4:
            cn.add_phone_book(guide)
        case 5:
            cn.change_phone_book(guide)
        case 6:
            cn.find_phone_book(guide)
        case 7:
            cn.delete_phone_book(guide)
        case 8:
            break
