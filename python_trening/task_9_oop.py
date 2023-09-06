class Button:  # создали класс

    type: str =  'Кнопка ' #константа внутри класса для всех объектов
    def __init__(self, text, link):     #аргументы(self, text, link)  #def __init__ конструктор класса
        self.text = text             # Атрибуты   # Текст кнопки
        self.link = link             # Атрибуты   #ссылка кнопки


#Создаем экземпляры класса (создаем объекты 1 и 2)
home = Button('Домой', '/home')           #объект 1  (в этом примере это кнопка)
catalog_msk = Button('Каталог', '/msk/catalog')   #объект 2  (в этом примере это кнопка)

#Получаем доступ к атрибутам
print(home.text)
print('Кнопка' + home.text + 'имеет ссылку ' + home.link)

print('\n')

print(catalog_msk.text)
print('Кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)
print(home.type)
print(catalog_msk.type)

#------

class ButtonTwo:

    def __init__(self, text, link, loc):    #метод инициализации # переменнная создана внутри функции доступна только внутри функции
        self.text = text
        self.link = link
        self.loc = loc  # Локатор

    def click(self):
        return 'Клик по локатору - {}'.format(self.loc)


# Создаем экземпляр класса
home_two = ButtonTwo('Домой','/home', 'button#home')

#Вызываем метод
print(home_two.click())