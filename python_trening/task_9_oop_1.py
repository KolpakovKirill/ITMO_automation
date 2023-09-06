class Input:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

#search = Input('Локатор')
home = Input('Домой', '/home')


print(search.loc)
print(home.text)


class Button:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

search_2 = Button('Локатор')
home_2 = Button('Домой', '/home')


print(search_2.loc)
print(home_2.text)


class Title:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

search_3 = Title('Локатор')
home_3 = Title('Домой', '/home')


print(search_3.loc)
print(home_3.text)


class Link:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

search_4 = Link('Локатор')
home_4 = Link('Домой', '/home')


print(search_4.loc)
print(home_4.text)