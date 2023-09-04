def task_1(a: int = 10, b: float = 3.0, c: str = 'word', d: list = [1, 2, 3], f: bool = True):
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(f))

task_1()

def task_1():
    """
    документационная строка(docstring)
    Функция выводит на консоль тип каждой переменной с использованием встроенной функции `type()`.
    """
    a_int = 5                        #- Переменная `int` содержит целочисленное значение 5.
    b_float = 3.14                   #- Переменная `float` содержит значение с плавающей запятой 3.14.
    c_str = "Hello World"            #- Переменная `str` содержит строку "Hello World".
    d_list = [1, 2, 3, 4, 5]         #- Переменная `list` содержит список целых чисел [1, 2, 3, 4, 5].
    f_bool = True                    #- Переменная `bool` содержит булево значение True.

    print(type(a_int))               #<class 'int'>
    print(type(b_float))             #<class 'float'>
    print(type(c_str))               #<class 'str'>
    print(type(d_list))              #<class 'list'>
    print(type(f_bool))              #<class 'bool'>

task_1()                             #Вызов функции
# ИЛИ

def task_1_1(var_int, var_float, var_str, var_list, var_bool):
    """
    Функция которая принимает пять аргументов
    """
    print(type(var_int))        #<class 'int'>
    print(type(var_float))      #<class 'float'>
    print(type(var_str))        #<class 'str'>
    print(type(var_list))       #<class 'list'>
    print(type(var_bool))       #<class 'bool'>

task_1_1(5, 3.14, "Hello World", [1, 2, 3, 4, 5], True)
# Функция `task_1` вызывается с аргументами `5`, `3.14`, `"Hello World"`, `[1, 2, 3, 4, 5]` и `True`,
# что означает, что значения этих аргументов будут переданы в функцию `task_1` при ее вызове.

def task_2():
    """
    Функция создает список `a` [1, 2, 3, 5, 8, 13, 21] затем выводит первые три элемента списка,
    используя срез `a[0:3
    """
    a = [1, 2, 3, 5, 8, 13, 21]      # эта последовательность чисел называется  "последовательностью Фибоначчи"
    print(a[0:3])                    # вывод первых трех элементов списка

task_2()                             # Вызов функции

def task_2_2(a = [1, 2, 3, 5, 8, 13, 21]):
    return a[0:3]

# Внутри функции используется операция среза a[0:3] которая возвращает подсписок,
# содержащий элементы с индексами от 0 до 2 (включительно).

print(task_2_2())

# Функция вызывается без аргументов (`task_2_2()`),
# поэтому будет использован список по умолчанию `[1, 2, 3, 5, 8, 13, 21]`.
# Результат вызова функции будет `[1, 2, 3]`, который затем будет напечатан.

def task_3(a: int) -> int:
    return a ** 2
print(task_3(7))