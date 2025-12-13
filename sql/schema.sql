CREATE DATABASE IF NOT EXISTS blu_ray_collection;
USE blu_ray_collection;

CREATE TABLE genres (
    genre_id INT AUTO_INCREMENT PRIMARY KEY,
    genre_name VARCHAR(50) NOT NULL,
    UNIQUE KEY (genre_name)
);

CREATE TABLE formats (
    format_id INT AUTO_INCREMENT PRIMARY KEY,
    format_name VARCHAR(10) NOT NULL,
    UNIQUE KEY (format_name)
);

CREATE TABLE distributors (
    distributor_id INT AUTO_INCREMENT PRIMARY KEY,
    distributor_name VARCHAR(100) NOT NULL,
    UNIQUE KEY (distributor_name)
);

CREATE TABLE movies (
    movie_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    release_date DATE NOT NULL,
    genre_ref INT NOT NULL,
    director VARCHAR(50) NOT NULL,
    lead_actor VARCHAR(50) NOT NULL,
    format_ref INT NOT NULL,
    distributor_ref INT NOT NULL,
    region_code VARCHAR(3) NOT NULL,
    date_added DATE NOT NULL,
    last_watched DATE,
    watched BOOLEAN DEFAULT FALSE,
    notes TEXT,
    FOREIGN KEY (genre_ref) REFERENCES genres(genre_id),
    FOREIGN KEY (format_ref) REFERENCES formats(format_id),
    FOREIGN KEY (distributor_ref) REFERENCES distributors(distributor_id)
);
