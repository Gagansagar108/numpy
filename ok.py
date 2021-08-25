import numpy as np
a=np.arange(1,21)
b=a.reshape(4,5)
print(b)
c=b.flatten()
print(c)
d=b.flatten(order='f')
print(d)
e=b.ravel(order='c')
print(e)
print(b.T)
z=c.reshape(4,5)
print(z)
print(np.vsplit(z,2))
print(np.concatenate((a,c)))
print(np.concatenate((a,c),axis=0))



