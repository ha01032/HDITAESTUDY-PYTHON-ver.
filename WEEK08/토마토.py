# https://www.acmicpc.net/problem/7576

#토마토
import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().strip().split())

tomato = [[] for _ in range(N)]

#입력
for y in range(N):
    tomato[y] = list(map(int, input().strip().split()))

    
ripeTime = [[0]*M for _ in range(N)] #안익었으면, -1 
q = deque([])    

#초기화 및 총 토마토 개수 구하기
tomatoNum=0
ripeNum=0
for y in range(N):
    for x in range(M):
        if(tomato[y][x] >=0): tomatoNum+=1
        if(tomato[y][x] == 1):
            q.append((y,x))
            ripeTime[y][x] = 0 # 처음부터 익어있음. 
            ripeNum+=1

#처음부터 다 익어있으면, 0 출력
if (ripeNum == tomatoNum):
    print(0)

#처음부터 다 안익어있으면, 시간에 따라 인접한 것들 영향주는 BFS 시작
else:            
    #bfs 준비
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]    

    def inBox(y,x):
        return 0<=y and y<N and 0<=x and x<M
    while q:
        #bfs 시작    
        y,x = q.popleft()
        currTime = ripeTime[y][x]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if inBox(ny, nx) and tomato[ny][nx] == 0: #해당위치의 토마토가 존재하고 안 익었으면,
                q.append((ny,nx))
                ripeTime[ny][nx] = currTime+1
                tomato[ny][nx] = 1
                ripeNum+=1
    
    #만약 모든 토마토가 익었으면 시간 출력, 다 안익었으면 -1출력
    print(currTime) if ripeNum == tomatoNum else print(-1)
