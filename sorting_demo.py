import sys
import random
import subprocess
from timeit import default_timer as timer
from sorting_algorithms import *

def ask_length():
    print("Start by giving the length of the array you want to sort.")
    print("You can choose any number between 1 and 10,000,000.")
    print("Spaces or commas can be used as thousands separators.")
    print("\nType \"quit\" to exit the program.\n")
    while True:
        length = input("Length: ").replace(" ","").replace(",","")
        if length == "quit":
            print("Bye!")
            sys.exit()
        else:
            try:
                length = int(length)
            except ValueError:
                print("Oops that's not an integer!\n")
                continue
            if length <= 0:
                print("Very funny...\n")
                continue
            elif length > 10000000:
                print("Trust me you don't want to go past ten million\n")
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
    print("3 - Randomized order")
    print("\nYou can type \"back\" to go back.\n")
    while True:
        choice = input("Enter the number of your choice: ")
        if choice == "back":
            return None
        elif choice == "1":
            print("\nGenerating the array...", end='')
            return [x for x in range(length)]
        elif choice == "2":
            print("\nGenerating the array...", end='')
            return [length - x for x in range(length)]
        elif choice == "3":
            print("\nGenerating the array...", end='')
            return [random.randint(1, 1000) for i in range(length)]
        else:
            print("There's no such option!\n")

def ask_sorting():
    print("\rChoose which sorting algorithm to use:\n")
    print("1 - Insertion Sort")
    print("2 - Merge Sort")
    print("3 - Quicksort")
    print("4 - Heapsort")
    print("\nYou can type \"back\" to go back to start.")
    print("\nFor lengths >100 000, insertion sort will be extremely inefficient.")
    print("If the sorting starts to take too long, CTRL-C is your friend.\n")
    while True:
        choice = input("Enter the number of your choice: ")
        if choice == "back":
            return None
        elif choice == "1":
            return InsertionSort()
        elif choice == "2":
            return MergeSort()
        elif choice == "3":
            return QuickSort()
        elif choice == "4":
            return HeapSort()
        else:
            print("There's no such option!\n")

if __name__ == "__main__":
    print("\n--- Sorting Algorithm Demo ---\n")
    while True:
        length = ask_length()
        array = generate_array(length)
        if not array:
            continue
        sorter = ask_sorting()
        if not sorter:
            continue
        break
    print("")
    animation = subprocess.Popen("./sorting_animation.sh")
    start_time = timer()
    sorter.sort(array)
    end_time = timer()
    animation.kill()
    subprocess.run(["stty", "echo"]) # Show input in terminal
    subprocess.run(["tput", "cvvis"]) # Make the cursor visible
    duration = end_time - start_time
    print(("\rSorting an array size of {:,} using {}"
           " took {:.3f} seconds\n").format(length,
                                            sorter.name,
                                            duration))
