def student_score():
    while True:
        try:
            n = input("\nEnter the Grade (0 - 100) and I will give you this grade in the USA system.\nNumber = ")
            n = float(n)
            if float(n) == int(n):
                n = int(n)
            if 0 <= n <= 100:
                break
            else:
                print("\nIt isn't a grade (0-100)", end=" ")
        except ValueError:
            print("\nIt isn't a number.", end=" ")
    print(f"\nYour grade: {n} - ", end="")
    if n >= 90:
        return print("A")
    elif n >= 82:
        return print("B")
    elif n >= 75:
        return print("C")
    elif n >= 64:
        return print("D")
    elif n >= 60:
        return print("E")
    else:
        return print("F")
