def getWordScore(word, n):
    """

    :param word:
    :param n:
    :return:
    """
    score = 0
    SCRABBLE_LETTER_VALUES = {"a": 1, "b": 4}
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]
    score *= len(word)
    if len(word) == n:
        score += 50
    return score


print(getWordScore("babab", 1))
