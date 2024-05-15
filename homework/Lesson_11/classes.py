# Библиотека
# Первый класс
# Создайте класс book с атрибутами:

# материал страниц
# наличие текста
# название книги
# автор
# кол-во страниц
# ISBN
# флаг зарезервирована ли книга или нет (True/False).
# Какие-то из атрибутов будут общими для всех книг (материал, наличие текста),
# какие-то индивидуальными.
# Создайте несколько (штук 5) экземпляров разных книг.
# После создания пометьте одну книгу как зарезервированную.
# Распечатайте детали о каждой книге в таком виде:
# Если книга зарезервирована:

# Название: Идиот, Автор: Достоевский, страниц: 500, материал: бумага,
# зарезервирована
# если не зарезервирована:

# Название: Идиот, Автор: Достоевский, страниц: 500,  материал: бумага


class Book:
    page_material = 'бумага'
    text_in_book = True

    def __init__(self, book_name, book_author, book_pages, isbn, reserved):
        self.book_name = book_name
        self.book_author = book_author
        self.book_pages = book_pages
        self.isbn = isbn
        self.reserved = reserved


book_1 = Book('Идиот', 'Достоевский', 500, 12345, False)
book_2 = Book('Война и мир', 'Толстой', 1000, 12346, False)
book_3 = Book('Улитка на склоне', 'Стругацкие', 300, 12347, True)
book_4 = Book('Ловец душ', 'Дембски-Боуден', 800, 12348, False)
book_5 = Book('Малазанская книга павших', 'Стивенсон', 10000, 12349, False)

books = [book_1, book_2, book_3, book_4, book_5]

for book in books:
    if book.reserved:
        print(f"Название: {book.book_name}, Автор: {book.book_author}, " +
              f"ISBN: {book.isbn}, страниц:{book.book_pages}, " +
              f"материал: {book.page_material}, зарезервирована")
    else:
        print(f"Название: {book.book_name}, Автор: {book.book_author}, " +
              f"ISBN: {book.isbn}, страниц: {book.book_pages}, " +
              f"материал: {book.page_material}")

# Второй класс
# Создайте дочерний класс для первого. Это будет класс для школьных учебников.
# В нем будут дополнительные атрибуты:

# предмет (типа математика, история, география),
# класс (школьный класс, для которого этот учебник)(осторожно с названием
# переменной. class - зарезервированное слово),
# наличие заданий (bool)
# Создайте несколько экземпляров учебников.
# После создания пометьте один учебник как зарезервированный.
# Распечатайте детали о каждом учебнике в таком виде: Если учебник
# зарезервирован:

# Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс:
# 9, зарезервирована
# если не зарезервирован:

# Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9


class SchoolBook(Book):
    def __init__(self, book_name, book_author, book_pages, subject,
                 class_number, tasks, reserved):
        super().__init__(book_name, book_author, book_pages, 12345, reserved)
        self.subject = subject
        self.class_number = class_number
        self.tasks = tasks


textbook_1 = SchoolBook('Алгебра', 'Иванов', 200, 'Математика', 9, True, False)
textbook_2 = SchoolBook('Геометрия', 'Петров', 300, 'Геометрия', 10, False,
                        True)
textbook_3 = SchoolBook('Рус. яз.', 'Сидорова', 500, 'Русский язык', 9, True,
                        False)

textbooks = [textbook_1, textbook_2, textbook_3]

for textbook in textbooks:
    if textbook.reserved:
        print(f"Название: {textbook.book_name}, " +
              f"Автор: {textbook.book_author}, " +
              f"страницы: {textbook.book_pages}, " +
              f"Материал: {textbook.page_material}, зарезервирована")
    else:
        print(f"Название: {textbook.book_name}, " +
              f"Автор: {textbook.book_author}, " +
              f"страницы: {textbook.book_pages}, " +
              f"Материал: {textbook.page_material}")
