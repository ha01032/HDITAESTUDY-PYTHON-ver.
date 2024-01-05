# https://www.acmicpc.net/problem/10026

#적록색약
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N= int(input().strip())

picture = [[]* N for _ in range(N)]

for i in range(N):
    picture[i] = list(input().strip())

normVisited = [[0]* N for _ in range(N)]
weakVisited = [[0]* N for _ in range(N)]

dy = [1,-1,0,0]
dx = [0,0,1,-1]


def normDfs(y,x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny and ny<N and 0<=nx and nx<N and not normVisited[ny][nx]:
            if picture[ny][nx]==currColor:
                normVisited[ny][nx] = 1
                normDfs(ny,nx)
                
def weakDfs(y,x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny and ny<N and 0<=nx and nx<N and not weakVisited[ny][nx]:
            if currColor == 'B':
                if picture[ny][nx]=='B':
                    weakVisited[ny][nx] = 1
                    weakDfs(ny,nx)   

            else:
                if picture[ny][nx]!='B':
                    weakVisited[ny][nx] = 1
                    weakDfs(ny,nx)   

normCount = 0
weakCount = 0
currColor = ""
#적록색약 없는 경우
for y in range(N):
    for x in range(N):
        currColor = picture[y][x]
        if not normVisited[y][x]:
            normDfs(y,x)        
            normCount+=1
        if not weakVisited[y][x]:
            weakDfs(y,x)
            weakCount+=1
            
print(normCount, end=" ")
print(weakCount)
