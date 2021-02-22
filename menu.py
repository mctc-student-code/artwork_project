import main

def display_menu():
    print ("""
    1: ADD new artist
    2: SEARCH all artwork by artist
    3: DISPLAY avalable artwork by artist
    4: ADD new artwork
    5: DELETE artwork
    6: CHANGE availability of the artwork
    Q/q: QUITE
   """)

    while True:
        option=input('Please enter your option: ')

        if option=='1':
            main.add_new_artist()


        elif option=='2':
            main.search_all_artwork()

        elif option=='3':
            main.display_available_artwork()

        elif option=='4':
            main.add_new_artwork()


        elif option=='5':
            main.delete_artwork()


        elif option=='6':
            main.update_artwork()

        elif option=='':
            print('Empty input please try again')
            continue

        elif option[0].lower() =='q':
            print('bye')
            break

