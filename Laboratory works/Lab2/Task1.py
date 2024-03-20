def positive_zero_negative():
    while True:
        try:
            n = input("\nEnter the number, and I will tell you its orientation.\nNumber = ")
            n = float(n)
            if float(n) == int(n):
                n = int(n)
            break
        except ValueError:
            print("\nIt isn't a number.", end=" ")
    if n < 0:
        return print(f"Number = {n}. It is a negative number.")
    if n == 0:
        return print(f"Number = {n}. It is zero number.")
    else:
        return print(f"Number = {n}. It is a positive number.")
