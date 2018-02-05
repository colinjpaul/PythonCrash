favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

friends = ['phil', 'jack', 'sarah', 'tom']


for friend in friends:
    if friend in favorite_languages.keys():
        print(friend.title() + ' thanks for taking part in the pool')
    else:
        print(friend.title() + ' please take part in the poll')


for name in favorite_languages:
    if name in friends:
        print('Hi ' + name.title() + '. I see your favourite language is ' + favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!')

for language in favorite_languages.values():
    print(language.title() + ' is here')

for language in set(favorite_languages.values()):
    print(language.title() + ' listed only once')