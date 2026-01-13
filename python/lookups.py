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


def get_formats(cursor):
    query = """
        SELECT format_id, format_name
        FROM formats
        ORDER BY format_name;
    """
    cursor.execute(query)
    return cursor.fetchall()


def get_genres(cursor):
    query = """
        SELECT genre_id, genre_name
        FROM genres
        ORDER BY genre_name;
    """
    cursor.execute(query)
    return cursor.fetchall()