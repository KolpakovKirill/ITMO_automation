# 1.	создайте класс прямоугольника.b.	методы - реализуйте 2 метода:i.	расчет площади прямоугольникаii.	расчет периметра прямоугольникаc.	создайте 3 объекта, рассчитайте площадь и периметр для каждого. Результаты выводить в консоль.

class Rectangle:


    def __init__(self, width, height):
        self.width = width                      # ширина
        self.height = height                    # высота


    def calculate_area(self):                    # расчет площади Формула S = A * B ,А - длина; В - ширина.
        return self.width * self.height


    def calculate_perimeter(self):                # растчет периметра Формула: P=2*(A+B) ,  А - длина; В - ширина.
        return 2 * (self.width + self.height)


# Создание Объектов, расчет площади и периметра
rectangle_1 = Rectangle(5, 10)
area_1 = rectangle_1.calculate_area()
perimeter_1 = rectangle_1.calculate_perimeter()


rectangle_2 = Rectangle(8,3)
area_2 = rectangle_2.calculate_area()
perimeter_2 = rectangle_2.calculate_perimeter()


rectangle_3 = Rectangle(15, 7)
area_3 = rectangle_3.calculate_area()
perimeter_3 = rectangle_3.calculate_perimeter()


print('Прямоугольник 1:', 'Площадь:', area_1, 'Периметр:', perimeter_1)
print('Прямоугольник 2:', 'Площадь:', area_2, 'Периметр:', perimeter_2)
print('Прямоугольник 3:', 'Площадь:', area_3, 'Периметр:', perimeter_3)


#2.	Создайте класс Math. a.	Создайте два атрибута — a и b. b.	Напишите методы i.	addition — сложение, ii.	multiplication — умножение, iii.	division — деление, iv.	subtraction — вычитание. При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.

class Math:


    def __init__(self, a, b):
        self.a = a
        self.b = b


    def addition(self):             # сложение
        return(self.a + self.b)


    def multiplication(self):        # умножение
        return (self.a * self.b)


    def division(self):                # деление
        return (self.a // self.b)


    def subtraction(self):              # вычитание
        return (self.a - self.b)


math_1 = Math(5, 10)           # math_1, math_2 все можно обозвать просто math?
addition = math_1.addition()

math_2 = Math(7, 13)
multiplication = math_2.multiplication()

math_3 = Math(20, 4)
division = math_3.division()

math_4 = Math(15, 2)
subtraction = math_4.subtraction()


print('Сложение: ', addition, 'Умножение: ', multiplication,'Деление: ', division, 'Вычитание: ', subtraction)

#ИЛИ
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        result = self.a + self.b
        print("Сложение:", result)

    def multiplication(self):
        result = self.a * self.b
        print("Умножение:", result)

    def division(self):
        result = self.a / self.b
        print("Деление:", result)

    def subtraction(self):
        result = self.a - self.b
        print("Вычитание:", result)


# Создание объекта класса Math
math = Math(5, 3)

# Вызов методов
math.addition()
math.multiplication()
math.division()
math.subtraction()


#Или
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        result = self.a + self.b
        return result

    def multiplication(self):
        result = self.a * self.b
        return result

    def division(self):
        result = self.a / self.b
        return result

    def subtraction(self):
        result = self.a - self.b
        return result


# Создание объекта класса Math
math = Math(5, 3)

# Вызов методов
print("Сумма:", math.addition())
print("Произведение:", math.multiplication())
print("Деление:", math.division())
print("Разность:", math.subtraction())


#


class Button:


    def __init__(self, text):
        self.text = text
        self.type = "Кнопка"
        self.locator = ""


    def click(self):
        return f"Клик по кнопке {self.text}"


text_box_button = Button("Text box")             #создает объект класса Button с именем `text_box_button` и аргументом "Text Box" переданным в конструктор класса. Таким образом, `text_box_button` представляет кнопку "Text Box".
submit_button = Button("Submit")


print(text_box_button.text)
print(submit_button.text)
print(text_box_button.click())
print(submit_button.click())


class Car:


    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year


    def sart_car(self):
        print("Автомобиль заведен")

    def turn_off_car(self):
        print("Автомобиль заглушен")


    def year_car(self, year):
        print(f"Год выпуска '{self.year}'")

    def type_car(self, type):
        print(f"Марка машины '{self.type}'" )


    def color_car(self, color):
        print(f"Цвет машины '{self.color}'")



car1 = Car("Красный", "Седан", 2020)     #
car1.sart_car()  # Выводит "Автомобиль заведен"   #
car1.turn_off_car()  # Выводит "Автомобиль заглушен"

car2 = Car("Синий", "Хэтчбек", 2018)
car2.year_car(2018)
car2.type_car("Хэтчбек")
car2.color_car("Синий")

car3 = Car("Зеленый","Кроссовер",2021)
print(car3.year)  # Выводит 2021
print(car3.type)  # Выводит "Кроссовер"
print(car3.color)  # Выводит "Зеленый"