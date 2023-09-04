def task_1_3(a: int = 10, b: float = 3.0, c: str = 'word', d: list = [1, 2, 3], f: bool = True):
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(f))

task_1_3()

#ИЛИ
def task_1():
    """
    документационная строка(docstring)
    Функция выводит на консоль тип каждой переменной с использованием встроенной функции `type()`.
    """
    a_int = 5
    b_float = 3.14
    c_str = "Hello World"
    d_list = [1, 2, 3, 4, 5]
    f_bool = True

    print(type(a_int))               #<class 'int'>
    print(type(b_float))             #<class 'float'>
    print(type(c_str))               #<class 'str'>
    print(type(d_list))              #<class 'list'>
    print(type(f_bool))              #<class 'bool'>

task_1()                             #Вызов функции
# ИЛИ

def task_1_1(a_int, b_float, c_str, d_list, f_bool):
    """
    Функция которая принимает пять аргументов
    """
    print(type(a_int))        #<class 'int'>
    print(type(b_float))      #<class 'float'>
    print(type(c_str))        #<class 'str'>
    print(type(d_list))       #<class 'list'>
    print(type(f_bool))       #<class 'bool'>

task_1_1(5, 3.14, "Hello World", [1, 2, 3, 4, 5], True)


#

def task_2():
    """
    Функция создает список `a` [1, 2, 3, 5, 8, 13, 21] затем выводит первые три элемента списка,
    используя срез `a[0:3
    """
    a = [1, 2, 3, 5, 8, 13, 21]      # эта последовательность чисел называется  "последовательностью Фибоначчи"
    print(a[0:3])

task_2()                             # Вызов функции
#ИЛИ
def task_2_2(a = [1, 2, 3, 5, 8, 13, 21]):
    return a[0:3]

print(task_2_2())

#
def task_3(a: int) -> int:
    return a ** 2
print(task_3(7))