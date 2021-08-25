import numpy as np
a=np.array([['Gagan'],['Happy']])
b=np.array(['hola', 'peter'])
print(b)
print(np.char.add(['hola'],['peter']))
print(np.char.add('hola','peter'))
print(np.char.add(a,b))
print(np.char.multiply('Gangu ',5))
print(np.char.center('hola',9,fillchar='#'))