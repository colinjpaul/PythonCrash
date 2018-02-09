cities = {
    'cork': {
        'country': 'ireland',
        'population': '119,230',
        'fact': 'capital of the rebel county',
    },
    'boston': {
        'country': 'usa',
        'population': '673,184',
        'fact': 'home of the red sox'
    },
    'liverpool': {
        'country': 'england',
        'population': '465,700',
        'fact': 'home of the five time european champions',
    },
}

for city, info in cities.items():
    print('some information on ' + city),
    print(str(('is located in ') + info['country']))
    print(str(('population ') + info['population']))
    print(str(('did you know? ') + info['fact']))

    # for k, v in city.items():
    #     print(k, v)
