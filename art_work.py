import sqlite3

artwork_db='artwork.sqlite'

class Artist:

    def __init__(self, name, email,id=None):
        self.name = name
        self.email = email
        self.id = id

class Artwork:
    def __init__(self, artist_ID, artwork_name, price, availability):
        self.artist_ID = artist_ID
        self.artwork_name = artwork_name
        self.price = price
        self.availability = availability

def create_table_artist():
    with sqlite3.connect(artwork_db) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS artists (id INTEGER PRIMARY KEY, name TEXT, email TEXT, UNIQUE( name COLLATE NOCASE, email COLLATE NOCASE))')
    conn.close()

def create_table_artwork():
    with sqlite3.connect(artwork_db) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS artworks (artwork_id INTEGER PRIMARY KEY, name TEXT UNIQUE, price INT, available BOOLEAN, artist_id INTEGER, FOREIGN KEY(artist_id) REFERENCES artists(id))')
    conn.close()

"""adds data to the the database
parameters:name, email
"""
def add_artist(artist):
    try:
        with sqlite3.connect(artwork_db) as conn:
            res = conn.execute('INSERT INTO artists (name, email) VALUES (?, ?)', (artist.name, artist.email))
            new_id=res.lastrowid
            artist.id=new_id
        conn.close()
        #return True
    except sqlite3.IntegrityError:
        print('sorry the name already exists')

def check_if_artist_exists(name):
    conn = sqlite3.connect(artwork_db)
    artist_id=conn.execute('SELECT * FROM artists WHERE name LIKE ?', (name, ))
    artist_found=artist_id.fetchone()
    conn.close()

    if artist_found is None:
        return False
    else:
        return artist_found

def check_if_artwork_exists(artwork_name):
    conn = sqlite3.connect(artwork_db)
    search_artworks=conn.execute('SELECT * FROM artworks WHERE name LIKE ?', (artwork_name, ))
    artwork_found=search_artworks.fetchone()
    conn.close()   

    if artwork_found is None:
        return False
    else:
        return artwork_found

def add_artwork(artwork):
    try:
        with sqlite3.connect(artwork_db) as conn:
            conn.execute('INSERT INTO artworks (name, price, available, artist_id) VALUES (?, ?, ?, ?)',
            (artwork.artwork_name, artwork.price, artwork.availability, artwork.artist_ID))
        conn.close()
        #return True
    except sqlite3.IntegrityError:
        print('sorry the name already exists')

def display_artwork(artist_id):
    conn = sqlite3.connect(artwork_db)
    artworks_found = conn.execute('SELECT * FROM artworks WHERE artist_id LIKE ?', (artist_id, ))
    artworks = []
    for artwork in artworks_found:
        artworks.append(artwork)
    conn.close()
    return artworks


def change_availability(availability, artwork_name):
    try:
        with sqlite3.connect(artwork_db) as conn:
            conn.execute('UPDATE artworks SET available = ? WHERE name = ?', (availability, artwork_name))
        conn.close()

    except sqlite3.IntegrityError:
        print('sorry the artwork name does not exists')

def delete_artwork(artwork_name):
    try:
        with sqlite3.connect(artwork_db) as conn:
            conn.execute('DELETE FROM artworks WHERE name = ?', (artwork_name, ))
        conn.close()
    except sqlite3.IntegrityError:
        print('sorry the artwork name does not exists')

