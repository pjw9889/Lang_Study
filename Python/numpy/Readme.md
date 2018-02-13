# Numpy Study



## 1. What is Numpy?



Library for scientific computers used in Python



## 2.  Operation method



import numpy as np



A = np.array)([[1,2],[3,4]])



### Arithmetic operation

print (A ** 2)

print (A * A)



print(np.dot(x,y))

print(x * y)



### logical operation

np.logical_or()

np.logical_and()



### Reductions operation

a = np.array([1,2,3,4,5])



a.sum()

a.min()

a.max()



a.argmin()

a.argmax()



#### logical Reductions

a = np.array([True, True, True])

np.all(a)

np.any(a)



#### Statistical Reductions

x = np.array([1,2,3,1])



np.mean(x)

np.median(x)

np.std(x) // Standard Deviation