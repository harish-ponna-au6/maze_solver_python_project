# AttainU Python Project

## Project Name : Maze Solver 
## Created By : Harish Ponna


## Maze Solver

```
This program will take input mxn matrix of 0s and 1s(0 denoting walls and 1 denoting path) and give a matrix of same mxn size in output file. 1s will show the shortest path between the start and the destination, and 0s will be the blocked path.
```

**Read me file content:**
-  Files inside mazesolver.
- How to run MazeSolver In Windows Operating System.
- Approach to solve the problem.
- Code Explanation.
- Modules used.
- Conclusion.

## Files inside mazesolver.

Github mazesolver folder consists of 4 contents.

1. README.md

2. maze_solver.py

3. input.txt

3. output.txt

### README.md 
It consists of user manual with contents, instructions and information about the project mazesolver.

### maze_solver.py
It contains the main script of the mazesolver project.

### input.txt
This is an input file which will be used to provide the default condition of the maze, this can be edited by the user.

### output.txt
This file will be the output file in which the maze_solver.py will save the output of the result from given input from input file.

## How to run MazeSolver In Windows OS.

Open the input.txt file and type the desired input in provided format and then save it and close.

`Format for typing the input condition.`

Input should be string of space separated integers, numbers of integers denote n of the matrix and number of lines denote m of the matrix.
Space between each integer is a must.

After you are finished with the typing your input, save the file and close it. Now open command prompt, change your current directory to this mazesolver project folder, and then type the command provided below to execute the mazesolver.py script. In case if you need any help, type 'python mazesolver.py -h or -help' without quotes for command help menu.


## Command line

This program has 1 command with 3 arguments(1 optional).

- python mazesolver.py -i inputfile.txt -o outputfile.txt -d 5,5

### Arguments
1. -i inputfile.txt
    Use this argument to provide the input file which will contain the input typed by you. By default there exist an input.txt file,
    if you want to give your own input file then give the name of your inputfile after --i.

2. -o outputfile.txt
    Use this argument to provide the output file which will contain the output produced by mazesolver.py. By default there exist an 
    output.txt file, if you want output in your own output file then give the name of your outputfile after --o.

3. -d 5,5 (Optional)
    This argument is optional and will take the value of the provided matrix size in the inputfile by default. This defines
    the destination in the maze. If you want to give your own destiantion type 2 integers separated by a comma(the coordinates of
    your destination) after --d. In this example 4,5 means destination is at [4,5] of the matrix with 0 indexing.Don't use any spaces in between integers, only comma and integers allowed.

## Approach to solve the problem.

Backtracking method is used in order to find the smallest path in less time. BFS algo time complexity is higher for the shortest path, hence backtracking method is perfect for this scenario. 

### Code Explanation

**main() function--**

This is the main function which initialises the input and output conditions by asking the user from command prompt and then pass them 
as arguments in the function solvemaze().

**solveMaze() function**

First of, input and output files are opened and stored in the variables, then a sol[] is defined to store the solution(this matrix will 
get modified according to the solution in further functions). After that the next function solveMazeUtil() is called to update the sol[]
and get the result. In the end of this function we wrtie the output file with sol[] and close the files.

**solveMazeUtil() function**

This is the main fucntion which checks and finds the shortest path with the help of a smaller function isSafe() which checks whether the next move is valid or not. And this function updates the sol [ ] recursively accordingly and returns it by assigning the values in it as the 
shortest path.

**isSafe() function**

This function is used to check the validity of next move. Returns true if next move exists else returns false.

## Modules Used

In creation of this python program, following module(s) is/are used:

`argparse` - To get user input in command line

## Conclusion

The project is a bit simpler, so i decided to optimize it further in future.I was thinking of making it bi-directional path finder, by doing the same thing from the destiantion side in reverse order simultaneously, which will result in even more reduced time.

`---THANK YOU---`
