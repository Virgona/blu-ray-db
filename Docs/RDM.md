# Blu-ray Collection Database – RDM

## Movies
- movie_id (PK)
- title
- release_date
- genre_ref (FK → genres.genre_id)
- director
- lead_actor
- format_ref (FK → formats.format_id)
- distributor_ref (FK → distributors.distributor_id)
- region_code
- date_added
- last_watched
- watched
- notes

## Genres
- genre_id (PK)
- genre_name (UNIQUE)

## Formats
- format_id (PK)
- format_name (UNIQUE)

## Distributors
- distributor_id (PK)
- distributor_name (UNIQUE)