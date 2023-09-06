#2.	Функция на вход получает два произвольных числа. Вывести в консоль наибольшее из чисел.
def num_1 (a, b):
    if a > b:
        print(a)
    else:
        print(b)
num_1(50, 10)
#Или
def num_2(a, b):
    max_n = max(a, b)
    print(max_n)
num_2(10, 20)
#3.	Функция на вход получает два произвольных числа. Вывести в консоль “yes”, если они отличаются друг от друга на 135, иначе вывести на экран “No”
def num_3(a, b):
    if a - b == 135 or b - a == 135:
        print("Yes")
    else:
        print("No")

num_3(200, 335)

#ИЛИ
def num_4 (a, b):
    if abs(a - b) == 135:
        print('yes')
    else:
        print('no')
num_4(100, 235)

#4.	Функция на вход получает произвольное число от 1 до 12 (номер месяца). Вывести название сезона года в консоль (зима, весна, лето, осень)

def season_1(month):
    seasons = ['Зима', 'Весна', 'Лето', 'Осень']
    if month in [12, 1, 2]:
        season = seasons[0]  # Зима
    elif month in [3, 4, 5]:
        season = seasons[1]  # Весна
    elif month in [6, 7, 8]:
        season = seasons[2]  # Лето
    elif month in [9, 10, 11]:
        season = seasons[3]  # Осень

        print(season)
season_1(3)

#Или
def season_2(month):
    seasons = ['Зима', 'Весна', 'Лето', 'Осень']

    if month in [12, 1, 2]:
        season = seasons[0]
    elif month in [3, 4, 5]:
        season = seasons[1]
    elif month in [6, 7, 8]:
        season = seasons[2]
    else:
        season = seasons[3]
    print(season)
season_2(1)
#Или
def season_3(month):
    seasons = ["зима", "весна", "лето", "осень"]
    for i in range(1, 13):   #?
        if month == i:
            season = seasons[i // 3 % 4] # можно ли проще?
            print(season)
season_3(3)

#5.	Функция на вход получает три произвольных числа. Если все числа больше 10, то вывести на экран “yes”, иначе “no”;
def num_4(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print("yes")
    else:
        print("no")
num_4(15, 12, 20)
#6.	Функция на вход получает список, состоящий из 5 произвольных чисел. Найти количество положительных чисел среди них.

def num_5(a):
    positive_count = 0
    for num in a:
        if num > 0:
            positive_count += 1
    print(f'Количество положительных чисел: {positive_count}')
a = [1, -2, 3, 0, 4]
num_5(a)

#или
def count_positive_numbers(numbers):
    count = 0
    for num in numbers:
        if num > 0:
            count += 1
    return count
numbers = [5, -2, 10, -7, 3]
positive_count = count_positive_numbers(numbers)
print(positive_count)

#7.	Функция на вход получает 2 переменные.a.	Кол-во лет (int)b.	Кол-во месяцев (int)Вывести в консоль количество дней за это время. Считать, что в каждом месяце 29 дней.
def year_month(a, b):
    c = a * 365 + b * 29
    print(f'Количество дней: {c}')

year_month(3, 6)

#или
def year_month(a, b):
    c = a * 365 + b * 29
    print('Количество дней: ' + str(c))

year_month(3, 6)

#или

def year_month(a, b):
    c = a * 365 + b * 29
    print('Количество дней:',  (c))

year_month(3, 6)