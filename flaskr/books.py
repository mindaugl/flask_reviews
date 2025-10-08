from flask import (
    Blueprint, redirect, session, url_for, render_template
)

from flaskr.db import get_db

bp = Blueprint('books', __name__, url_prefix='/books')

@bp.route('/list', methods=('GET',))
def books_list():
    books = get_db().execute(
        'SELECT * FROM books'
    ).fetchall()
    session['books'] = books
    return render_template("books/list.html", books=books)