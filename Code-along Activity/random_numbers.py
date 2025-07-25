import random

def append_random_numbers(numbers_list, quantity=1):
    """Appends 'quantity' random integers (1-100) to numbers_list."""
    for _ in range(quantity):
        num = random.randint(1, 100)
        numbers_list.append(num)

def append_random_words(words_list, quantity=1):
    """Appends 'quantity' random words from predefined choices to words_list."""
    word_choices = ["sun", "moon", "cloud", "rain", "star", "sky", "comet", "planet"]
    for _ in range(quantity):
        word = random.choice(word_choices)
        words_list.append(word)

def main():
    # Working with random numbers
    numbers = []
    append_random_numbers(numbers)           # Appends 1 random number
    append_random_numbers(numbers, 3)        # Appends 3 more random numbers
    print("Random Numbers:")
    print(numbers)

    # Working with random words
    words = []
    append_random_words(words)               # Appends 1 random word
    append_random_words(words, 4)            # Appends 4 more random words
    print("\nRandom Words:")
    print(words)

    # ✨ Fun Enhancement: Pair random words with numbers!
    paired = list(zip(words, numbers[:len(words)]))
    print("\nWord-Number Pairs:")
    for word, num in paired:
        print(f"{word} → {num}")

# Ensures the program only runs when executed directly
if __name__ == "__main__":
    main()