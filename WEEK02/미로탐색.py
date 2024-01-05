# https://www.acmicpc.net/problem/2178

import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split(' ')]
miro = ''
for _ in range(n):
    miro += input().strip()

pos = lambda i, j: i * m + j

visited = [0] * n * m

q = []

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

q.append((0, 0))
visited[pos(0, 0)] = 1
while q:
    y, x = q[0]
    q = q[1:]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (ny < 0 or ny > n - 1 or nx < 0 or nx > m - 1 
            or miro[pos(ny, nx)] == '0' or visited[pos(ny, nx)]):
            continue
        visited[pos(ny, nx)] = visited[pos(y, x)] + 1
        q.append((ny, nx))

print(visited[pos(n - 1, m - 1)])
