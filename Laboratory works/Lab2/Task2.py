def even_odd():
    while True:
        try:
            n = input("\nEnter the number, and I will tell you if it's even or odd.\nNumber = ")
            n = float(n)
            if float(n) == int(n):
                n = int(n)
            break
        except ValueError:
            print("\nIt isn't a number.", end=" ")
    if n % 2 == 0:
        return print(f"{n} is an even number.")
    else:
        return print(f"{n} is an odd number.")
