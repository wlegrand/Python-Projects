import random
import math

L = 5
K = 1000000
N1 = 0
N2 = 0

for n in range(K):
    x = random.random()
    y = random.random()

    d2 = (x-L/2)**2 + (y - L/2)**2
    d = math.sqrt(d2)

    if d < L/2:
        N1 = N1+1
    else:
        N2 = N2+1


print("N1 = ", N1)
print("N2 = ", N2)
pp = 4*N1/K
print("pi =", pp)


ca = pp*(L/2**2)

print("air of the circle = ", ca)
