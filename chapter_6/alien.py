alien_0 = {'colour': 'green', 'points': 5}
alien_1 = {'colour': 'yellow', 'points': 10}
alien_2 = {'colour': 'red', 'points': 15}

aliens = []

for alien in range(30):
    new_alien = {'colour': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)


print("total number of aliens > " + str(len(aliens)))

for alien in aliens[0:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['colour'] == 'yellow':
        alien['colour'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
#
# for alien in aliens:
#     print(alien)
#
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)
#
# alien_0['colour'] = 'yellow'
# print("alien colour is now " + alien_0['colour'])
#
# alien_0['speed'] = 'fast'
#
# print("original x-position: " + str(alien_0['x_position']))
#
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
#
# alien_0['x_position'] = alien_0['x_position'] + x_increment
#
# print("new position: " + str(alien_0['x_position']))
#
# del(alien_0['points'])
# print(alien_0)
#



