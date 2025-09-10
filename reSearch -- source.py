import matplotlib
matplotlib.use("TkAgg")
import time
from random import randint
from lab import CircularDeque
from matplotlib import pyplot as plt

dq = CircularDeque((10 ** 5), True)
numbers = [randint(-(10**3), 10**3) for _ in range((10 ** 5) * 15)]
marks = [10**x for x in range(1, 4)] + [x * (10 ** 4) for x in range(1, 10)] + [x * (10 ** 5) for x in range(1, 15)]

pfront = []
pback = []
for i, el in enumerate(numbers):
    if i in marks:
        start = time.time()
        dq.push_front(el)
        st = time.time() - start
        pfront.append(st)
        start = time.time()
        dq.push_back(el)
        st = time.time() - start
        pback.append(st)
    else:
        dq.push_front(el)

plt.plot(marks, pfront, "r-", label="push_front")
plt.plot(marks, pback, "b-", label="push_back")
plt.ylabel('execution time')
plt.xlabel('amount of elements')
plt.ylim(2 * 10**(-12), 9 * 10**(-6))
plt.axhline(y=3 * (10**(-6)), color='r', linestyle='--', label="O(1)")
plt.legend()
plt.show()