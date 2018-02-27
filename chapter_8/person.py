def build_person(first_name, last_name, age=''):
    '''Return a dictionary of information about a person'''
    person = {'First Name': first_name, 'Last Name': last_name}
    if age:
        person['Age'] = age
    return(person)

musician = build_person('jimi', 'hendrix', age=27)
print(musician)