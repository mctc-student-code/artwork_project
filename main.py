import menu
import art_work
from art_work import Artist, Artwork
import ui

def main():
    #call create table which creats tables for artists and artworks if doeesn't exist
    art_work.create_table_artist()
    art_work.create_table_artwork()
    
    #call menu function
    menu.display_menu()

#function that gets artist info and adds it to the database
def add_new_artist():
    try:
        #gets name and email
        new_artist = ui.get_artist_info()
        #checks if name already exits
        artist=art_work.check_if_artist_exists(new_artist.name)

        #if artist doesn't exist add and confirm
        if artist is False:
            art_work.add_artist(new_artist)
            ui.confirmation('successfully added '+ new_artist.name)
        # if it exists error message
        else:
            ui.failed(new_artist.name+ ' has not been added')
    except Exception as e:
        print(e)


#searches and displays all artwork
def search_all_artwork():
    name= ui.verify_name('Enter the name of the artist: ')
    #checks if artist exists
    artist_found = art_work.check_if_artist_exists(name)

    if not artist_found:
        ui.failed('artist not found')
    else:
        artworks = art_work.display_artwork(artist_found[0])    #get all of the artwork
        ui.display_artwork(artworks)    #display them formatted


# get artist name, check if artist exist then display available artworks
def display_available_artwork():
    name= ui.verify_name('Enter the name of the artist: ')
    artist_found = art_work.check_if_artist_exists(name)

    if not artist_found:
        ui.failed('artist not found')
    else:
        artworks = art_work.display_artwork(artist_found[0])
        for art in artworks:
            if art[3]==0:
                artworks.remove(art)
        ui.display_artwork(artworks)

# addes new artwork
def add_new_artwork():
    artwork , artist = ui.get_artwork_info()
    artist_found = art_work.check_if_artist_exists(artist)
    try:
        if not artist_found:
            ui.failed('artist does not exist')
        else:
            new_artwork = Artwork(artist_found[0], artwork.artwork_name, artwork.price, artwork.availability)
            check_artwork = art_work.check_if_artwork_exists(artwork.artwork_name)
            if check_artwork is False:
                art_work.add_artwork(new_artwork)
                ui.confirmation('successfully added '+ artwork.artwork_name)
            else:
                ui.failed(artwork.artwork_name + ' has not been added')
    except Exception as e:
        print(e)

#deletes artwork if it exists
def delete_artwork():
    name= ui.verify_name('enter the name of the artwork: ')
    artwork_found = art_work.check_if_artwork_exists(name)

    if not artwork_found:
        ui.failed('artist not found')
    else:
        y_n=ui.verify('are you sure you want to delete ' + name)
        if y_n is True:
            art_work.delete_artwork(name)
            ui.confirmation('successfully deleted '+name)
        else:
            ui.confirmation('Deletion canceled.')



#checks if artwork exists then changes it to either sold or available
def update_artwork():
    try:
        name= ui.verify_name('enter the name of the artwork: ')
        artwork_found = art_work.check_if_artwork_exists(name)

        if not artwork_found:
            ui.failed('artist not found')
        else:
            if artwork_found[3]==0:
                art_work.change_availability(1,name)
                ui.confirmation('successfully updated to Available')
            else:
                art_work.change_availability(0,name)
                ui.confirmation('successfully updated to Sold')
    except Exception:
        ui.failed('artwork doesn\'t exist')


if __name__ =='__main__':
    main()