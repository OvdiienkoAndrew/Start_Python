def find_the_word():
    words = ["I", "You", "We", "They", "He", "She", "It", "Everybody", "Nobody", "am", "is", "are"]
    print("\nI will provide you with a list. You will enter a word. If this word is in the list,", end="")
    print("I will write it and give you the index (or position) of this word.")
    print("Otherwise, I will say that the list doesn't have this word.")
    while True:
        try:
            a = input("If you want to see words when I know, enter 'y'; if you don't want, enter 'n': ")
            if a.lower() == 'y' or a.lower() == 'n':
                break
        except ValueError:
            print("It isn't a valid input.")
    if a.lower() == 'y':
        print("\nList:")
        for i, word in enumerate(words, start=1):
            print(f"{i}. {word}", end="")
            if i == len(words):
                print(".")
            else:
                print(";")
    word = input("\nEnter a word: ")
    for i, words2 in enumerate(words, start=1):
        if word.lower() == words2.lower():
            return print(f"\nThe list contains this word.\nThe word \"{word}\" has index {i}.")
    return print("\nThe list doesn't contain this word.")
