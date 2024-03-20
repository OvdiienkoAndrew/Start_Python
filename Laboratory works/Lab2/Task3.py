def day_of_the_week():
    while True:
        try:
            n = input("\nEnter the number (1-7) and I will tell you the name of the day.\nNumber = ")
            n = int(n)
            if 0 < n < 8:
                break
            else:
                print("\nIt isn't a number (1-7)", end=" ")
        except ValueError:
            print("\nIt isn't a natural number.", end=" ")
    if n == 1:
        return print("First day is Monday.")
    if n == 2:
        return print("Second day is Tuesday.")
    if n == 3:
        return print("Third day is Wednesday.")
    if n == 4:
        return print("Fourth day is Thursday.")
    if n == 5:
        return print("Fifth day is Friday.")
    if n == 6:
        return print("Sixth day is Saturday.")
    else:
        return print("Seventh day is Sunday.")
