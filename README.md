# Sorting Algorithm Demo
This is a small Python program that demonstrates runtimes of common sorting algorithms. I used this project mainly to teach myself how different sorting algorithms work and how they differ. 
***
**For Windows users:** Because the program includes bash commands, it will crash if run on Windows. If you wish to run it on a Windows machine, open the `sorting_demo.py` file and remove all the lines that use the subprocess module (lines 95, 99, 100, 101, 108, 109). This will prevent an animation from running during the sorting process.

![GIF missing](https://raw.githubusercontent.com/vrompasa/sorting-demo/master/sorting.gif)
***
## How does it work?
To start the program, run the `sorting_demo.py` file.

First, the program asks the length of the array the user wants to sort. I limited the length to ten million because for larger values, generating the array takes too long to be practical.

Then, the user is asked in which order the array should be:
- **Ascending order** - elements are in ascending order `[0, 1, 2, ... length-2, length-1]`
- **Descending order** - elements are in descending order `[length-1, length-2, length-3, ... 1, 0]`
- **Randomized order** - the array consists of `length` number of elements between 0 to 999 in random order

Finally, the user decides which of the following sorting algorithm to use:
- **Insertion Sort**
- **Merge Sort**
- **Quick Sort**
- **Heap Sort**

After the algorithm finishes, the program gives the time it took to sort the array and exits.
