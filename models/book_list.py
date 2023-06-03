from models.book import Book

book1 = Book("Catch-22", "Joseph Heller", "War Fiction", False)
book2 = Book("Embassytown", "China Mieville", "Science Fiction", False)
book3 = Book("The Final Empire", "Brandon Sanderson", "Fantasy", True)

book_list = [book1, book2, book3]

def add_new_book(new_book):
    book_list.append(new_book)

def delete_book(index):
    book_list.pop(index)

def check_out(selected_book_index):
    if book_list[selected_book_index].checked_out == False:
        book_list[selected_book_index].checked_out = True
    if book_list[selected_book_index].checked_out == True:
        book_list[selected_book_index].checked_out = False