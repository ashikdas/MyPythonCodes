# add two dictionary

D = {'a': 100, 'b': 200}
E = {'c': 300, 'd':400}

new_idc = D.copy()
new_idc.update(E)
print(new_idc)