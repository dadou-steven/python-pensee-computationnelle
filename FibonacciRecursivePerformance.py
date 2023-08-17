def fastFib(n, memo={}):
    """

    :param n:
    :param memo:
    :return:
    """
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n - 1, memo) + fastFib(n - 2, memo)
        memo[n] = result
        return result


for i in range(101):
    print("fastFib(" + str(i) + ") =", fastFib(i))
