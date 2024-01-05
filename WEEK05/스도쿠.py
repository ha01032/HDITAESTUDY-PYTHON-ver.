# https://www.acmicpc.net/problem/2580
# pypy3로 품..

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

sudoku = [[0] * 9  for _ in range(9)]

for i in range(9):
    sudoku[i] = list(map(int,input().strip().split()))



blankY = []
blankX = []

for y in range(9):
    for x in range(9):
        if sudoku[y][x]==0:
            blankY += [y]
            blankX += [x]


blankLen = len(blankY)


def sudokuDFS(n):
    global sudoku
    if n == blankLen:
        for w in sudoku:
            for i in range(9):
                print(w[i], end=" ")
            print()
        exit(0)
    y=blankY[n]
    x=blankX[n]
    boxH = y - (y%3)
    boxW = x - (x%3)
    for i in range(1,10):
        if checkLine(i,y,x) and checkBox(i, boxH, boxW):
            sudoku[y][x] = i
            sudokuDFS(n+1)
            sudoku[y][x] = 0




def checkLine(value, y, x):
    global sudoku
    if value in sudoku[y]: return False
    for i in range(9):
        if sudoku[i][x] == value : return False
    return True

def checkBox(value, boxH, boxW):
    global sudoku
    for i in range(boxH, boxH+3):
        for j in range(boxW, boxW+3):
            if sudoku[i][j] == value : return False
    return True



sudokuDFS(0)
