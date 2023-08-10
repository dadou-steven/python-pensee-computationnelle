print("Pensez à un nombre entrre 0 et 100 !")

hi = 100
lo = 0
guessed = False

while not guessed:
    guess = (hi + lo) // 2
    print("Votre numéro secret est ", guess, "?")
    user_inp = input("Saississez 'h' pour indiquer que le résultat est trop élevé. Entrer 'l' pour indiquer que la "
                     "réponse est trop basse. Entrez 'C' pour "
                     "indiquer que j'ai déviné correctement :")
    if user_inp == 'c':
        guessed = True
    elif user_inp == 'h':
        hi = guess
    elif user_inp == 'l':
        lo = guess
    else:
        print("Désolé, je n'ai pas compris votre contribution.")

print("La partie est términéee. Votre numéro sécret était : ", guess)
