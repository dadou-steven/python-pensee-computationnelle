# En Python, le résultat est affiché pendant environ 21042 secondes ou 6 heures.
# In Python, the result is displayed for approximately 21042 seconds or 6 hours.

# En Java, le résultat est affiché pendant environ 2738 secondes ou 46 minutes.
# In Java, the result is displayed for approximately 2738 seconds or 46 minutes.

import random
from time import time

from cffi.backend_ctypes import xrange

n = 4096

A = [[random.random()
      for row in xrange(n)]
     for col in xrange(n)]
B = [[random.random()
      for row in xrange(n)]
     for col in xrange(n)]
C = [[0 for row in xrange(n)]
     for col in xrange(n)]

start = time()
for i in xrange(n):
    for j in xrange(n):
        for k in xrange(n):
            C[i][j] += A[i][k] * B[k][j]
end = time()

print('%0.6f' % (end - start))

