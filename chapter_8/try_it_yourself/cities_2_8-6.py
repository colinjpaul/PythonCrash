def city_country(city, country):
    where_am_i = city + ',' + ' ' + country
    return where_am_i


location_1 = city_country('Cork', 'Ireland')
location_2 = city_country('Liverpool', 'England')
location_3 = city_country('Boston', 'US')

print(location_1)
print(location_2)
print(location_3)