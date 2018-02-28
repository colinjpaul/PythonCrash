def show_magicians(magician_list):
    for magician in magician_list:
        print(magician)


def make_great(magician_list):
    for magician in magician_list:
        magician += " the Great"


magicians = ['mick', 'john', 'tom']
show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)


