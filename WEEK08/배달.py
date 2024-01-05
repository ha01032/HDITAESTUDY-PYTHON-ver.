# https://school.programmers.co.kr/learn/courses/30/lessons/12978

import heapq
import math
# 다익스트라 거리배열을 만들고
# K이하인 수를 세서 출력

def solution(N, road, K):
    #인접리스트 생성
    G = [[] for _ in range(N+1)]
    #거리배열 생성
    INF = math.inf
    D = [INF]*(N+1)
    #우선순위큐 생성
    q=[]
    #visited 생성
    visited = [False]*(N+1)
    
    #각각 초기화
    D[1] = 0
    visited[1] = True
    for way in road:
        G[way[0]].append((way[1], way[2]))
        G[way[1]].append((way[0], way[2]))
        if(way[0] == 1):
            if D[way[1]] > way[2]:
                D[way[1]] = way[2]
                heapq.heappush(q, (way[2], way[1]))
        if(way[1] == 1):
            if D[way[0]] > way[2]:
                D[way[0]] = way[2]
                heapq.heappush(q, (way[2], way[0]))      
    #다익스트라 수행
    while q:
        dist, currTown = heapq.heappop(q)
        visited[currTown] = True
        
        for adj in G[currTown]:
            adjTown, adjDist = adj
            if visited[adjTown]: continue
            if D[adjTown] > dist+adjDist:
                D[adjTown] = dist+adjDist    
                heapq.heappush(q, (D[adjTown], adjTown))
            
    #정답구하기
    answer = 0
    for minDist in D:
        if minDist <= K:
            answer+=1
        
    return answer
