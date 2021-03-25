num = input("Введите число\n")
operator = 0
while True:
    operator = input()
    if num.isdigit() is True:
        if operator.find('+') == 0:
            res = int(num) + int(operator[1])
        elif operator.find('-') == 0:
            res = int(num) - int(operator[1])
        elif operator.find('*') == 0:
            res = int(num) * int(operator[1])
        elif operator.find('**') == 1:
            res = int(num) ** int(operator[1])
        elif operator.find('%') == 0:
            if int(operator[1]) != 0:
                res = int(num) % int(operator[1])
            else:
                print("Деление на ноль!")
        elif operator.find('/') == 0:
            if int(operator[1]) != 0:
                res = int(num) / int(operator[1])
            else:
                print("Деление на ноль!")
        elif operator.find('=') == 0:
            print(res)
            break

        else:
            print("Неверный знак операции!")