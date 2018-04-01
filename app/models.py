"""Contains the models used by the application"""

from werkzeug.security import check_password_hash, generate_password_hash
import datetime
from app import db


<<<<<<< HEAD
users_list = []
books_list = []
borrowing_info = []
# token blacklist
blacklist = set()


class Book:
    """Class containing all the book information"""

    book_id = 0

    def __init__(self, title='', publisher='', 
        category='', subcategory='', description='', 
        pub_year=''):

        self.id = id
        self.title = title
        self.publisher = publisher
        self.publication_year = pub_year
        self.edition = 1
        self.category = category
        self.subcategory = subcategory
        self.description = description
        self.is_borrowed = False

    def generate_id(self):
        Book.book_id += 1
        self.id = Book.book_id

    def save(self):
        """Save current instance in the books list"""

        self.generate_id()
        books_list.append(self)

    def delete(self):
        """Delete the current instance in the books list"""

        books_list.remove(self)

    @staticmethod
    def get_by_id(book_id):
        """Get a book by its id"""

        for book in books_list:
            if book.id == book_id:
                return book
        return None

    @staticmethod
    def get_all():
        """Get all books in the books list"""

        return books_list

    def serialize(self):
        """Return a dictionary object with all the book details"""

        return {
            'book_id': self.id,
            'book_title': self.title,
            'publisher': self.publisher,
            'publication_year': self.publication_year,
            'edition': self.edition,
            'category': self.category,
            'subcategory': self.subcategory,
            'description': self.description
        }


class User:
    """Class containing all the user information"""

    def __init__(self):
        self.id = None
        self.email = None
        self.password = None
        self.is_admin = False
        self.books = []
        self.books_borrowed = []

=======
blacklist = set()    # token blacklist


class Book(db.Model):
    """class containing all the book information"""

    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    publisher = db.Column(db.String)
    publication_year = db.Column(db.String)
    edition = db.Column(db.String)
    category = db.Column(db.String)
    subcategory = db.Column(db.String)
    description = db.Column(db.String)
    available = db.Column(db.Integer, default=1)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(book_id):
        return Book.query.get(book_id)

    @staticmethod
    def get_all():
        return Book.query.all()

    def __repr__(self):
        return '<Book: {}>'.format(self.title)


class User(db.Model):
    """class containing all the user information"""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    is_admin = db.Column(db.String)
    borrowed_books = db.relationship('BorrowLog', backref='user')

>>>>>>> Create Book, User and BorrowLog models
    def set_password(self, password):
        """Generate a password hash"""

        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Check if the entered password and the stored password are the same"""

        return check_password_hash(self.password, password)

    def save(self):
<<<<<<< HEAD
        """Save current instance in the users list"""

        users_list.append(self)
=======
        db.session.add(self)
        db.session.commit()
>>>>>>> Create Book, User and BorrowLog models

    def borrow_book(self, book_id):
        """Borrow a book"""

        book = Book.get_by_id(book_id)
<<<<<<< HEAD
        self.books_borrowed.append(book)
        book.is_borrowed = True
=======
>>>>>>> Create Book, User and BorrowLog models
        now = datetime.datetime.now()
        record = BorrowLog(user_id=self.id,
                           book_id=book.id,
                           borrow_timestamp=now)
        record.save()

    def return_book(self):
        pass

    def borrowing_history(self):
        pass

    @staticmethod
    def get_by_email(email):
<<<<<<< HEAD
        """Retrieve a user by their email"""

        for user in users_list:
            if user.email == email:
                return user


class BorrowLog:
    """Class containing log of all books borrowed"""

    def __init__(self, id, user, book, borrow_date):
        self.id = id
        self.user = user
        self.book = book
        self.borrow_date = borrow_date

    def save(self):
        """Save borrowing record"""

        borrowing_info.append(self)
=======
        return User.query.filter_by(email=email).first()

    def __repr__(self):
        return '<User: {}>'.format(self.email)


class BorrowLog(db.Model):
    """class containing log of all books borrowed"""

    __tablename__ = 'borrow_log'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)  # user who has borrowed the book
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), primary_key=True)  # book that has been borrowed
    borrow_timestamp = db.Column(db.DateTime)
    returned = db.Column(db.Boolean)
    return_timestamp = db.Column(db.DateTime)

    def save(self):
        db.session.add(self)
        db.session.commit()
>>>>>>> Create Book, User and BorrowLog models
