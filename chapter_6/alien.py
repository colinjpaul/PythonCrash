alien_0 = {'colour': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0['colour'] = 'yellow'
print("alien colour is now " + alien_0['colour'])

alien_0['speed'] = 'fast'

print("original x-position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print("new position: " + str(alien_0['x_position']))

del(alien_0['points'])
print(alien_0)



