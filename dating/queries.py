""" This file queries databases """

from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy
from dating.models import *
from functools import wraps
from flask import Flask, render_template, redirect, request, flash, session, g
import datetime



def get_user_id(input_email):

    """ Queries the users table with email as an argument and
        returns the user_id of a user.
    """

    user = User.query.filter(User.email == '{}'.format(input_email)).all()
    user_id = user[0].user_id
    return user_id

def get_user_name(input_id):
    """ Queries the users table and accepts a userid as input.
        Returns the fname and lname of the user.
    """

    user = User.query.filter(User.id == input_id).first()
    username = user.username;
    return username

def get_user_info(input_id):
    """ Queries the users table and accepts a userid as input.
        Returns all the user info as a list
        OUTPUT FORMAT = string.
    """

    user = User.query.filter(User.id == input_id).all()

    user_id = user[0].id
    email = user[0].email
    user_name = user[0].username
    date_of_birth = user[0].date_of_birth
    zipcode = user[0].city
    phone = user[0].phone
    fname = user[0].firstname
    lname = user[0].lastname
    profile_picture = user[0].image_file


    return [user_id, email, user_name,
            date_of_birth, zipcode, phone,
            fname, lname, profile_picture]


def get_all_made_matches(user_id):
    """ Queries the user_matches table and accepts a userid as input.
        INPUT FORMAT = Integer.
        Returns a list of tuples with the first element as the user name
        and the second element as the url to the profile picture.
        OUTPUT FORMAT = list of tuples of strings.
    """
    # query the user_matches table
    check_matches = UserMatch.query.filter(UserMatch.user_id_1 == user_id,
                                         UserMatch.user_2_status == True)

    matches = check_matches.all()
    all_match_info = []

    for match in matches:
        user_id2 = match.user_id_2
        user_info = get_user_info(user_id2)
        user_name = user_info[6] + " " + user_info[7]
        all_match_info.append(user_name, user_info[-1])

    return all_match_info

def validate_password(input_email, input_password):
    """ Queries the users table and accepts email and password as inputs for validation"""

    user = User.query.filter(User.email == '{}'.format(input_email)).first()
    password = user.password
    email = user.email

    return password == input_password and email == input_email

def get_max_id(input_table_id):
    """ Queries a given table.
        Returns a max count for the primary key of the given table.
    """

    max_id = db.session.query(func.max(input_table_id)).one()
    return int(max_id[0])

def all_book_genres():
    """ Queries the book_genres table.Returns a list of tuples, first element is the genre id and second
        element is the name."""

    book_genres = BookGenre.query.all()
    books = []

    for book in book_genres:
        books.append((book.book_genre_id, book.book_genre_name))

    return ["Favorite book genre", books]


def all_movie_genres():
    """ Queries the movie_genres table.Returns a list of tuples, first element is the genre id and second
        element is the name."""


    movie_genres = MovieGenre.query.all()
    movies = []

    for movie in movie_genres:
        movies.append((movie.movie_genre_id, movie.movie_genre_name))

    return ["Favorite movie genre", movies]


def all_music_genres():
    """ Queries the music_genres table. Returns a list of tuples, first element is the genre id and second
        element is the name.
    """

    music_genres = MusicGenre.query.all()
    music = []

    for music_genre in music_genres:
        music.append((music_genre.music_genre_id,
                         music_genre.music_genre_name))

    return ["Favorite music genre", music]

def all_fav_cuisines():
    """ Queries the fav_cuisines table. Returns a list of tuples, first element is the cuisine id and second
        element is the name.
    """

    fav_cuisines = FavCuisine.query.all()
    cuisines = []

    for cuisine in fav_cuisines:
        cuisines.append((cuisine.fav_cuisine_id, cuisine.fav_cuisine_name))

    return ["Preferred cuisine type", cuisines]


def all_hobbies():
    """ Queries the hobbies table.Returns a list of tuples, first element is the hobby id and second
        element is the name.
    """

    hobbies = Hobby.query.all()
    hobby = []

    for curr_hobby in hobbies:
        hobby.append((curr_hobby.hobby_id, curr_hobby.hobby_name))

    return ["Favorite hobby", hobby]

def all_religions():
    """ Queries the religions table. Returns a list of tuples, first element is the religion id and second
        element is the name.
    """

    religions = Religion.query.all()
    rel = []

    for religion in religions:
        rel.append((religion.religion_id, religion.religion_name))

    return ["Religion", rel]


def all_outdoors():
    """ Queries the outdoors table. Returns a list of tuples, first element is the activity id and second
        element is the name.
    """

    all_outdoors = Outdoor.query.all()
    activities = []

    for out in all_outdoors:
        activities.append((out.outdoor_id,
                               out.outdoor_activity))

    return ["Favorite Outdoor activity", activities]

def get_user_interests(user_id):
    """ Queries the interests table and accepts a userid as input.
        Returns an object representing one user interest.
    """

    user = Interest.query.filter(Interest.user_id == user_id).first()
    return user


def get_interest_name(interest_id, table_name):
    """ Queries the interest table, accepts interest_id and name of table as
        a parameter. Returns an object of interest type.
    """

    Interest = table_name.query.filter(Interest.user_id == user_id).first()

def get_interest_info(interest_info):
    """ Accepts a SINGLE tuple of INPUT FORMAT: (int, int)
        The first element of the tuple is the value of the interest.
        The second element is the table id.
        Assigns the queries to a small dictionary in this order:
            user.interest_id          |(0)
            user.book_genre_id        |(1)
            user.movie_genre_id       |(2)
            user.music_genre_id       |(3)
            user.food_habit_id        |(4)
            user.fav_cuisine_id       |(5)
            user.hobby_id             |(6)
            user.political_view_id    |(7)
            user.religion_id          |(8)
            user.outdoor_id           |(9)
    """

    common_value = interest_info[0]
    table_id = interest_info[1]

    id_info = { 1 : BookGenre.query.filter(BookGenre.book_genre_id == common_value),
                2 : MovieGenre.query.filter(MovieGenre.movie_genre_id == common_value),
                3 : MusicGenre.query.filter(MusicGenre.music_genre_id == common_value),
                4 : FavCuisine.query.filter(FavCuisine.fav_cuisine_id == common_value),
                5 : Hobby.query.filter(Hobby.hobby_id == common_value),
                6 : Religion.query.filter(Religion.religion_id == common_value),
                7 : Outdoor.query.filter(Outdoor.outdoor_id == common_value) }

    interest_details = id_info[table_id].first()

    return interest_details

def get_user_match(user_id):
    """ Queries the user_matches table and accepts a user id as input.
        Returns a list of confirm matches for the specific user.
    """

    q1 = UserMatch.query
    fil = q1.filter(UserMatch.user_id_2 == 339, UserMatch.user_2_status == False).all()



def find_valid_matches(user_id_1, pincode, query_time):
    """ Queries the pending_match for pending matches.
        returns a list of pending match user user_ids.
    """
    potential_matches = []
    # creates an object from the input date string

    # finding matches for the same query time
    query_time_obj = datetime.datetime.strptime(query_time, "%Y-%m-%d %H:%M:%S")

    # check for all pending_matches
    match_q = PendingMatch.query.filter(PendingMatch.query_pin_code == pincode,
                                        func.date(PendingMatch.query_time) == query_time_obj.date(),
                                        PendingMatch.pending == True)

    users = match_q.all()

    for i in users:
        user_id = i.user_id
        potential_matches.append(user_id)

    return potential_matches
