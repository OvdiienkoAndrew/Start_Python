def enter(n):
    if n > 0:
        while True:
            try:
                a = input("Enter: ")
                a = int(a)
                break
            except ValueError:
                print("\nIt isn't a valid integer. Please enter a valid integer.")
        n -= 1
        enter(n)
        print(a, end=' ')


def recursive_reverse_without_arrays_and_cycles():
    print("Enter an integer, and I will give you its reverse sequence.")
    while True:
        try:
            n = int(input("Enter the number of elements: "))
            if n > 0:
                break
        except ValueError:
            print("\nIt isn't a valid number of elements.")
    if n == 1:
        print(f"You can enter {n} element, and I will give you its reverse.")
    else:
        print(f"You can enter {n} elements, and I will give you their reverse.")
    enter(n)
