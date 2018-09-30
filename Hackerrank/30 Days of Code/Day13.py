from abc import ABCMeta, abstractclassmethod

class Book(object, metaclass=ABCMeta):
    def __int__(self, title, author):
        self.title = title
        self.author = author

    @abstractclassmethod
    def display(cls):
        pass


class MyBook(Book):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print('Title: {} \nAuthor: {} \nPrice: {}'
              .format(self.title, self.author, self.price))


title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()
