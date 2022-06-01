weight = int(input("Введите ваш вес(кг.):"))
height = int(input("Введите ваш рост(см.):"))

bmi = weight / (height / 100) ** 2

print(
    "Ваш индекс массы тела:" , round(bmi , 2) ,
    "\n20" + "=" * (int(bmi) - 20) + "|" + "=" * 
    (50 - int(bmi)) + "50"
)

#variables solution
#l_equals = int(bmi - 20)
#r_equals = int(50 - bmi)
#print(
#"Ваш индекс массы тела:" , round(bmi , 2) ,
    #"\n20" + "=" * l_equals + "|" + "=" * r_equals + "50"
#)
