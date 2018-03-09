def build_profile(first, last, **user_info):
    '''Build a dictionary containing everything we know about a user'''

    profile = {}
    profile['first_name'] = first
    profile['last name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('Colin', 'Paul',
                             location='Glanmire',
                             interests='Loads of stuff',
                             favourite_team='Liverpool')


print(user_profile)
