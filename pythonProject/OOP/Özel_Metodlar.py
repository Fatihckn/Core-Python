class Book:

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return self.pages == other.pages

    def __lt__(self, other):
        return self.pages < other.pages

book1 = Book("Python Programlama","Guido van Rossum", 360 )
book2 = Book("Java Basic","James Gosling", 500 )
book3= Book("C++ Guide","Bjarne Stroustrup", 360 )

print(book1) #__str__

print(book1 == book3) #True,__eq__

print(book1 < book2) #__lt__