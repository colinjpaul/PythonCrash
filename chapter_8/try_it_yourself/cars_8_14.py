def make_car(manufacturer, model_name, **extra_info):

    car = {}
    car['Make'] = manufacturer
    car['Model'] = model_name
    for key, value in extra_info.items():
        car[key] = value
    return car


my_car = make_car('Skoda', 'Suberb',
                  colour='Gray',
                  tow_package=False,
                  size='massive')
print(my_car)



