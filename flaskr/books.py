from flask import (
    Blueprint, redirect, session, url_for
)

from flaskr.db import get_db

bp = Blueprint('books', __name__, url_prefix='/books')

@bp.route('/list', methods=('GET',))
def books_list():
    books = get_db().execute(
        'SELECT * FROM books'
    )
    session['books'] = books
    return redirect(url_for("books.list"))