def input_X():
    return

def input_N():
    return

def find_first_cif():
    return

def find_nn_cif():
    return

while True:
    print("1. Ввести целое трехзначное число X")
    print("2. Ввести цифру N (которая меньше числа разрядов числа X)")
    print("3. Найти первую цифру числа X")
    print("4. Найти N-ю цифру числа X (цифры нумеруются справа налево)")
    print("0. Выход")
    print()
    
    a = input("Введите номер выбранного действия: ")
    if a == "1":
        input_X()
    elif a == "2":
        input_N()
    elif a == "3":
        find_first_cif()
    elif a == "4":
        find_nn_cif()
    elif a == "0":
        print("Программа завершена. До свидания!")
        break
    else:
        print("Вы ввели неправильный вариант ответа!")

