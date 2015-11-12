__author__ = 'zhangfuqiang'

# Dictionaries are not sequences at all, but are instead known as mappings.
# Mapping s are also collection of other objects, but they store objects by key instead of relative position.


def mapping_operations():  # Mapping operations
    d = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
    print(d['food'])
    d['quantity'] += 1
    print(d)
    #
    e = {}
    e['name'] = 'Bob'
    e['job'] = 'dev'
    e['age'] = 40
    print(e)


def nesting_revisited():  # nested revisited
    rec = {'name': {'first': 'Bob', 'last': 'Smith'},
           'job': ['dev', 'mgr'],
           'age': 40.5}
    print(rec)
    print(rec['name'])
    print(rec['name']['first'])
    for j in rec['job']:
        print(j)
    rec['job'].append('janitor')
    print(rec)


# mapping_operations()
nesting_revisited()
