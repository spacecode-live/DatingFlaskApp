from dating import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
#The purpose of this field is to hold a hash of the user password, which will be used to verify the password entered
#by the user during the login process. werkzeug is a package that implements password hashing.

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
#Flask-Login knows nothing about databases, it needs the application's help in loading a user.
#configure a user loader function that can be called to load a user given the ID.
#The user loader is registered with Flask-Login with the @login.user_loader decorator.

class User(db.Model, UserMixin):  #This class defines several fields as class variables.
    """ User of the Dating website."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    image_file = db.Column(db.String(20), nullable=True, default='default.jpg')
    #profile_picture = db.Column(db.String(250), default = 'default.jpg', nullable=True)

    def _repr_(self): #The __repr__ method tells Python how to print objects of this class
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Interest(db.Model):
    """ User interests and hobbies for matchmaking, Each Column will
    hold integers that correspond to the information on other tables.
    """

    __tablename__ = 'interests'

    interest_id = db.Column(db.Integer, autoincrement=True,
                            primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    book_genre_id = db.Column(db.Integer,
                            db.ForeignKey('book_genres.book_genre_id'),
                            nullable=False)
    movie_genre_id = db.Column(db.Integer,
                                db.ForeignKey('movie_genres.movie_genre_id'),
                                nullable=False)
    music_genre_id = db.Column(db.Integer,
                                db.ForeignKey('music_genres.music_genre_id'),
                                nullable=False)
    fav_cuisine_id = db.Column(db.Integer,
                                db.ForeignKey('fav_cuisines.fav_cuisine_id'),
                                nullable=False)
    hobby_id = db.Column(db.Integer,
                        db.ForeignKey('hobbies.hobby_id'), nullable=False)
    religion_id = db.Column(db.Integer,
                        db.ForeignKey('religions.religion_id'),
                        nullable=False)
    outdoor_id = db.Column(db.Integer,
                        db.ForeignKey('outdoors.outdoor_id'),
                        nullable=False)

    def __repr__ (self):
        """return interest choices of the user"""

        d1 ='< interest_id={a}, book_genre_id={b},'.format(a=self.interest_id,
                                                        b=self.book_genre_id)
        d2 =' movie_genre_id={c}, music_genre_id={d},'.format(c=self.movie_genre_id,
                                                        d=self.music_genre_id)
        d3 =' food_habit_id={e}, fav_cuisine_id={f},'.format(e=self.food_habit_id,
                                                        f=self.fav_cuisine_id)
        d4 =' hobby_id={g}, politicial_view_id={h},'.format(g=self.hobby_id,
                                                        h=self.political_view_id)
        d5 =' religion_id={i}, outdoor_id={j}>'.format(i=self.religion_id,
                                                        j=self.outdoor_id)

        return d1 + d2 + d3 + d4 + d5


class UserMatch(db.Model):
    """holds matches made through the history of the app"""

    __tablename__ = "user_matches"

    match_id = db.Column(db.Integer, autoincrement=True,
                        primary_key=True)
    user_id_1 = db.Column(db.Integer,
                        db.ForeignKey('users.id'),
                        nullable=False)
    user_id_2 = db.Column(db.Integer,
                        db.ForeignKey('users.id'),
                        nullable=False)
    match_date = db.Column(db.DateTime, nullable=False)
    user_2_status = db.Column(db.Boolean, nullable=False)
    query_pincode = db.Column(db.String(20), nullable=False)

    def __repr__ (self):
        """return interest choices of the user"""

        d1 = '< match_id={a}, user_id_1={b},'.format(a=self.match_id,
                                                    b=self.user_id_1)
        d2 =' user_id_2={c}, match_date={d}>'.format(c=self.user_id_2,
                                                    d=self.match_date)

        return d1 + d2


class PendingMatch(db.Model):
    """holds a list of all pending matches for user queries"""

    __tablename__ = "pending_matches"

    user_query_id = db.Column(db.Integer, autoincrement=True,
                            primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                            nullable=False)
    query_pin_code = db.Column(db.Integer, nullable=False)
    query_time = db.Column(db.DateTime, nullable=False)
    pending = db.Column(db.Boolean, nullable=False)

    def __repr__ (self):
        """return information about a user query"""

        d1 = "<user_query_id={a}, user_id={b},".format(a=self.user_query_id,
                                                        b=self.user_id)
        d2 = " query_pin_code={c}, query_time={d},".format(c=self.query_pin_code,
                                                        d=self.query_time)
        d3 = " pending={e}>".format(e=self.pending)

        return d1 + d2 + d3

class BookGenre(db.Model):
    """Holds the Music_genres and their corresponding ids"""

    __tablename__ = 'book_genres'

    book_genre_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    book_genre_name = db.Column(db.String(40), nullable=False)

    interest = db.relationship('Interest',
                            backref=db.backref('book_genre'))

    def __repr__ (self):
        """displays the ids of Book genres and book genres
        Can be cross-referenced with the interests table"""

        return'<book_genre_id={}, book_genre_name={}>'.format(self.book_genre_id,
                                                            self.book_genre_name)


class MovieGenre(db.Model):
    """Holds the Movie names and their corresponding ids"""

    __tablename__ = 'movie_genres'

    movie_genre_id= db.Column(db.Integer, autoincrement=True,
                                            primary_key=True)
    movie_genre_name = db.Column(db.String(40), nullable=False)

    interest = db.relationship('Interest',
                            backref=db.backref('movie_genre'))

    def __repr__(self):
        """displays the ids of movies and movie names
        Can be cross-referenced with the interests table"""

        return'<move_genre_id={}, movie_genre_name={}>'.format(self.movie_genre_id,
                                                            self.movie_genre_name)


class MusicGenre(db.Model):
    """Holds the Music_genres and their corresponding ids"""

    __tablename__ = 'music_genres'

    music_genre_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    music_genre_name = db.Column(db.String(40), nullable=False)

    interest = db.relationship('Interest',
                            backref=db.backref('music_genre'))

    def __repr__ (self):
        """displays the ids of music genres and music genres
        Can be cross-referenced with the interests table"""

        return'<music_genre_id={}, music_genre_name={}>'.format(self.music_genre_id,
                                                            self.music_genre_name)


class FavCuisine(db.Model):
    """Holds the types of cuisines and thier corresponding ids"""

    __tablename__ = 'fav_cuisines'

    fav_cuisine_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fav_cuisine_name= db.Column(db.String(40), nullable=False)

    interest = db.relationship('Interest',
                            backref=db.backref('fav_cuisine'))

    def __repr__ (self):
        """displays the ids of cuisines and cuisine names
        Can be cross-referenced with the interests table"""

        return'<fav_cuisine_id={}, fav_cuisine_name={}>'.format(self.fav_cuisine_id,
                                                                self.fav_cuisine_name)


class Hobby(db.Model):
    """Holds the list of hobbies and thier corresponding ids"""

    __tablename__ = 'hobbies'

    hobby_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    hobby_name= db.Column(db.String(40), nullable=False)

    interest = db.relationship('Interest',
                            backref=db.backref('hobby'))

    def __repr__ (self):
        """displays the ids of hobbies and hobby names
        Can be cross-referenced with the interests table"""

        return'<hobby_id={}, hobby_name={}>'.format(self.hobby_id,
                                                    self.hobby_name)



class Religion(db.Model):
    """Holds the religious views and their corresponding ids"""

    __tablename__ = 'religions'

    religion_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    religion_name = db.Column(db.String(40), nullable=False)

    interest = db.relationship('Interest',
                            backref=db.backref('religion'))

    def __repr__ (self):
        """displays the ids of religion and religion names
        Can be cross-referenced with the interests table"""

        return'<religion_id={}, religion_name={}>'.format(self.religion_id,
                                                        self.religion_name)


class Outdoor(db.Model):
    """Holds the outdoor_activities and their corresponding ids"""

    __tablename__ = 'outdoors'

    outdoor_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    outdoor_activity = db.Column(db.String(40), nullable=False)

    interest = db.relationship('Interest',
                            backref=db.backref('outdoor'))

    def __repr__ (self):
        """displays the ids of oa, and oa
        Can be cross-referenced with the interests table"""

        return'<outdoor_id={}, outdoor_activity={}>'.format(self.outdoor_id,
                                                            self.outdoor_activity)
