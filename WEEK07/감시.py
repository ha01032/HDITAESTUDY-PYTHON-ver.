# https://www.acmicpc.net/problem/15683

#감시
import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit = 10**8

N,M = map(int,input().strip().split())

office = [[0]*M for _ in range(N)]
for i in range(N):
    office[i] = list(map(int,input().strip().split()))

    
def cctvAction(y,x,n,t,v):
    global office
    if n==0:
        for k in range(y-1,-1,-1):
            if office[k][x] == 6: break
            if office[k][x] == t: 
                office[k][x] = v
    if n==1:
         for k in range(y+1,N):
            if office[k][x] == 6: break
            if office[k][x] == t: 
                office[k][x] = v
    if n==2:
         for k in range(x-1,-1,-1):
            if office[y][k] == 6: break
            if office[y][k] == t: 
                office[y][k] = v
    if n==3:
         for k in range(x+1,M):
            if office[y][k] == 6: break
            if office[y][k] == t:
                office[y][k] = v
            

def dfs(start):
    global office, minBlindCnt
    
    for s in range(start, N*M):
        y = s // M
        x = s % M
        if office[y][x] == 0 or office[y][x] == 6 or office[y][x] == 9: continue
        nextStart = y*M + x + 1
        v = y*M+x+10
        if office[y][x] == 1:
            cctvAction(y,x,0,0,v)
            dfs(nextStart)
            cctvAction(y,x,0,v,0)
            
            cctvAction(y,x,1,0,v)
            dfs(nextStart)
            cctvAction(y,x,1,v,0)
            
            cctvAction(y,x,2,0,v)
            dfs(nextStart)
            cctvAction(y,x,2,v,0)
            
            cctvAction(y,x,3,0,v)
            dfs(nextStart)
            cctvAction(y,x,3,v,0)
            break
        if office[y][x] == 2:
            cctvAction(y,x,0, 0,v)
            cctvAction(y,x,1, 0,v)
            dfs(nextStart)
            cctvAction(y,x,0, v,0)
            cctvAction(y,x,1, v,0)
            
            cctvAction(y,x,2, 0,v)
            cctvAction(y,x,3, 0,v)
            dfs(nextStart)
            cctvAction(y,x,2, v,0)
            cctvAction(y,x,3, v,0)
            break
        if office[y][x] == 3:
            cctvAction(y,x,0, 0,v)
            cctvAction(y,x,2, 0,v)
            dfs(nextStart)
            cctvAction(y,x,0, v,0)
            cctvAction(y,x,2, v,0)
            
            cctvAction(y,x,0, 0,v)
            cctvAction(y,x,3, 0,v)
            dfs(nextStart)
            cctvAction(y,x,0, v,0)
            cctvAction(y,x,3, v,0)
            
            cctvAction(y,x,1, 0,v)
            cctvAction(y,x,2, 0,v)
            dfs(nextStart)
            cctvAction(y,x,1, v,0)
            cctvAction(y,x,2, v,0)
            
            cctvAction(y,x,1, 0,v)
            cctvAction(y,x,3, 0,v)
            dfs(nextStart)
            cctvAction(y,x,1, v,0)
            cctvAction(y,x,3, v,0)
            break
        if office[y][x] == 4:
            #0,1,2
            cctvAction(y,x,0, 0,v)
            cctvAction(y,x,1, 0,v)
            cctvAction(y,x,2, 0,v)
            dfs(nextStart)
            cctvAction(y,x,0, v,0)
            cctvAction(y,x,1, v,0)
            cctvAction(y,x,2, v,0)
            #0,1,3
            cctvAction(y,x,0, 0,v)
            cctvAction(y,x,1, 0,v)
            cctvAction(y,x,3, 0,v)
            dfs(nextStart)
            cctvAction(y,x,0, v,0)
            cctvAction(y,x,1, v,0)
            cctvAction(y,x,3, v,0)
            #0,2,3
            cctvAction(y,x,0, 0,v)
            cctvAction(y,x,2, 0,v)
            cctvAction(y,x,3, 0,v)
            dfs(nextStart)
            cctvAction(y,x,0, v,0)
            cctvAction(y,x,2, v,0)
            cctvAction(y,x,3, v,0)
            #1,2,3
            cctvAction(y,x,1, 0,v)
            cctvAction(y,x,2, 0,v)
            cctvAction(y,x,3, 0,v)
            dfs(nextStart)
            cctvAction(y,x,1, v,0)
            cctvAction(y,x,2, v,0)
            cctvAction(y,x,3, v,0)
            break
        if office[y][x] == 5:
            for i in range(4):
                cctvAction(y,x,i, 0,v)    
    #for문 끝난후
    blindCnt = 0
    for y in range(N):
        for x in range(M):
            if office[y][x]==0: blindCnt+=1  
    if minBlindCnt > blindCnt: 
        minBlindCnt = blindCnt
        # print(minBlindCnt)
        # for y in range(N):
        #     for x in range(M):
        #         print(str(office[y][x]).zfill(2), end=" ")
        #     print()
        # print()
        
minBlindCnt=M*N
dfs(0)
print(minBlindCnt)
