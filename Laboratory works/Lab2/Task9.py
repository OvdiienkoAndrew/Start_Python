def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)


def factorial_with_recursion():
    print("You can enter a natural number, and I will give you the factorial of that number.")
    while True:
        try:
            n = input("Number = ")
            n = int(n)
            break
        except ValueError:
            print("\nIt isn't an integer.")
    return print(f"{n}! = {factorial(n)}")
