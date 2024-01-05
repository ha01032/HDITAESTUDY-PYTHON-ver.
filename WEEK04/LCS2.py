# https://www.acmicpc.net/problem/9252

import sys
input = sys.stdin.readline

seq1 = input().strip()
seq2 = input().strip()

len1 = len(seq1)
len2 = len(seq2)

DP = [[0]*(len1+1) for _ in range(len2+1)]

for y in range(1,len2+1):
    for x in range(1,len1+1):
        if seq1[x-1] == seq2[y-1]:
            DP[y][x] = DP[y-1][x-1] + 1 
        else:
            if DP[y-1][x] > DP[y][x-1]:
                DP[y][x] = DP[y-1][x]
            else:  
                DP[y][x] = DP[y][x-1]

print(DP[len2][len1])

ans = ""
y,x = len2, len1
while(DP[y][x]>0):
    if seq1[x-1] == seq2[y-1]:
        ans = seq1[x-1] + ans
        y-=1
        x-=1
    else:
        if DP[y-1][x] > DP[y][x-1]:
            y-=1
        else: 
            x-=1
print(ans) 
