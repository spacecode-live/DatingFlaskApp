"""file to seed data from generated data in seed_data into sqlite database"""
from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy
from dating.models import *
from random import choice
import datetime
from dating import bcrypt
#import pdb; pdb.set_trace()

def load_users():
    """Load users from static/user_data.txt into database."""

    print ("User")
    User.query.delete()

    file = open("seed_data/user_data.txt")
    for row in file:
        row = row.rstrip()
        row = row.split("|")

        user_id = row[0]
        fname = row[1]
        lname = row[2]
        email = row[3]
        user_name = row[4]
        password = row[5]
        date_of_birth = row[6]
        zipcode = row[7]
        phone = row[8]
        profile_picture = row[10]

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        #insert user
        user = User(id=user_id,
                    firstname=fname,
                    lastname=lname,
                    email=email,
                    username=user_name,
                    password=hashed_password,
                    date_of_birth=date_of_birth,
                    city=zipcode,
                    phone=phone,
                    image_file=profile_picture)

        db.session.add(user)

    db.session.commit()


def load_books():
    """Load books from book_genre_data into database."""

    print ("BookGenre")

    #read book_genre_data
    for row in open("seed_data/book_genre_data.txt"):
        row = row.rstrip()
        book_genre_id, book_genre_name = row.split("|")
        # insert book genre
        book = BookGenre(book_genre_id=book_genre_id,
                          book_genre_name=book_genre_name)

        db.session.add(book)

    db.session.commit()


def load_movies():
    """Load movies from movie_genre_data into database."""

    print ("MovieGenre")

    for row in open("seed_data/movie_genre_data.txt"):
        row = row.rstrip()
        movie_genre_id, movie_genre_name = row.split("|")
        #insert movie
        movie = MovieGenre(movie_genre_id=movie_genre_id,
                          movie_genre_name=movie_genre_name)

        db.session.add(movie)

    db.session.commit()


def load_music():
    """Load music from music_genre_data into database."""

    print ("MusicGenre")

    for row in open("seed_data/music_genre_data.txt"):
        row = row.rstrip()
        music_genre_id, music_genre_name = row.split("|")
        #insert music
        music = MusicGenre(music_genre_id=music_genre_id,
                          music_genre_name=music_genre_name)

        db.session.add(music)

    db.session.commit()



def load_cuisines():
    """Load  from fav_cuisine_data into database."""

    print ("FavCuisine")

    for row in open("seed_data/fav_cuisine_data.txt"):
        row = row.rstrip()
        fav_cuisine_id, fav_cuisine_name = row.split("|")
        #insert cuisine
        cuisine = FavCuisine(fav_cuisine_id=fav_cuisine_id,
                          fav_cuisine_name=fav_cuisine_name)

        db.session.add(cuisine)

    db.session.commit()


def load_hobbies():
    """Load  from hobby_data_data into database."""

    print ("Hobby")

    for row in open("seed_data/hobby_data.txt"):
        row = row.rstrip()
        hobby_id, hobby_name = row.split("|")
        #insert hobby
        hobby = Hobby(hobby_id=hobby_id,
                          hobby_name=hobby_name)

        db.session.add(hobby)

    db.session.commit()




def load_religions():
    """Load  from book_genre_data into database."""

    print ("Religions")

    for row in open("seed_data/religion_data.txt"):
        row = row.rstrip()
        religion_id, religion_name = row.split("|")
        #insert religion
        religion = Religion(religion_id=religion_id,
                            religion_name=religion_name)

        db.session.add(religion)

    db.session.commit()



def load_outdoor_activities():
    """Load  from book_genre_data into database."""

    print ("Outdoors")

    for row in open("seed_data/outdoor_data.txt"):
        row = row.rstrip()
        outdoor_id, outdoor_activity = row.split("|")
        #insert outdoor
        outdoor = Outdoor(outdoor_id=outdoor_id,
                              outdoor_activity=outdoor_activity)

        db.session.add(outdoor)

    db.session.commit()




if __name__ == "__main__":
    from flask import Flask
    from dating import app
    SQLAlchemy(app)

    # Import different types of data
    load_books()
    load_movies()
    load_music()
    load_cuisines()
    load_hobbies()
    load_religions()
    load_outdoor_activities()
