import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', default='input.txt', type=str, help='This command is used to provide input file, input.txt by default.')
    parser.add_argument('-o', default='output.txt', type=str, help='This command is used to provide output file, output.txt by default.')
    parser.add_argument('-d', default=[-1,-1], type=list, help='This command is used to give manual destination, [N][N] by default.')
    args = parser.parse_args()
    sys.stdout.write(str(solve_maze(args)))


N = 0
def print_solution(sol):
    for i in sol:
        for j in i:
            print(str(j) + " ", end="")
        print("")


def is_safe(maze, x, y):

    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
        return True

    return False


def solve_maze(args):
    output_file = args.o
    ofile = open(output_file, 'w')
    ofile.write("")
    input_file = args.i
    ifile = open(input_file, 'r')
    lines = ifile.readlines()
    maze = []
    for i in lines:
        maze.append(list(map(int, i.split(' '))))
    global N

    N = len(maze)
    ifile.close()
    sol = [[0 for j in range(len(maze))] for i in range(len(maze))]

    if solve_maze_util(maze, 0, 0, sol) == False:
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


def solve_maze_util(maze, x, y, sol):

    if x == N - 1 and y == N - 1 and maze[x][y] == 1:
        sol[x][y] = 1
        return True

    if is_safe(maze, x, y) == True:
        sol[x][y] = 1
        if solve_maze_util(maze, x + 1, y, sol) == True:
            return True
        if solve_maze_util(maze, x, y + 1, sol) == True:
            return True
        sol[x][y] = 0
        return False


if __name__ == "__main__":
    main()
