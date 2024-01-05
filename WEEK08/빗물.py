# https://www.acmicpc.net/problem/14719

import sys
input = sys.stdin.readline

H,W = map(int, input().strip().split())

block = list(map(int,input().strip().split()))

DP = [500] * W

barrier = 0

#순차적으로 DP넣기
for i in range(W):
    if block[i] >= barrier: 
        DP[i] = 0
        barrier = block[i]
    else:
        DP[i] = barrier - block[i]


barrier = 0
#역순으로 DP넣기
for i in range(W):
    if block[W-i-1] >= barrier: 
        DP[W-i-1] = 0
        barrier = block[W-i-1]
    else:
        if DP[W-i-1] > (barrier - block[W-i-1]):
            DP[W-i-1] = barrier - block[W-i-1]

            
print(sum(DP))
