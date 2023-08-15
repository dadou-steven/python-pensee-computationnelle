def fact_iter(n):
    """

    :param n:
    :return:
    """
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer


print(fact_iter(3))

# https://github.com/dadou-steven/mathematical/blob/main/src/main/java/appsinc/fr/lesmaths/FactorielIter.java
