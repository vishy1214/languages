class Book:
    def __init__(self,author, title):
        self.author = author
        self.title = title

    def bookdesc(self):
        return "Book '{}' by {}".format(self.title,self.author)



book = Book("George Martin","A Game of Thrones")
type(book)
print(book.author)
print(book.bookdesc())

bookA = Book("George Martin","A Game of Thrones")

print(id(book))

print(id(bookA))