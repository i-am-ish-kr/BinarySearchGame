low = 1
high = 1000
print("please think of a number between {0} and {1}".format(low, high))
input("press ENTER to start")
guesses = 1
while True:
    guess = low + (high - low) // 2
    high_low = input("My guess is {}, please enter h, l, c ".format(guess)).casefold()

    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print("I guessed it in {} guesses".format(guesses))
        break
    guesses = guesses + 1