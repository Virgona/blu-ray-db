import mysql.connector          # MySQL database driver
from dotenv import load_dotenv  # Loads variables from .env file
import os                       # Lets us access environment variables
from datetime import date


# --------------------------------------------------
# Load environment variables from the .env file
# (This keeps credentials OUT of the code and GitHub)
# --------------------------------------------------
load_dotenv()

# mapping .env values into Python variables
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

print("Host:", DB_HOST)
print("User:", DB_USER)
print("Password present:", bool(DB_PASSWORD))
print("Database:", DB_NAME)

def get_db_connection():                    #--- Connects to the database using credentials stored in the env ---#
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

#-- helper function to get all of the distributors from the db for a list later --#
def get_distributors(cursor):
     query = """
        SELECT distributor_id, distributor_name, distributor_type
        FROM distributors
        ORDER BY distributor_type DESC, distributor_name;
        """
     cursor.execute(query)
     return cursor.fetchall()

def add_movie():
    print("Add a new movie to the database\n")

    title = input("Title: ")
    release_year = input("Release Year (YYYY): ")
    genre_ref = input("Genre ID: ")
    director = input("Director: ")
    lead_actor = input("Lead Actor: ")
    format_ref = input("Format ID: ")
    distributor_ref = input("Distributor ID: ")
    region_code = input("Region Code (e.g., A/B/C): ")

    # adding date of entry
    date_added = date.today()
    # We use try / except / finally to safely handle errors
    # and guarantee the database connection closes properly.

    connection = None
    cursor = None

    try:
            connection = get_db_connection()
            cursor = connection.cursor()

            # --- Query for SQL ---
            sql = """
            INSERT INTO movies
            (title, release_year, genre_ref, director, lead_actor,
             format_ref, distributor_ref, region_code, date_added)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
            values = ( 
            title,
            int(release_year),
            int(genre_ref),
            director,
            lead_actor,
            int(format_ref),
            int(distributor_ref),
            region_code,
            date_added
            )

            cursor.execute(sql, values)
            connection.commit()   # <- Saves the insert permanently

            print("Movie added successfully!")

    except mysql.connector.Error as err:
        print("Database error:", err)

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    add_movie()
# --------------------------------------------------
# This ensures the script only runs when executed
# directly (not when imported by another script)
# --------------------------------------------------