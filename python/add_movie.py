import mysql.connector          # MySQL database driver
from dotenv import load_dotenv  # Loads variables from .env file
import os                       # Lets us access environment variables
from datetime import date


# --------------------------------------------------
# Load environment variables from the .env file
# --------------------------------------------------
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

print("Host:", DB_HOST)
print("User:", DB_USER)
print("Password present:", bool(DB_PASSWORD))
print("Database:", DB_NAME)


# --------------------------------------------------
# Database connection helper
# --------------------------------------------------
def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )


# --------------------------------------------------
# Fetch distributors (STANDARD + BOUTIQUE only)
# --------------------------------------------------
def get_distributors(cursor):
    query = """
        SELECT distributor_id, distributor_name, distributor_type
        FROM distributors
        WHERE distributor_type = 'BOUTIQUE'
           OR distributor_name = 'STANDARD'
        ORDER BY distributor_type DESC, distributor_name;
    """
    cursor.execute(query)
    return cursor.fetchall()


# --------------------------------------------------
# Add a movie
# --------------------------------------------------
def add_movie():
    connection = None
    cursor = None

    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        print("\nAdd a new movie to the database\n")

        title = input("Title: ")
        release_year = int(input("Release Year (YYYY): "))
        genre_ref = int(input("Genre ID: "))
        director = input("Director: ")
        lead_actor = input("Lead Actor: ")
        format_ref = int(input("Format ID: "))
        region_code = input("Region Code (A/B/C): ").upper()

        # --- Distributor selection ---
        distributors = get_distributors(cursor)

        print("\nAvailable Distributors:")
        for idx, d in enumerate(distributors, start=1):
            print(f"{idx}) {d[1]} ({d[2]})")

        choice = int(input("\nChoose distributor number: "))
        distributor_ref = distributors[choice - 1][0]

        sql = """
            INSERT INTO movies
            (
                title,
                release_year,
                genre_ref,
                director,
                lead_actor,
                format_ref,
                distributor_ref,
                region_code,
                date_added
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            title,
            release_year,
            genre_ref,
            director,
            lead_actor,
            format_ref,
            distributor_ref,
            region_code,
            date.today()
        )

        cursor.execute(sql, values)
        connection.commit()

        print("\n✅ Movie added successfully!")

    except mysql.connector.Error as err:
        print("❌ Database error:", err)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

#--- displays all movies currently in the database ---#

def list_movies():
    connection = None
    cursor = None

    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        query = """
            SELECT
                m.title,
                m.release_year,
                d.distributor_name
            FROM movies m
            JOIN distributors d ON m.distributor_ref = d.distributor_id
            ORDER BY m.title;
        """

        cursor.execute(query)
        movies = cursor.fetchall()

        print("\n=== All Movies ===")
        if not movies:
            print("(no movies yet)")
            return

        for title, year, distributor in movies:
            print(f"{title} ({year}) — {distributor}")

    except mysql.connector.Error as err:
        print("Database error:", err)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

#-- Basic menu for a user to operate db --#
def main_menu():
    while True:
        print("\n=== Blu-ray Collection ===")
        print("1) Add a movie")
        print("2) List all movies")
        print("3) Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_movie()

        elif choice == "2":
            list_movies()

        elif choice == "3":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()