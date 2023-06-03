from flask import render_template, request, redirect
from app import app
from models.book_list import *
from models.book import *

@app.route("/home")
def index():
    return render_template('index.html', title='Home', book_list=book_list)

@app.route("/home/<index>")
def book_details(index):
    return render_template("book_details.html", book = book_list[int(index)])

@app.route("/home", methods=["POST"])
def add_book():
    book_title = request.form["title"]
    book_author = request.form["author"]
    book_genre = request.form["genre"]
    new_book = Book(book_title, book_author, book_genre, False)
    add_new_book(new_book)
    return redirect("/home")

@app.route("/home/delete/<index>")
def delete(index):
    delete_book(int(index))
    return redirect("/home")

@app.route("/home/books/<index>", methods=["POST"])
def check_out_book(index):
    check_out(int(index))
    return redirect("/home")
