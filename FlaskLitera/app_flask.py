from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    author = db.Column(db.String(30), nullable=False)
    name_father_Author = db.Column(db.String(5), nullable=False)
    title = db.Column(db.String(300), nullable=False)
    publisher = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    pages = db.Column(db.Integer, nullable=False)


class Journal(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    author = db.Column(db.String(30), nullable=False)
    name_father_Author = db.Column(db.String(5), nullable=False)
    title = db.Column(db.Text, nullable=False)
    publisher = db.Column(db.String(20), nullable=False)
    number_tom = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    page_start = db.Column(db.Integer, nullable=False)
    page_end = db.Column(db.Integer, nullable=False)



class Conf(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    author = db.Column(db.String(30), nullable=False)
    name_father_Author = db.Column(db.String(5), nullable=False)
    title = db.Column(db.Text, nullable=False)
    publisher = db.Column(db.String(20), nullable=False)
    place = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Integer, nullable=False)
    page_start = db.Column(db.Integer, nullable=False)
    page_end = db.Column(db.Integer, nullable=False)



@app.route('/')
def main_page():
    return render_template('main.html')


@app.route('/descript')
def descript_page():
    return render_template('descript.html')


@app.route('/book', methods=['POST', 'GET'])
def book_page():
    if request.method == 'POST':
        author = request.form['author']
        name_father_Author = request.form['name_father_Author']
        title = request.form['title']
        publisher = request.form['publisher']
        city = request.form['city']
        year = request.form['year']
        pages = request.form['pages']
        books = Book(
            author=author,
            name_father_Author=name_father_Author,
            title=title,
            publisher=publisher,
            city=city,
            year=year,
            pages=pages
        )
        db.session.add(books)
        db.session.commit()
        book = Book.query.order_by(desc(Book.id)).first()
        return render_template('book_final.html', book=book)

    return render_template('book.html')


@app.route('/book_final')
def book_final_page():
    book = Book.query.order_by(Book.id).first()
    return render_template('book_final.html', book=book)


@app.route('/journal', methods=['POST', 'GET'])
def journal_page():
    if request.method == 'POST':
        author = request.form['author']
        name_father_Author = request.form['name_father_Author']
        title = request.form['title']
        publisher = request.form['publisher']
        number_tom = request.form['number_tom']
        year = request.form['year']
        page_start = request.form['page_start']
        page_end = request.form['page_end']
        journal = Journal(
            author=author,
            name_father_Author=name_father_Author,
            title=title,
            publisher=publisher,
            number_tom=number_tom,
            year=year,
            page_start=page_start,
            page_end=page_end
        )
        db.session.add(journal)
        db.session.commit()
        journal = Journal.query.order_by(desc(Journal.id)).first()
        return render_template('journal_final.html', journal=journal)
    else:
        return render_template('journal.html')


@app.route('/journal_final')
def journal_final_page():
    journal = Journal.query.order_by(Journal.id).first()
    return render_template('journal_final.html', journal=journal)


@app.route('/conference', methods=['POST', 'GET'])
def conf_page():
    if request.method == 'POST':
        author = request.form['author']
        name_father_Author = request.form['name_father_Author']
        title = request.form['title']
        publisher = request.form['publisher']
        city = request.form['city']
        place = request.form['place']
        date = request.form['date']
        year = request.form['year']
        page_start = request.form['page_start']
        page_end = request.form['page_end']
        conf = Conf(
            author=author,
            name_father_Author=name_father_Author,
            title=title,
            publisher=publisher,
            place=place,
            date=date,
            city=city,
            year=year,
            page_start=page_start,
            page_end=page_end
        )
        db.session.add(conf)
        db.session.commit()
        conf = Conf.query.order_by(desc(Conf.id)).first()
        return render_template('conf_final.html', conf=conf)
    else:
        return render_template('conf.html')


if __name__ == "__main__":
    app.run(debug=True)
