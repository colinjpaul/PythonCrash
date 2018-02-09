favourite_places = {
    'colin': ['cork', 'liverpool', 'boston'],
    'edel': ['cork', 'boston'],
    'luke': ['boston']
}

for person, place in favourite_places.items():
    if len(place) <= 1:
        print(person + "'s favourite place is ")
    else:
        print(person + "'s favourite places are ")
    for location in place:
        print(location)
