from datetime import date
import mysql.connector

from db import get_db_connection
from cli_helper import prompt_int, choose_from_list
from lookups import get_distributors, get_formats, get_genres


def add_movie():
    connection = None
    cursor = None

    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        print("\n=== Add a Movie ===")

        title = input("Title: ").strip()
        release_year = prompt_int("Release Year (YYYY): ")
        director = input("Director: ").strip()
        lead_actor = input("Lead Actor: ").strip()
        region_code = input("Region Code (A/B/C): ").strip().upper()

        # Choose genre / format / distributor from DB lists
        genres = get_genres(cursor)
        chosen_genre = choose_from_list(genres, "Genres", label_fn=lambda r: r[1])
        genre_ref = chosen_genre[0]

        formats = get_formats(cursor)
        chosen_format = choose_from_list(formats, "Formats", label_fn=lambda r: r[1])
        format_ref = chosen_format[0]

        distributors = get_distributors(cursor)
        chosen_distributor = choose_from_list(
            distributors,
            "Distributors",
            label_fn=lambda r: f"{r[1]} ({r[2]})"
        )
        distributor_ref = chosen_distributor[0]

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
        print("\n❌ Database error:", err)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


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
        rows = cursor.fetchall()

        print("\n=== All Movies ===")
        if not rows:
            print("(no movies yet)")
            return

        for title, year, distributor in rows:
            print(f"{title} ({year}) — {distributor}")

    except mysql.connector.Error as err:
        print("\n❌ Database error:", err)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def list_boutique_movies():
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
            WHERE d.distributor_type = 'BOUTIQUE'
            ORDER BY d.distributor_name, m.title;
        """

        cursor.execute(query)
        rows = cursor.fetchall()

        print("\n=== Boutique Movies ===")
        if not rows:
            print("(no boutique movies yet)")
            return

        for title, year, distributor in rows:
            print(f"{title} ({year}) — {distributor}")

    except mysql.connector.Error as err:
        print("\n❌ Database error:", err)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()