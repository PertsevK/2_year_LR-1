import math  # Бібліотека math

def Integer14():
    """Дано тризначне число. У ньому закреслили першу праворуч цифру і приписали її зліва. Вивести отримане число."""
    try: # Перевірка на помилки
        Number = int(input("Enter three digit number -> ")) # Введення числа
    except ValueError: # Якщо помилка
        print("Ansver: Number must be integer") # Сповіщення про помилку
    else:
        if Number > 99 and Number < 1000:
            n2 = (Number - Number % 10) / 10+Number % 10 * 100;
            print("Answer: ", int(n2))
        else: print("Answer: Number must be three digits")
        
def Task2():
    """Function y"""
    try: # Перевірка на помилки
        x = float(input("Enter x -> ")) # Введення числа х
        y1 = (15*pow(3, x)*pow(math.exp(2*x)*abs(3*math.sin(42+x)), 0.5))
        y2 = math.log(4*abs(x), 3)
        print("Answer: y = ", y1/y2)
    except ValueError: # Якщо помилка
        print("Answer: x must be float") # Сповіщення про помилку
        
def Boolean14():
    """Дано три цілих числа: A, B, C. Перевірити істинність висловлювання: «Рівне одне з чисел A, B, C позитивне»"""
    try: # Перевірка на помилки
        print("Condition: one of the numbers is positive")
        A = int(input("Enter number A -> ")) # Введення числа А
        B = int(input("Enter number B -> ")) # Введення числа В
        C = int(input("Enter number C -> ")) # Введення числа С
    except ValueError: # Якщо помилка
        print("Answer: All numbers must be integer") # Сповіщення про помилку
    else:
        if A>0 and B<=0 and C<=0 or B>0 and A<=0 and C<=0 or C>0 and B<=0 and A<=0: # Перевірка умови
            print("Answer: Only one of the numbers is positive")
        else:
            print("Answer: Contradicts the condition")
 

Num = 0
while Num != 4: # Меню
    print("     MENU")
    print("1 - Integer14")
    print("2 - Task2")
    print("3 - Boolean14")
    print("4 - Exit")
    Num = int(input("Select task number -> "))
    if Num == 1: 
        Integer14() # Функція Integer14
    elif Num == 2: 
        Task2()  # Функція Task2
    elif Num == 3: 
        Boolean14()  # Функція Boolean14
    elif Num == 4: 
        print("Exit...")  # Вихід
    else: 
        print("Enter true task number")
