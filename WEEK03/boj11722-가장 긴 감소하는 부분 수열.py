# https://www.acmicpc.net/problem/11722
import sys
input = sys.stdin.readline

seqLen = int(input())
seq = list(map(int,input().strip().split()))

DP = [1]*seqLen

for currIdx in range(seqLen):
    for pastIdx in range(currIdx):
        if seq[pastIdx] > seq[currIdx]:
            DP[currIdx] = max(DP[currIdx], DP[pastIdx]+1)

print(max(DP))
