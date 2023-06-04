from models.book import Book

book1 = Book("Catch-22", "Joseph Heller", "War Fiction", False)
book2 = Book("Embassytown", "China Mieville", "Science Fiction", False)
book3 = Book("The Final Empire", "Brandon Sanderson", "Fantasy", True)

book_list = [book1, book2, book3]

def add_new_book(new_book):
    book_list.append(new_book)

def delete_book(index):
    book_list.pop(index)

def checkout_book(index):
    book_list[index].checked_out = not book_list[index].checked_out