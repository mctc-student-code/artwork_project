from art_work import Artist, Artwork

def get_artist_info():
    name=verify_name('Enter artist name: ')
    email=verify_email('what is '+ name+'\'s Email: ')

    return Artist(name, email)


def get_artwork_info():
    name=verify_name('enter the artist name: ')
    artwork_name=verify_name('Enter the name of the artwork: ')
    price=verify_price('Enter the price of the artwork: ')
    availability=verify_availability('is the artwork available or sold: ')

    return Artwork(None, artwork_name, price, availability), name

def verify_price(ask_price):
    while True:
        try:
            price = int(input(ask_price))
            if price >= 1:
                return price
            else:
                print('price must be greater than 1')
        except ValueError:
            print('PLease enter valid input')

def verify_name(ask_name):
    while True:
            name =input(ask_name)
            if isinstance(name, str) == True:
                return name
            else:
                print('name must be string')
        #except ValueError:
        #    print('PLease enter valid input')

def verify_email(ask_email):
    while True:
            email =input(ask_email)
            if '@' in email:
                return email
            else:
                print('not valid email')

def verify_availability(ask_if_available):
    while True:
        available =input(ask_if_available)
        if available[0].lower() == 's':
            return False
        else:
            return True

def confirmation(name_or_message):
        stars='*'*len(name_or_message)
        print(stars)
        print(name_or_message)
        print(stars)

def display_artwork(artworks):
    availability = ''

    print('\n{:<20s} {:<20s} {:<20s} {:<20s}\n'.format('Artwork ID', 'Artwork name', 'Price', 'availability'))
    for artwork in artworks:
        if artwork[3]==0:
            availability = 'SOLD'
        else:
            availability = 'AVAILABLE'
        #print(artwork)
        print(f'{artwork[0]:<20} {artwork[1]:<20} ${artwork[2]:<20} {availability:<20}')
