import math  # Бібліотека math

def Integer14(): # Дано тризначне число. У ньому закреслили першу праворуч цифру і приписали її зліва. Вивести отримане число.
    "Three digit number conversion"
    try: # Перевірка на помилки
        Number = input("Enter three digit number -> ") # Введення числа
        lenth = len(Number)
        int(Number)
        if lenth == 3:
            print("Answer: ", Number[2]+Number[1])
        else: print("Answer: Number must be three digits")
    except: # Якщо помилка
        print("Ansver: Number must be integer") # Сповіщення про помилку
        
def Task2():
    "Function y"
    try: # Перевірка на помилки
        x = float(input("Enter x -> ")) # Введення числа х
        y = (15*pow(3, x)*pow(math.exp(2*x)*abs(3*math.sin(42+x)), 0.5))/math.log(4*abs(x), 3)
        print("Answer: y = ", y)
    except: # Якщо помилка
        print("Answer: x must be float") # Сповіщення про помилку
        
def Boolean14(): # Дано три цілих числа: A, B, C. Перевірити істинність висловлювання: «Рівне одне з чисел A, B, C позитивне».
    "Only one of these numbers is positive"
    try: # Перевірка на помилки
        print("Condition: one of the numbers is positive")
        A = int(input("Enter number A -> ")) # Введення числа А
        B = int(input("Enter number B -> ")) # Введення числа В
        C = int(input("Enter number C -> ")) # Введення числа С
        if A>0 and B<=0 and C<=0 or B>0 and A<=0 and C<=0 or C>0 and B<=0 and A<=0: # Перевірка умови
            print("Answer: One of the numbers is positive")
        else:
            print("Answer: Contradicts the condition")
    except: # Якщо помилка
        print("Answer: All numbers must be integer") # Сповіщення про помилку

Num = 0
while Num != 4: # Меню
    print("     MENU")
    print("1 - Integer14")
    print("2 - Task2")
    print("3 - Boolean14")
    print("4 - Exit")
    Num = int(input("Select task number -> "))
    if Num == 1: Integer14() # Функція Integer14
    elif Num == 2: Task2()  # Функція Task2
    elif Num == 3: Boolean14()  # Функція Boolean14
    elif Num == 4: print("Exit...")  # Вихід
    else: print("Enter true task number")
