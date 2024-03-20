from Task1 import positive_zero_negative
from Task2 import even_odd
from Task3 import day_of_the_week
from Task4 import student_score
from Task5 import smart_parrot
from Task6 import find_the_word
from Task7 import find_the_capital
from Task8 import tournament
from Task9 import factorial_with_recursion
from Task10 import recursive_reverse_without_arrays_and_cycles


def main():
    while True:
        print("\nMenu:")
        print("\t 0. Exit;")
        print("\t 1. Task 1: \"Positive/Zero/Negative\";")
        print("\t 2. Task 2: \"Even/Odd\";")
        print("\t 3. Task 3: \"Day of the Week\";")
        print("\t 4. Task 4: \"Student Score\";")
        print("\t 5. Task 5: \"Smart Parrot\";")
        print("\t 6. Task 6: \"Find the Word\";")
        print("\t 7. Task 7: \"Find the Capital\";")
        print("\t 8. Task 8: \"Tournament\";")
        print("\t 9. Task 9: \"Factorial with recursion\";")
        print("\t10. Task 10: \"Recursive reverse without arrays and cycles\".")
        while True:
            try:
                menu = input("\nEnter menu item: ")
                menu = int(menu)
                if 0 <= int(menu) <= 10:
                    if menu == 0:
                        print("\nExit...\n\n")
                        return 0
                    elif menu == 1:
                        positive_zero_negative()
                        break
                    elif menu == 2:
                        even_odd()
                        break
                    elif menu == 3:
                        day_of_the_week()
                        break
                    elif menu == 4:
                        student_score()
                        break
                    elif menu == 5:
                        smart_parrot()
                        break
                    elif menu == 6:
                        find_the_word()
                        break
                    elif menu == 7:
                        find_the_capital()
                        break
                    elif menu == 8:
                        tournament()
                        break
                    elif menu == 9:
                        factorial_with_recursion()
                        break
                    elif menu == 10:
                        recursive_reverse_without_arrays_and_cycles()
                        break
                else:
                    print("\nIt isn't a valid menu item.")
            except ValueError:
                print("\nIt isn't a valid menu item.")


main()
