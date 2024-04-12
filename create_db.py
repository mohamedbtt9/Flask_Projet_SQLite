import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO livres (titre, auteur, année_publication, genre) VALUES (?, ?, ?, ?)",
            ('Titre du livre 1', 'Auteur du livre 1', 2020, 'Genre 1'))
cur.execute("INSERT INTO livres (titre, auteur, année_publication, genre) VALUES (?, ?, ?, ?)",
            ('Titre du livre 2', 'Auteur du livre 2', 2018, 'Genre 2'))
cur.execute("INSERT INTO livres (titre, auteur, année_publication, genre) VALUES (?, ?, ?, ?)",
            ('Titre du livre 3', 'Auteur du livre 3', 2015, 'Genre 1'))
cur.execute("INSERT INTO livres (titre, auteur, année_publication, genre) VALUES (?, ?, ?, ?)",
            ('Titre du livre 4', 'Auteur du livre 4', 2019, 'Genre 3'))
cur.execute("INSERT INTO livres (titre, auteur, année_publication, genre) VALUES (?, ?, ?, ?)",
            ('Titre du livre 5', 'Auteur du livre 5', 2021, 'Genre 2'))

connection.commit()
connection.close()
