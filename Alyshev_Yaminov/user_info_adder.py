from main_menu import*
from keybebra import keyboard
import json
def beta():
    while True:
        beta = input("Вы хотите пройти полную регистрацию - ДА(R) / Нет (A)")
        if beta == "A":
            main_menu()
        elif beta == "R":
            info()

def info():
    print('\n Укажите дату рождения, почту, номер телефона')
    Birthd_input = input('Укажите дату рождения: ')
    email_input = input("Укажите почту: ")
    numb_input = input("Укажите номер телефона: ")
    user["Birthday"] = Birthd_input
    user["email"] = email_input
    user["number"] = numb_input
    data["users"].append(user)
    with open('user_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print("Информация успешно обновлена")
    if keyboard.wait('Enter'):
        print('Enter нажат!')
        main_menu()