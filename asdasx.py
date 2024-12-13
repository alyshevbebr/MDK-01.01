from pynput import keyboard

def on_press(key):
    try:
        # Если нажата клавиша "+", разрешаем её
        if key.char == '+':
            print("Клавиша '+' нажата.")
            return  # Разрешаем выполнение
    except AttributeError:
        # Игнорируем специальные клавиши
        pass

    # Блокируем нажатие других клавиш
    print(f"Клавиша {key} заблокирована.")
    return False  # Блокируем остальные клавиши

# Запускаем слушатель клавиатуры
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

# Запускаем основной цикл
keyboard_listener.join()
