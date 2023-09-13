from python_trening.task_9_checks import Checks
class Input(Checks):
    def __init__(self, Loc, text):
        super().__init__(Loc)
        self.Loc = Loc                 #Создал две одинаковых переменных , одна наследуется из checks и создаю ее и в Input это не совсем правильно
        self.text = text

class Button(Checks):
    def __init__(self, Loc, text):
        super().__init__(Loc)
        self.Loc = Loc
        self.text = text

class Title(Checks):
    def __init__(self, Loc, text):
        super().__init__(Loc)
        self.Loc = Loc
        self.text = text

class Link(Checks):
    def __init__(self, Loc, text):
        super().__init__(Loc)
        self.Loc = Loc
        self.text = text

search = Input("Location", "text")
button = Button("Button location", "Button text")
title = Title("Title location", "Title text")
link = Link("Link location", "Link text")

print(search.text, search.Loc)
print(button.text, button.Loc)
print(title.text, title.Loc)
print(link.text, link.Loc)