def month_to_season():
    x = input("Введите номер месяца ")
    num = int(x)
    if num >12 or num <1:
        print("Вы ввели неправильные данные. Попробуйте еще раз")
    elif num >2 and num <6:
        print(num, "-  Весна")
    elif num >5 and num <9:
        print(num, "- Лето")
    elif num >8 and num <12:
        print(num, "- Осень")
    elif num >1 and num <3:
        print(num, "- Зима")
    elif num == 12:
        print(num, "- Зима")


month_to_season()