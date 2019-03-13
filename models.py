from app import db

class User(db.Model):
    """ User of the Dating website."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True,
                                    primary_key=True)
    fname = db.Column(db.String(100), nullable=False)
    lname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.String(100), nullable=False)
    zipcode = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    profile_picture = db.Column(db.String(250), nullable=True)

    interest = db.relationship('Interest',
                            backref=db.backref('User'))


class Interest(db.Model):
    """ User interests and hobbies for matchmaking, Each Column will
    hold integers that correspond to the information on other tables.
    """

    __tablename__ = 'interests'

    interest_id = db.Column(db.Integer, autoincrement=True,
                            primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    hobby_id = db.Column(db.Integer,
                        db.ForeignKey('hobbies.hobby_id'), nullable=False)
    religion_id = db.Column(db.Integer,
                        db.ForeignKey('religions.religion_id'),
                        nullable=False)
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
    outdoor_id = db.Column(db.Integer,
                        db.ForeignKey('outdoors.outdoor_id'),
                        nullable=False)

class BookGenre(db.Model):
    """Holds the Book_genres and their corresponding ids"""

    __tablename__ = 'book_genres'

    book_genre_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    book_genre_name = db.Column(db.String(40), nullable=False)

    interest = db.relationship('Interest',
                            backref=db.backref('book_genre'))


class MovieGenre(db.Model):
    """Holds the Movie names and their corresponding ids"""

    __tablename__ = 'movie_genres'

    movie_genre_id= db.Column(db.Integer, autoincrement=True,
                                            primary_key=True)
    movie_genre_name = db.Column(db.String(40), nullable=False)

    interest = db.relationship('Interest',
                            backref=db.backref('movie_genre'))


class MusicGenre(db.Model):
    """Holds the Music_genres and their corresponding ids"""

    __tablename__ = 'music_genres'

    music_genre_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    music_genre_name = db.Column(db.String(40), nullable=False)

    interest = db.relationship('Interest',
                            backref=db.backref('music_genre'))


class FavCuisine(db.Model):
    """Holds the types of cuisines and thier corresponding ids"""

    __tablename__ = 'fav_cuisines'

    fav_cuisine_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fav_cuisine_name= db.Column(db.String(40), nullable=False)

    interest = db.relationship('Interest',
                            backref=db.backref('fav_cuisine'))


class Hobby(db.Model):
    """Holds the list of hobbies and thier corresponding ids"""

    __tablename__ = 'hobbies'

    hobby_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    hobby_name= db.Column(db.String(40), nullable=False)

    interest = db.relationship('Interest',
                            backref=db.backref('hobby'))

class Religion(db.Model):
    """Holds the religious views and their corresponding ids"""

    __tablename__ = 'religions'

    religion_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    religion_name = db.Column(db.String(40), nullable=False)

    interest = db.relationship('Interest',
                            backref=db.backref('religion'))


class Outdoor(db.Model):
    """Holds the outdoor_activities and their corresponding ids"""

    __tablename__ = 'outdoors'

    outdoor_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    outdoor_activity = db.Column(db.String(40), nullable=False)

    interest = db.relationship('Interest',
                            backref=db.backref('outdoor'))


def example_data():
    """Fixed data to test app."""

    user1 = User(user_id=1, fname="Selina", lname="Mangaroo",
                email="selinamangaroo@gmail.com", user_name="SelinaMangaroo",
                password="PASSWORDSHOULDBEHASHED", date_of_birth="01-01-1998",
                zipcode="11436", phone="657897149")
    user2 = User(user_id=2,fname="Yohanes", lname="Berhane",
                email="yohannesberhane@gmail.com", user_name="yohannesberhane",
                password="PASSWORDSHOULDBEHASHED",date_of_birth="12-09-1997",
                zipcode="11432", phone="3015329251")
    user3 = User(user_id=3, fname="Alexandra", lname="BayBay",
                email="eforman@gmail.com", user_name="AlexBayBay",
                password="PASSWORDSHOULDBEHASHED", date_of_birth="12-12-1997",
                zipcode="11111", phone="6509908999")
    user4 = User(user_id=4, fname="Brandon", lname="Dow",
                email="kels@hotmail.com", user_name="kel",
                password="PASSWORDSHOULDBEHASHED", date_of_birth="01-11-1996",
                zipcode="11420", phone="789891849")

    db.session.add_all([user1, user2, user3, user4])
    db.session.commit()

    book_genre1 = BookGenre(book_genre_id=1,
                            book_genre_name="Fantasy")
    book_genre2 = BookGenre(book_genre_id=2,
                            book_genre_name="Fiction")

    movie_genre1 = MovieGenre(movie_genre_id=1,
                            movie_genre_name="Thriller")
    movie_genre2 = MovieGenre(movie_genre_id=2,
                            movie_genre_name="Comedy")

    music_genre1 = MusicGenre(music_genre_id=1,
                            music_genre_name="Hip-Hop")
    music_genre2 = MusicGenre(music_genre_id=2,
                            music_genre_name="Classic Rock")

    fav_cuisine1 = FavCuisine(fav_cuisine_id=1,
                            fav_cuisine_name="Ethiopian")
    fav_cuisine2 = FavCuisine(fav_cuisine_id=2,
                            fav_cuisine_name="Mexican")

    hobby1 = Hobby(hobby_id=1, hobby_name="Coding")
    hobby2 = Hobby(hobby_id=2, hobby_name="Coin Collecting")

    religion1 = Religion(religion_id=1, religion_name="Hindu")
    religion2 = Religion(religion_id=2, religion_name="Christian")

    outdoor1 = Outdoor(outdoor_id=1, outdoor_activity="Soccer")
    outdoor2 = Outdoor(outdoor_id=2, outdoor_activity="Swimming")

    user_interest1 = Interest(user_id=1, book_genre_id=2, movie_genre_id=1,
                            music_genre_id=1, food_habit_id=2,fav_cuisine_id=2,
                            hobby_id=2, political_view_id=1, religion_id=1,
                            outdoor_id=1)
    user_interest2 = Interest(user_id=2, book_genre_id=1, movie_genre_id=1,
                            music_genre_id=1, food_habit_id=1,fav_cuisine_id=2,
                            hobby_id=2, political_view_id=2, religion_id=2,
                            outdoor_id=1)
    user_interest3 = Interest(user_id=3, book_genre_id=2, movie_genre_id=1,
                            music_genre_id=1, food_habit_id=2,fav_cuisine_id=2,
                            hobby_id=1, political_view_id=1, religion_id=1,
                            outdoor_id=2)
    user_interest4 = Interest(user_id=4, book_genre_id=1, movie_genre_id=1,
                            music_genre_id=1, food_habit_id=1,fav_cuisine_id=2,
                            hobby_id=2, political_view_id=1, religion_id=2,
                            outdoor_id=1)

    db.session.add_all([user_interest1, user_interest2, user_interest3,
                        user_interest4, book_genre1, book_genre2, movie_genre1, movie_genre2,
                        music_genre1, music_genre2, fav_cuisine1, fav_cuisine2, hobby1, hobby2,
                        religion1, religion2, outdoor1, outdoor2])

    db.session.commit()
