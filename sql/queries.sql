-- Movies by Distributor

SELECT
    d.distributor_name,
    m.title,
    m.release_date,
    f.format_name,
    g.genre_name,
    m.region_code,
    m.last_watched
FROM movies m
JOIN distributors d ON m.distributor_ref = d.distributor_id
JOIN formats f ON m.format_ref = f.format_id
JOIN genres g ON m.genre_ref = g.genre_id
ORDER BY d.distributor_name, m.title;

-- List of Directors

SELECT DISTINCT director
FROM movies
ORDER BY director;

-- Number of movies per distributor

SELECT
    d.distributor_name,
    COUNT(*) AS movie_count
FROM movies m
JOIN distributors d ON m.distributor_ref = d.distributor_id
GROUP BY d.distributor_name
ORDER BY movie_count DESC;

-- All 4K UHD movies
SELECT
    m.title,
    d.distributor_name,
    g.genre_name,
    m.release_date
FROM movies m
JOIN formats f ON m.format_ref = f.format_id
JOIN distributors d ON m.distributor_ref = d.distributor_id
JOIN genres g ON m.genre_ref = g.genre_id
WHERE f.format_name = '4K UHD'
ORDER BY m.title;

-- Movies by director
SELECT
    director,
    title,
    release_date,
    d.distributor_name,
    f.format_name
FROM movies m
JOIN distributors d ON m.distributor_ref = d.distributor_id
JOIN formats f ON m.format_ref = f.format_id
ORDER BY director, release_date;