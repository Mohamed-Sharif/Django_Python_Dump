import random

def play_hangman():
    # List of words to choose from
    words = ["apple", "banana", "orange", "peach", "pear"]

    # Choose a random word from the list
    word = random.choice(words)

    # Create a list of underscores to represent the letters in the word
    progress = ["_"] * len(word)

    # Keep track of the letters that have been guessed
    guessed = []

    # Set the number of allowed incorrect guesses
    attempts = 6

    # Loop until the word is guessed or the player runs out of attempts
    while attempts > 0 and "_" in progress:
        # Print the current progress and list of guessed letters
        print(" ".join(progress))
        print("Guessed letters:", guessed)

        # Get a letter from the player
        guess = input("Guess a letter: ").lower()

        # Check if the letter has already been guessed
        if guess in guessed:
            print("You already guessed that letter.")
        # Check if the letter is in the word
        elif guess in word:
            # Update the progress with the new letter
            for i in range(len(word)):
                if word[i] == guess:
                    progress[i] = guess
            print("Correct!")
        # If the letter is not in the word, decrement the number of attempts
        else:
            attempts -= 1
            print("Incorrect. You have", attempts, "attempts remaining.")

        # Add the letter to the list of guessed letters
        guessed.append(guess)

    # Check if the player won or lost
    if "_" not in progress:
        print("Congratulations, you guessed the word:", word)
    else:
        print("Sorry, you ran out of attempts. The word was:", word)

# Start the game
play_hangman()
