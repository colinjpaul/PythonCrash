def show_magicians(magician_list):
    for magician in magician_list:
        print(magician)


def make_great(magician_list, great_magician_list):
    while magician_list:
        great_magician = magician_list.pop()
        great_magician_list.append(great_magician + ' the Great')


magicians = ['mick', 'john', 'tom']
great_magicians = []

show_magicians(magicians)
make_great(magicians, great_magicians)
show_magicians(magicians)
show_magicians(great_magicians)


