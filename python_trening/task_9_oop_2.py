class Page:  # создали класс

    def __init__(self, url):
        self.url = url

    def get(self):
        print(self.url)
home = Page('https://demoqa.com/')
home.get()                #как вызов функции  # переход на сайт



