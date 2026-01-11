USE blu_ray_collection;

INSERT INTO genres (genre_name) VALUES
('Action'),
('Drama'),
('Sci-Fi'),
('Horror');

INSERT INTO formats (format_name) VALUES
('Blu-ray'),
('4K UHD');

INSERT INTO distributors (distributor_name) VALUES
('Criterion Collection'),
('Vinegar Syndrome'),
('Arrow Video'),
('Umbrella Entertainment');

INSERT INTO boutique_distributor
(distributor_id, boutique_label_name, notes)
VALUES
(1, 'The Criterion Collection', 'High-quality restorations and Preservation'),
(2, 'Vinegar Syndrome', 'Restoration and Preservation of genre films'),
(3, 'Arrow Video', 'Restoring Cult Classics'),
(4, 'Umbrella Entertainment', 'Distributing Cult Cinema');

INSERT INTO movies (
    title,
    release_date,
    genre_ref,
    director,
    lead_actor,
    format_ref,
    distributor_ref,
    region_code,
    date_added,
    watched,
    notes
) VALUES (
    'Road House',
    '1989-05-19',
    1, -- Action
    'Rowdy Herrington',
    'Patrick Swayze',
    2, -- 4K UHD
    3, -- Arrow Video
    'B',
    CURRENT_DATE,
    FALSE,
    'Arrow Video Limited Edition'
);

INSERT INTO movies (
    title,
    release_date,
    genre_ref,
    director,
    lead_actor,
    format_ref,
    distributor_ref,
    region_code,
    date_added,
    watched,
    notes
) VALUES (
    'The Keep',
    '1983-12-16',
    3, -- Sci-Fi
    'Michael Mann',
    'Scott Glenn',
    2, -- 4K UHD
    2, -- Arrow Video
    'All',
    CURRENT_DATE,
    FALSE,
    'Vinegar Syndrome Limited Edition 4K UHD'
);