import numpy as np
#vectorization in numpy
a=np.arange(1,6)#performing mathematical operation on entire array without using any loop is called vectorization
print(a)#advantages of vectorization are 1)Improved Performance, 2)Simplified Syntax, 3)Parallelization Opportunities, 4)Enhanced Memory Efficiency , 5)Avoidance of Explicit Loops 
b=a+5
print(b)
c=a+b
print(c)
d=a/b
print(d)


import numpy as np
import time

start = time.time()

array1 = np.arange(100000)

result = array1 + 10

end = time.time()

print("Vectorization time:", end - start)
