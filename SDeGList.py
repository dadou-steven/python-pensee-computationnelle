# Séquence de grêlon, list. En java array ou tableau.

a = []
i = 0
n = 3
while n != 1:
    print(n)
    i += i
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3 * n + 1
print(n)
