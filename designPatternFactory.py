class Book:
    def book_category(self):    pass

class PythonBook(Book):
    def book_category(self):
        print "Python book"

class JavaBook(Book):
    def book_category(self):
        print "Java book"

class BookFactory:
    def get_book(self, book_type):
        if book_type=='python':
            return PythonBook()
        elif book_type=='java':
            return JavaBook()
        else:
            return None

bookFactory = BookFactory()
pythonBook = bookFactory.get_book('python')
pythonBook.book_category()

javaBook = bookFactory.get_book('java')
javaBook.book_category()