number1 = int(input("Введите первое число:"))
number2 = int(input("Введите второе число:"))
number3 = int(input("Введите третье число:"))

number1 and number2 and number3 and print("Нет нулевых значений!!!")
print(number1 or number2 or number3 or "Введены все нули!")


if number1 > number2 + number3:
    print(number1 - number2 - number3)

if number1 < number2 + number3:
    print(number2 + number3 - number1)

if number1 > 50 and (number2 > number1 or number3 > number1):
    print("Вася")

if number1 > 5 or number2 == 7 and number3 == 7:
    print("Петя")
