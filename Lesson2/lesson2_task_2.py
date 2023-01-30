def is_year_leap(): 
    is_year_leap = input("Введите год ")
    year = int(is_year_leap)
    if year % 4 ==0:
        print("Год ", year,": True Високосный") 
    else:
        print("Год ", year,": False Обычный")


is_year_leap()