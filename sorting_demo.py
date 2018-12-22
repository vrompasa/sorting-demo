import sys
import random
import subprocess
from timeit import default_timer as timer
from sorting_algorithms import *

def ask_length():
    length = 0
    print("Give the length of the to be sorted array. You can choose any number between 1 and 1,000,000")
    print("Type \"quit\" to exit the program.")
    while True:
        length = input("Length: ").replace(" ","")
        if length == "quit":
            print("Bye bye!")
            sys.exit()
        else:
            try:
                length = int(length)
            except ValueError:
                print("Oops that's not a number!")
                continue
            if length <= 0:
                print("Very funny...")
                continue
            elif length > 1000000:
                print("Trust me, you don't want to go past a million")
                continue
            return length

def ask_array():
    numbers = input("Give the to be sorted numbers separated by a comma: ")
    array = numbers.split(",")
    return list(map(int, array)) # Convert the string values to ints

def generate_array(length):
    print("\nIn which order do you want the array to be?\n")
    print("1 - Ascending order")
    print("2 - Descending order")
    print("3 - Random order")
    print("You can type \"back\" to go back.")
    while True:
        choice = input("Enter the number of your choice: ")
        if choice == "back":
            break
        elif choice == "1":
            return [x for x in range(length)]
        elif choice == "2":
            return [length - x for x in range(length)]
        elif choice == "3":
            return [random.randint(1, 1000) for i in range(length)]
        else:
            print("Not a valid input")

def ask_sorting():
    print("\nChoose which sorting algorithm to use:\n")
    print("1 - Insertion Sort")
    print("2 - Merge Sort")
    print("3 - Quicksort")
    print("You can type \"back\" to go back.")
    while True:
        choice = input("Enter the number of your choice: ")
        if choice == "back":
            break
        elif choice == "1":
            return InsertionSort()
        elif choice == "2":
            return MergeSort()
        elif choice == "3":
            return QuickSort()
        else:
            print("Not a valid input")

if __name__ == "__main__":
    print("\n--- Sorting Algorithm Demo ---\n")
    length = ask_length()
    array = generate_array(length)
    sorter = ask_sorting()
    print("")
    animation = subprocess.Popen("./sorting_animation.sh")
    start_time = timer()
    sorter.sort(array)
    end_time = timer()
    animation.kill()
    subprocess.run(["stty", "echo"]) # Enable input in terminal
    subprocess.run(["tput", "cvvis"]) # Make the cursor visible
    duration = end_time - start_time
    print(("\r\b\rSorting an array size of {:,} using {}"
           " took {:.3f} seconds\n").format(length,
                                            sorter.name,
                                            duration))
