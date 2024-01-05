import sys
input = sys.stdin.readline

w,h = map(int, input().strip().split())

field = [[] for _ in range(h)]

for i in range(h):
	field[i] = list(input().strip())

visited = [[False]*w for _ in range(h)]



dy=[1,-1,0,0]
dx=[0,0,1,-1]

def inRange(y,x):
	return y>=0 and y<h and x>=0 and x<w

def dfs(y,x):
	global visited, team, cnt
	for i in range(4):
		ny = y + dy[i]
		nx = x + dx[i]
		if inRange(ny,nx) and not visited[ny][nx]:
			if field[ny][nx] == team:
				cnt += 1
				visited[ny][nx] = True
				dfs(ny,nx)
				
alias = 0
enemy = 0

for y in range(h):
	for x in range(w):
		if not visited[y][x]:
			team = field[y][x]
			cnt = 1
			visited[y][x]=True
			dfs(y,x)
            
			if team=='W': alias += (cnt*cnt)
			else: enemy += (cnt*cnt)


print(str(alias)+" "+str(enemy))
