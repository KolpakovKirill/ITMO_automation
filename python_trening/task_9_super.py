class A:
    def __init__(self):
        self.x = 10

#...




class B(A):

    def __init__(self):
        super().__init__()
        self.y = self.x + 5

print(B().y)  # так делать не принято мы обращаемся к атрибуту B до его создания # нцжно сначала создать b  а потом вызывать print()

b = B()
print(b.y)