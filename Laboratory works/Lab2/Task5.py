def smart_parrot():
    words = {"Bye", "Good bye", "Have a nice day", "Farewell", "See you later"}
    print("\nEnter a line of text. If you want to finish, enter one of the farewell phrases:")
    for i, word in enumerate(words, start=1):
        print(f"- {word}", end="")
        if len(words) == i:
            print(".")
        else:
            print(";")
    while True:
        text = input("\nEnter the text, and the parrot will copy this text.\nText = ")
        if text.lower() in (word.lower() for word in words):
            print("When suddenly, we fell apart.")
            break
        else:
            print(text)
