# https://www.acmicpc.net/problem/12851
import sys
from collections import deque

input = sys.stdin.readline


N,K = map(int,input().strip().split())
maxSpot = max(N,K)*2


minTime = abs(N-K)
cnt = 0

#bfs시작
deq = deque([])
visited = [False] * (maxSpot+1)
deq.append((N, 0))
while(deq):
    currSpot, currTime = deq.popleft()
    #만약 현재 위치가 K와 같으면 더이상 BFS진행안함
    if currSpot == K: 
        if currTime < minTime:
            minTime = currTime
        if currTime == minTime:
            cnt+=1
        if currTime > minTime:
            break
    visited[currSpot] = True
    for i in range(3):
        nextSpot = currSpot+1 if i==0 else currSpot-1 if i==1 else currSpot*2
        if 0<=nextSpot and nextSpot <=maxSpot and not visited[nextSpot]:
            deq.append((nextSpot, currTime+1))
print(minTime)
print(cnt)       
