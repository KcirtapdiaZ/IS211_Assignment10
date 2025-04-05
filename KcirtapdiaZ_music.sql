CREATE TABLE artists (
    artist_id INTEGER PRIMARY KEY,
    artist_name TEXT NOT NULL
);

CREATE TABLE albums (
    album_id INTEGER PRIMARY KEY,
    album_name TEXT NOT NULL,
    artist_id INTEGER,
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
);

CREATE TABLE songs (
    song_id INTEGER PRIMARY KEY,
    song_name TEXT NOT NULL,
    album_id INTEGER,
    track_number INTEGER,
    duration_seconds INTEGER,
    FOREIGN KEY (album_id) REFERENCES albums(album_id)
);

