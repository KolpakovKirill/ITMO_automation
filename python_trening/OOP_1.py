class Button:

    type: str =  'Кнопка '
    def __init__(self, text, link):
        self.text = text
        self.link = link



home = Button('Домой', '/home')
catalog_msk = Button('Каталог', '/msk/catalog')


print(home.text)
print('Кнопка' + home.text + 'имеет ссылку ' + home.link)

print('\n')

print(catalog_msk.text)
print('Кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)
print(home.type)
print(catalog_msk.type)