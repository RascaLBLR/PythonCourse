weight = int(input("Введите ваш вес(кг.):"))
height = int(input("Введите ваш рост(см.):"))
gender = input("Введите ваш пол М/Ж:")
age = int(input("Введите ваш возраст(кол-во. полных лет):"))

bmi = weight / (height / 100) ** 2

print(
    "Ваш индекс массы тела:" , round(bmi , 2) ,
    "\n20" + "=" * (int(bmi) - 20) + "|" + "=" * 
    (50 - int(bmi)) + "50"
)

if gender == "м" or gender == "М":
    if bmi < 20:
        description = "Вам бы покушать!"
    elif bmi >= 20 and bmi < 25:
        description = "Продолжать в том же духе!"
    elif bmi >= 25 and bmi < 30:
        description = "Пузо все ближе!"
    elif bmi >= 30 and bmi < 40:
        description = "Пора переходить на зеленые салатики!"
    else:
        description = "Вы приближаетесь к критической точке!"
    print("В вашем", age, "- летнем возрасте, пора подумать о том, что:", description)    
elif gender == "ж" or gender == "Ж":
    if bmi < 20:
        description = "Скоро совсем сдуетесь!"
    elif bmi >= 20 and bmi < 25:
        description = "Все хорошо, кушайте дальше!"
    elif bmi >= 25 and bmi < 30:
        description = "А бока вы не плохо набили!"
    elif bmi >= 30 and bmi < 40:
        description = "Пора бы почитать о модной диете!"
    else:
        description = "Скоро лопните!"
    print("В вашем", age, "- летнем возрасте, пора подумать о том, что:", description)    
else:
    print("Что ты такое?")
