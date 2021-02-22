import menu
import art_work
from art_work import Artist, Artwork
import ui

def main():
    art_work.create_table_artist()
    art_work.create_table_artwork()

    menu.display_menu()


def add_new_artist():
    try:
        new_artist = ui.get_artist_info()
        art_work.add_artist(new_artist)
        ui.confirmation('successfully added '+ new_artist.name)
    except Exception as e:
        print(e)

def search_all_artwork():
    name= ui.verify_name('Enter the name of the artist: ')
    artist_found = art_work.check_if_artist_exists(name)

    if not artist_found:
        print('artist not found')
    else:
        artworks = art_work.display_artwork(artist_found[0])
        ui.display_artwork(artworks)

def display_available_artwork():
    name= ui.verify_name('Enter the name of the artist: ')
    artist_found = art_work.check_if_artist_exists(name)

    if not artist_found:
        print('artist not found')
    else:
        artworks = art_work.display_artwork(artist_found[0])
        for art in artworks:
            if art[3]==0:
                artworks.remove(art)
        ui.display_artwork(artworks)

def add_new_artwork():
    artwork , artist = ui.get_artwork_info()
    artist_found = art_work.check_if_artist_exists(artist)
    try:
        if not artist_found:
            print('artist does not exist')
        else:
            new_artwork = Artwork(artist_found[0], artwork.artwork_name, artwork.price, artwork.availability)
            art_work.add_artwork(new_artwork)
            ui.confirmation('successfully added '+ artwork.artwork_name)
    except Exception as e:
        print(e)

def delete_artwork():
    name= ui.verify_name('enter the name of the artwork: ')
    artwork_found = art_work.check_if_artwork_exists(name)

    if not artwork_found:
        print('artist not found')
    else:
        art_work.delete_artwork(name)
        ui.confirmation('successfully deleted '+name)

def update_artwork():
    try:
        name= ui.verify_name('enter the name of the artwork: ')
        artwork_found = art_work.check_if_artwork_exists(name)

        if not artwork_found:
            print('artist not found')
        else:
            if artwork_found[3]==0:
                art_work.change_availability(1,name)
                ui.confirmation('successfully updated to Available')
            else:
                art_work.change_availability(0,name)
                ui.confirmation('successfully updated to Sold')
    except Exception:
        print('artwork doesn\'t exist')


if __name__ =='__main__':
    main()