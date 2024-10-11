"""
 _____         _      __  
|_   _|       | |    /  | 
  | | __ _ ___| | __ `| | 
  | |/ _` / __| |/ /  | | 
  | | (_| \__ \   <  _| |_
  \_/\__,_|___/_|\_\ \___/

Напишите программу, которая выводит в консоль "Hello world"

hint: что такое print?
"""

print ("Hello world")

"""
 _____         _      _____ 
|_   _|       | |    / __  \
  | | __ _ ___| | __ `' / /'
  | |/ _` / __| |/ /   / /  
  | | (_| \__ \   <  ./ /___
  \_/\__,_|___/_|\_\ \_____/

Напишите рограмму, которая выводит числа от 1 до введенного пользователем. Для чисел, кратных 3, выводится "Fizz",'
для кратных 5 — "Buzz", а для чисел, кратных 3 и 5 — "FizzBuzz"

hint: цикл, если и "%"
"""

x = int(input("Введите число больше единицы"))+1
for i in range (1, x):
   if i % 3==0:
     print ("Fizz")
   elif i % 5==0:
     print ("Buzz")
   elif i % 3==0 and i % 5==0:
     print ("FizzBuzz")
   else:
    print (i)

"""
 _____         _      _____ 
|_   _|       | |    |____ |
  | | __ _ ___| | __     / /
  | |/ _` / __| |/ /     \ \
  | | (_| \__ \   <  .___/ /
  \_/\__,_|___/_|\_\ \____/ 

Напишите программу, которая проверяет, является ли введенный пользователем год високосным

hint: https://ru.wikihow.com/%D0%B2%D1%8B%D1%81%D1%87%D0%B8%D1%82%D1%8B%D0%B2%D0%B0%D1%82%D1%8C-%D0%B2%D0%B8%D1%81%D0%BE%D0%BA%D0%BE%D1%81%D0%BD%D1%8B%D0%B5-%D0%B3%D0%BE%D0%B4%D1%8B
"""
x = int(input("Введите год.."))
if x % 4 == 0 and x % 100 == 0:
  print("Весокосный год")
elif x % 100 == 0 and x % 400 == 0:
  print("Весокосный год")
else:
  print(x, "Весокосный год")


"""
 _____         _        ___ 
|_   _|       | |      /   |
  | | __ _ ___| | __  / /| |
  | |/ _` / __| |/ / / /_| |
  | | (_| \__ \   <  \___  |
  \_/\__,_|___/_|\_\     |_/

Напишите программау, которая проверяет, является ли введенная пользователем строка или число палиндромом, то есть читается ли оно одинаково с обеих сторон

hint: https://letpy.com/handbook/builtins/reversed/
"""

x = input("Введите число или строку: ")
y = x[::-1]
if x == y:
  print("Строка/число является полидромом")
else:
  print("Строка/число неявляется полидромом")

"""
 _____         _      _____ 
|_   _|       | |    |  ___|
  | | __ _ ___| | __ |___ \ 
  | |/ _` / __| |/ /     \ \
  | | (_| \__ \   <  /\__/ /
  \_/\__,_|___/_|\_\ \____/ 

Напишите программу, которая запрашивает число у пользователя и вычисляет факториал заданного числа, используя цикл или рекурсию

hint: https://ru.wikipedia.org/wiki/%D0%A4%D0%B0%D0%BA%D1%82%D0%BE%D1%80%D0%B8%D0%B0%D0%BB
"""

x = int(input("Введите факторила.."))
factorial = 1
for i in range (1, x+1):
  factorial = factorial * i
print (factorial)

"""
 _____         _       ____ 
|_   _|       | |     / ___|
  | | __ _ ___| | __ / /___ 
  | |/ _` / __| |/ / | ___ \
  | | (_| \__ \   <  | \_/ |
  \_/\__,_|___/_|\_\ \_____/

Напишите программу, которая проверяет, является ли число простым (делится только на 1 и само на себя). Используйте перебор делителей.

hint: x <= 1 - не простые числа
hint 2: %
"""

x = int(input("Введите число.."))
count = 0
if x <= 1: 
  print ("не простое")
else:
  for i in range (1, x+1):
    if x % i == 0:
      count += 1
  if count != 2:
    print ("не простое") 
  else:
    print ("простое")   

"""
 _____         _      ______
|_   _|       | |    |___  /
  | | __ _ ___| | __    / / 
  | |/ _` / __| |/ /   / /  
  | | (_| \__ \   <  ./ /   
  \_/\__,_|___/_|\_\ \_/    

Напишите программу, которая находит сумму всех цифр числа

hint: циклы
"""
x = int(input("Введите число.."))
сумма = 0
while x != 0:
  a = x % 10
  x = x // 10
  сумма += a
print (сумма)
"""
 _____         _      _____ 
|_   _|       | |    |  _  |
  | | __ _ ___| | __  \ V / 
  | |/ _` / __| |/ /  / _ \ 
  | | (_| \__ \   <  | |_| |
  \_/\__,_|___/_|\_\ \_____/

Напишите программу, которая генерирует последовательность Фибоначчи до указанного числа или количества элементов

hint: 1, 1, 2, 3 https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8
hint 2: попробуйте решить с помощью рекурсии
"""

def fibonacci_limit(x):
    sequence = []
    a, b = 0, 1
    while a <= x:
        sequence.append(a)
        a, b = b, a + b
    return sequence

x = int(input("Введите число: "))
print(f"Последовательность Фибоначчи до {x}: {fibonacci_limit(x)}")5





