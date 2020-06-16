import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', default='input.txt', type=str,
                        help='To provide input file, input.txt by default.')
    parser.add_argument('-o', default='output.txt', type=str,
                        help='To provide output file, output.txt by default.')
    parser.add_argument('-d', default=0, type=str,
                        help='To give manual destination a,b by default.')
    args = parser.parse_args()
    sys.stdout.write(str(solveMaze(args)))


m = 0
n = 0
D = [0, 0]


# to check the validity of next move
def isSafe(maze, x, y):
    if x >= 0 and x < m and y >= 0 and y < n and maze[x][y] == 1:
        return True
    return False


# To store the input,output and destination in variables
def solveMaze(args):
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
    n = len(maze[0])
    if dest == 0:
        D = [m-1, n-1]
    else:
        dest = dest.split(',')
        D = [int(dest[0]), int(dest[1])]

    ifile.close()
    sol = [[0 for j in range(n)] for i in range(m)]

    if not solveMazeUtil(maze, 0, 0, sol):
        output_file = args.o
        ofile = open(output_file, 'w')
        ofile.write('-1')
        ofile.close()
        print("Solution doesn't exist")
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
def solveMazeUtil(maze, x, y, sol):

    if x == D[0] and y == D[1] and maze[x][y] == 1:
        sol[x][y] = 1
        return True

    if isSafe(maze, x, y):
        sol[x][y] = 1
        if solveMazeUtil(maze, x + 1, y, sol):
            return True
        if solveMazeUtil(maze, x, y + 1, sol):
            return True
        sol[x][y] = 0
        return False


# This is the main function to execute the script
if __name__ == "__main__":
    main()
