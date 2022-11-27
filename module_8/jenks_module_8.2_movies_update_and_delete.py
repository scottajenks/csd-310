# Scott Jenks
# Module 8.2 - Movies: Update & Deletes
# 11/25/2022

# https://github.com/scottajenks/csd-310.git

import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'root',
    'password': 'P!aybill!985',
    'host': 'localhost',
    'database': 'movies',
    'raise_on_warnings': True
}
try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(
        config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue...\n")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)

cursor = db.cursor()


def show_films(cursor, title):
    cursor.execute("SELECT film.film_name as Name, film.film_director as Director, "
                   "genre.genre_name as Genre, studio.studio_name as 'Studio Name' "
                   "from film "
                   "INNER JOIN genre ON film.genre_id=genre.genre_id "
                   "INNER JOIN studio ON film.studio_id=studio.studio_id")

    films = cursor.fetchall()

    print("\n  -- {} --".format(title))

    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0],
                                                                                         film[1],
                                                                                         film[2],
                                                                                         film[3]))


def update_movies(cursor):
    new_movie = "INSERT INTO film(film_name, film_releaseDate, film_runtime, film_director, " \
                "studio_id, genre_id) " \
                "VALUES ('Titanic', 1997, 195, 'James Cameron', (SELECT studio_id FROM studio " \
                "WHERE studio_name = '20th Century Fox'), (SELECT genre_id FROM genre WHERE " \
                "genre_name = 'Drama'))"

    # Executing the SQL command
    cursor.execute(new_movie)
    # Commit you changes in the database
    db.commit()

def update_genre(cursor):
    new_genre = "UPDATE film SET film_id = 2, genre_id = 1 WHERE genre_id = 2"

    # Executing the SQL command
    cursor.execute(new_genre)
    # Commit you changes in the database
    db.commit()

def delete_movie(cursor):
    delete_movie = "DELETE FROM film WHERE film_name = 'Gladiator'"

    # Executing the SQL command
    cursor.execute(delete_movie)
    # Commit you changes in the database
    db.commit()


show_films(cursor, "DISPLAYING FILMS")
update_movies(cursor)
show_films(cursor, "DISPLAYING FILMS AFTER INSERT")
update_genre(cursor)
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")
delete_movie(cursor)
show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

db.close()

close = input("Press Enter to Close.")
