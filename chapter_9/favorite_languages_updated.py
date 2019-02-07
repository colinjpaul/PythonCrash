'''From Chapter 6 but updated to included OrderedDict()'''

from collections import OrderedDict

favorite_language = OrderedDict()

favorite_language['jen'] = 'python'
favorite_language['sarah'] = 'c'
favorite_language['edward'] = 'ruby'
favorite_language['phil'] = 'python'

for name, language in favorite_language.items():
    print("\n" + name.title() + "'s favourite language is " + language.title() + ".")