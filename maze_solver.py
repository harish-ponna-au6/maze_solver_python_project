import argparse
import sys
import os


def initialization():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', default='input.txt', type=str,
                        help='To provide input file, input.txt by default.')
    parser.add_argument('-o', default='output.txt', type=str,
                        help='To provide output file, output.txt by default.')
    parser.add_argument('-d', default=0, type=str,
                        help='To give manual destination a,b by default.')

    args = parser.parse_args()

    # Checking whether input file exist or not
    if not os.path.exists(args.i):
        return print("The file does not exist!")

    sys.stdout.write(str(solve_maze(args)))


m = 0
n = 0
D = [0, 0]


# To store the input,output and destination in variables
def solve_maze(args):
    output_file = args.o
    ofile = open(output_file, 'w')
    ofile.write("")
    input_file = args.i
    ifile = open(input_file, 'r')
    lines = ifile.readlines()
    maze = []
    for i in lines:
        maze.append(list(map(int, i.strip().split(' '))))
    dest = args.d
    global m
    global n
    global D
    m = len(maze)
    if m == 0:
        return 'Given input file has no matrix'
    for i in range(1, len(maze)):
        if(len(maze[0]) != len(maze[i])):
            return 'Given input file has no matrix'
    n = len(maze[0])
    if dest == 0:
        D = [m-1, n-1]
    else:
        dest = dest.split(',')
        D = [int(dest[0]), int(dest[1])]

    ifile.close()
    sol = [[0 for j in range(n)] for i in range(m)]

    if not solve_maze_util(maze, 0, 0, sol):
        output_file = args.o
        ofile = open(output_file, 'w')
        ofile.write('-1')
        ofile.close()
        print("Solution doesn't exist for the maze")
        return False

    output_file = args.o
    ofile = open(output_file, 'a')
    for i in sol:
        b = list(map(str, i))
        b.append('\n')
        ofile.write(' '.join(b))
    ofile.close()
    return True


#  to find shortest path with the help of a smaller function isSafe()
def solve_maze_util(maze, x, y, sol):
    if x == D[0] and y == D[1] and maze[x][y] == 1:
        sol[x][y] = 1
        return True

    if isSafe(maze, x, y):
        sol[x][y] = 1
        if solve_maze_util(maze, x + 1, y, sol):
            return True
        if solve_maze_util(maze, x, y + 1, sol):
            return True
        sol[x][y] = 0
        return False


# to check the validity of next move
def isSafe(maze, x, y):
    if x >= 0 and x < m and y >= 0 and y < n and maze[x][y] == 1:
        return True
    return False


initialization()
