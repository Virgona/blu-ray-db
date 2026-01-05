import mysql.connector          # MySQL database driver
from dotenv import load_dotenv  # Loads variables from .env file
import os                       # Lets us access environment variables


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

def add_movie():
    print("Add a new movie to the database\n")

    title = input("Movie Title: ")
    director = input("Director: ")
    release_year = input("Release Year: ")
    distributor_ref = input("Distributor ID: ")

    # We use try / except / finally to safely handle errors
    # and guarantee the database connection closes properly.

    connection = None
    cursor = None

    try:
            connection = get_db_connection()
            cursor = connection.cursor()

            # --- Query for SQL ---
            sql = """
                INSERT INTO movies (title, director, release_year, distributor_ref)
                VALUES (%s, %s, %s, %s)
            """
            values = (title, director, release_year, distributor_ref)

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