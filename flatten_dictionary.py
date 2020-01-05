import collections

import collections

def flatten(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        try:
            items.extend(flatten(v, '%s%s%s' % (parent_key, k,sep)).items())
        except AttributeError:
            items.append(('%s%s' % (parent_key, k), v))
    return dict(items)

# a = {'foo': {'bar':'yo'}}
print("="*20)
a = {'a': 1, 'c': {'a': 2, 'b': {'x': 5, 'y' : 10}}, 'd': [1, 2, 3]}
print(a)
b = flatten(a)
print(b)
print("="*20)
