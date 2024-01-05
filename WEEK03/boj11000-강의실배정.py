# https://www.acmicpc.net/problem/11000

import sys, heapq
input = sys.stdin.readline

N = int(input())

lecture = [[0,0] for _ in range(N)]

for i in range(N):
    lecture[i][0], lecture[i][1] = map(int,input().strip().split())

lecture.sort(key=lambda x: (x[0], x[1]))

room = []

heapq.heappush(room, lecture[0][1])

for i in range(1,N):
    if lecture[i][0] >= room[0]:
        heapq.heappop(room)
        heapq.heappush(room,lecture[i][1])
    else:
        heapq.heappush(room,lecture[i][1])

print(len(room))
