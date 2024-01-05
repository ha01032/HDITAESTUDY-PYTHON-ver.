# https://www.acmicpc.net/problem/14226

#boj14226 이모티콘
import sys, math
from collections import deque
input = sys.stdin.readline

S = int(input())

#그냥 하나 복사해서 더해주면 무조건 S가 됨
minTime = S

visited = [[-1]*(2*S+1) for _ in range(2*S+1)]

#BFS 시작
q = deque([])
q.append((1, 0))
visited[1][0] = 0

while q:
    currState = q.popleft()
    emoticon = currState[0]
    clipboard= currState[1]
    time = visited[emoticon][clipboard]
    if emoticon == S: 
        print(time)
        break
    
    for i in range(3):
        nextEmoticon = emoticon if i==1 else emoticon+clipboard if i==2 else emoticon-1
        nextClipboard = emoticon if i==1 else clipboard
        if nextEmoticon<=0 or nextEmoticon>2*S or visited[nextEmoticon][nextClipboard] != -1: continue
        visited[nextEmoticon][nextClipboard] = visited[emoticon][clipboard]+1
        q.append((nextEmoticon, nextClipboard))
