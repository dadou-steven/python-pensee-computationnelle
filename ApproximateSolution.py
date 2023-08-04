# cube root

cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.01
num_guesses = 0

while abs(guess ** 3 - cube) >= epsilon:
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess ** 3 - cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)


# square root

x = 25
low = 1.0
high = x
ans = (high + low) / 2.0
print("")

while abs(ans ** 2 - x) >= epsilon:
    print('low = ', low, "high = ", high, "ans = ", ans)
    num_guesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print("numGuesses = ", num_guesses)
print(ans, "is close to square root of", x)
