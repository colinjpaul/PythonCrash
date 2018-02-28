def make_album(artist, title, number_of_tracks=''):
    if number_of_tracks:
        album = {'Artist': artist,
                'Album': title,
                'Number of Tracks': number_of_tracks}
    else:
        album = {'Artist': artist,
                 'Album': title}
    return album


while True:
    artist_name = input("\n Please input the Artist's name ('q' to quit)")
    if artist_name == 'q':
        break
    album_title = input("\n Please input the Album title ('q' to quit)")
    if album_title == 'q':
        break

    album_details = make_album(artist_name, album_title)
    print(album_details)









