DROP TABLE IF EXISTS livres;

CREATE TABLE livres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    titre TEXT NOT NULL,
    auteur TEXT NOT NULL,
    année_publication INTEGER NOT NULL,
    genre TEXT NOT NULL
);
