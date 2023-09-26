import math  # Бібліотека math


def Integer14(): 
  """Дано тризначне число. У ньому закреслили першу праворуч цифру і 
  приписали її зліва. Вивести отримане число."""
    # "Three digit number conversion"
  try: # Перевірка на помилки
      number = int(input("Enter three digit number -> ")) # Введення числа
  except ValueError: # Якщо помилка
      print("Ansver: Number must be integer") # Сповіщення про помилку
  else:
      # Додайте перевірку на тризначність числа (більше 99, менше 1000)

      # Після цього ви повинні працювати з числом як цілочисельним типом
      # Для цього просто виделіть окремі цифри за допомогою цілочисельного 
      # ділення та взття остатку. Наприклад, ви можете отримати другу 
      # цифру як n2 = number // 10 % 10

      # Фінальне тризначне число ви можете отримати як суму добутку прешої 
      # цифри на 100, другої на 10 та третьої на 1
      pass


def Task2():
    """Function y"""
    try: # Перевірка на помилки
        x = float(input("Enter x -> ")) # Введення числа х
        # Як рекомендація, то можно відокремити чисельник та знаменик у 
        # окремі змінні. Так легше перевіряти правильнисть написання 
        # кожної частини
        y = (15*pow(3, x)*pow(math.exp(2*x)*abs(3*math.sin(42+x)), 0.5))/math.log(4*abs(x), 3)
    except ValueError: # Якщо помилка
        print("Answer: x must be float") # Сповіщення про помилку
    else:
        print("Answer: y = ", y)


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
