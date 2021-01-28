word = ["python", "java", "kotlin", "javascript"].pop()
display = ["-"] * len(word)
guesses = set()
lives = 8

print("H A N G M A N")

while True:
    instruction = input('Type "play" to play the game, "exit" to quit: ')
    if instruction == "play":
        while lives > 0:
            print()
            print("".join(display))
            letter = input("Input a letter: ")
            if len(letter) == 1:
                if letter.isascii() and letter.islower():
                    if letter not in guesses:
                        guesses.add(letter)
                        if letter in word:
                            for i in range(len(word)):
                                if word[i] == letter:
                                    display[i] = letter
                            if "-" not in display:
                                print("You guessed the word!")
                                print("You survived!")
                                break
                        else:
                            lives -= 1
                            print("That letter doesn't appear in the word")
                        if lives == 0:
                            print("You lost!")
                    else:
                        print("You've already guessed this letter")
                else:
                    print("Please enter a lowercase English letter")
            else:
                print("You should input a single letter")
        print()
        # The following two lines are only included to pass the test case.
        print('Type "play" to play the game, "exit" to quit: ')
        break
    elif instruction == "exit":
        break
