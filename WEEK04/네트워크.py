# https://school.programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    global adjMatrix, visited, N
    N = n
    adjMatrix = computers
    answer = 0
    visited = [False]*n

    for computer in range(n):
        if visited[computer]: continue
        visited[computer] = True
        answer+=1
        dfs(computer)  
    return answer

def dfs(computer):
    global adjMatrix, visited, N
    for other in range(N):
        if computer!=other and not visited[other] and adjMatrix[computer][other]:
            visited[other] = True
            dfs(other)
