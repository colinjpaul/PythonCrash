from collections import OrderedDict

glossary = OrderedDict()

glossary['a_forloop'] = 'allows you to iterate through a series of variables'
glossary['a_dictionary'] = 'stores key value pairs'
glossary['a_list'] = 'homogeneous sequences'
glossary['a_variable'] = 'store a particular value in memory'
glossary['an_if_else_statement'] = 'conditional logic'
glossary['sorted'] = 'sorts output in alphabetical order'

for k,v in glossary.items():
    print(k, v, '\n')