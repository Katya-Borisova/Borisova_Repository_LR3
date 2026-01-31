def input_X():
    try:
        X = int(input("Введите трехзначное число X: "))
        if 100 <= abs(X) <= 999:
            print(f"Число {X} успешно сохранено")
            return X
        else:
            print("Ошибка! Число должно быть трехзначным (от 100 до 999 или от -999 до -100)")
            return None
    except:
        print("Ошибка! Введите целое число")
        return None    

def input_N():
    while True:
        try:
            N = int(input("Введите цифру N (1 или 2 т.к. должно быть меньше числа разрядов X): "))
            if 1 <= N <= 2:
                print(f"Цифра N = {N} успешно сохранена!")
                return N  
            else:
                print("Ошибка! N должно быть 1 или 2")
        except:
            print("Ошибка! Введите число 1 или 2")

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
        X = input_X()
    elif a == "2":
        N = input_N()
    elif a == "3":
        find_first_cif()
    elif a == "4":
        find_nn_cif()
    elif a == "0":
        print("Программа завершена. До свидания!")
        break
    else:
        print("Вы ввели неправильный вариант ответа!")

