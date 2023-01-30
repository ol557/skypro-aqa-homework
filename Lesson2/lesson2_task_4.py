def fizz_buzz():
    n_x = input("Введите число ")
    n = int(n_x)
    for p in range(1, n):
        
        if p % 3 == 0:
            print("Fizz")
        elif p % 5 == 0:
            print("Buzz")
        elif (p % 3 == 0) and (p % 5 == 0):
            print("FizzBuzz")
        else:
            print(p)
   
   

fizz_buzz()

