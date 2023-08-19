functions = []
for i in range(5):
    def func(x):
        return x + i


    functions.append(func)

for f in functions:
    print(f(12))

print(i)
print()


x1 = [1, 2, 3, 4, 5]
print("X           : ", x1)
x1.insert(1, 8)
print("Insert      : ", x1)
x1.append(8)
print("Append      : ", x1)
x1.extend([6, 7])
print("Extend      : ", x1)
x1.append([8, 9])
print("Append list : ", x1)
x1.pop(9)
print("Pop         : ", x1)
x1.remove(8)
print("Remove      : ", x1)
print()


def quad_eval(a, b, c, v):
    """

    :param a:
    :param b:
    :param c:
    :param v:
    :return:
    """
    term1 = a * v ** 2
    term2 = b * v
    return term1 + term2 + c


print(quad_eval(7, 8, 9, 3))
