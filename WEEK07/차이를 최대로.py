# https://www.acmicpc.net/problem/10819

import sys
input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int,input().strip().split()))
visited = [0]*N



def dfs(start):
    global N, n, maxSum, visited, currSum
    if n==N:
        maxSum = max(maxSum, currSum)
        return
    for i in range(N):
        if(visited[i]): continue
        visited[i]=1
        n+=1
        currSum+=abs(start-arr[i])
        dfs(arr[i])
        currSum-=abs(start-arr[i])
        n-=1
        visited[i]=0

maxSum=0
for i in range(N):
    currSum=0
    visited[i] = 1
    n=1
    dfs(arr[i])
    visited[i] = 0
print(maxSum)        
