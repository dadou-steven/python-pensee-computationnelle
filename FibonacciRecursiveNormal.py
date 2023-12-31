def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for i in range(101):
    print("fib(" + str(i) + ") =", fib(i))

# Slow mode in Java :
# https://github.com/dadou-steven/mathematical/blob/main/src/main/java/appsinc/fr/lesmaths/FibonacciRecursiveNormal.java
# Fast mode in Python :
# https://github.com/dadou-steven/python-pensee-computationnelle/blob/main/FibonacciRecursivePerformance.py
