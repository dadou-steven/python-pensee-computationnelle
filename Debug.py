def isPal(x):
    assert type(x) == list
    temp = x
    print(temp, x)
    temp.reverse()
    print(temp, x)
    if temp == x:
        return True
    else:
        return False


def silly(n):
    result = []
    for i in range(n):
        elem = input("Entrer un élément : ")
        result.append(elem)
    print(result)
    if isPal(result):
        print('Oui')
    else:
        print('Non')


print(silly(2))
