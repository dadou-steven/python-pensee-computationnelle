def fact_recur(n):
    """

    :param n:
    :return:
    """
    if n <= 1:
        return 1  # cas de base
    else:
        return n * fact_recur(n - 1)  # étape recursive


print(fact_recur(3))

# https://github.com/dadou-steven/mathematical/blob/main/src/main/java/appsinc/fr/lesmaths/FactorielRecur.java
