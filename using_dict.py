# a dict is a non-ordinal mutable collection of any data as key:value pairs

bbc = {'founder':'Reith', 'obj':{'inform', 'educate', 'entertain'}, 'age':83}
# we may iterate over a dict like this
for (k,v) in bbc.items():
    print(f'{k} contains {v}')