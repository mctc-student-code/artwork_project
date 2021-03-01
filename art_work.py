import sqlite3

artwork_db = 'artwork.sqlite'

class Artist:
    def __init__(self, name, email, id=None):
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


def add_artist(artist):
    """
    adds artist to the the database and generates ID.  Indicates error if artist name or email are duplicates.
    parameters: artist - an artist object
    """

    try:
        with sqlite3.connect(artwork_db) as conn:
            res = conn.execute('INSERT INTO artists (name, email) VALUES (?, ?)', (artist.name, artist.email))
            new_id = res.lastrowid
            artist.id = new_id
        conn.close()
    except sqlite3.IntegrityError:
        print('sorry the name already exists') 

        
def check_if_artist_exists(name):
    """checks if artist in the databse
    parameters:artist name
    returns: a tuple of artist information, if an artist with the given name is in the database. False otherwise
    """
    conn = sqlite3.connect(artwork_db)
    results = conn.execute('SELECT * FROM artists WHERE name LIKE ?', (name, ))
    artist_found = results.fetchone()
    conn.close()

    if artist_found is None:
        return False
    else:
        return artist_found

    
"""checks if artwork in the database
parameters:artwork name
"""
def check_if_artwork_exists(artwork_name):
    conn = sqlite3.connect(artwork_db)
    search_artworks=conn.execute('SELECT * FROM artworks WHERE name LIKE ?', (artwork_name, ))
    artwork_found=search_artworks.fetchone()
    conn.close()   

    if artwork_found is None:
        return False
    else:
        return artwork_found

"""adds artwork to the the database
parameters:artwork list with artist ID
"""
def add_artwork(artwork):
    try:
        with sqlite3.connect(artwork_db) as conn:
            conn.execute('INSERT INTO artworks (name, price, available, artist_id) VALUES (?, ?, ?, ?)',
            (artwork.artwork_name, artwork.price, artwork.availability, artwork.artist_ID))
        conn.close()
    except sqlite3.IntegrityError:
        print('sorry the name already exists')

"""gets all artwork from the database
parameters:artist's ID
"""
def display_artwork(artist_id):
    conn = sqlite3.connect(artwork_db)
    artworks_found = conn.execute('SELECT * FROM artworks WHERE artist_id LIKE ?', (artist_id, ))
    artworks = []
    for artwork in artworks_found:
        artworks.append(artwork)
    conn.close()
    return artworks

"""updates wether artwork is sold or available 
parameters: availability and artwork name
"""
def change_availability(availability, artwork_name):
    try:
        with sqlite3.connect(artwork_db) as conn:
            conn.execute('UPDATE artworks SET available = ? WHERE name = ?', (availability, artwork_name))
        conn.close()

    except sqlite3.IntegrityError:
        print('sorry the artwork name does not exists')

"""deletes artwork from database
parameters:artwork name
"""
def delete_artwork(artwork_name):
    try:
        with sqlite3.connect(artwork_db) as conn:
            conn.execute('DELETE FROM artworks WHERE name = ?', (artwork_name, ))
        conn.close()
    except sqlite3.IntegrityError:
        print('sorry the artwork name does not exists')

