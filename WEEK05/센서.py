# https://www.acmicpc.net/problem/2212

import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

sensors = list(map(int,input().strip().split()))
# 센서의 오름차순 정렬
sensors.sort()

# 간격 구하기
term = [0]*(N-1)
for i in range(N-1):
    term[i] = sensors[i+1] - sensors[i]

# 간격의 내림차순 정렬
term.sort(reverse=True)

# 간격 중 큰거 K-1개 제거한 합이 답
print(sum(term[K-1:]))
