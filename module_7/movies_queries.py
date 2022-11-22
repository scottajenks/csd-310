#Scott Jenks
#Module 7.2 - Movies: Table Queries
#11/21/2022

#https://github.com/scottajenks/csd-310.git

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

print("-- DISPLAYING Studio RECORDS --")

cursor = db.cursor()

query1 = "SELECT studio_id, studio_name FROM studio"

cursor.execute(query1)

studios = cursor.fetchall()

for studio in studios:
    print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

print("\n-- DISPLAYING Genre RECORDS --")

cursor = db.cursor()

query2 = "SELECT genre_id, genre_name FROM genre"

cursor.execute(query2)

genres = cursor.fetchall()

for genre in genres:
    print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

print("\n-- DISPLAYING Short Film RECORDS --")

cursor = db.cursor()

query3 = "SELECT film_name, film_runtime FROM film"

cursor.execute(query3)

films = cursor.fetchall()

for film in films:
    if film[1] < 120:
        print("Film Name: {}\nRuntime: {}\n".format(film[0], film[1]))

print("\n-- DISPLAYING Director RECORDS in Order --")

cursor = db.cursor()

query4 = "SELECT film_name, film_director FROM film ORDER BY film_releaseDate DESC"

cursor.execute(query4)

directors = cursor.fetchall()

for director in directors:
    print("Film Name: {}\nDirector: {}\n".format(director[0], director[1]))

db.close()

close = input("Press Enter to Close.")



