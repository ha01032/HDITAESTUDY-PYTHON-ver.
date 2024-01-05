# https://www.acmicpc.net/problem/2805

#나무자르기
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

trees = list(map(int,input().strip().split()))
trees.sort(reverse=True)
trees.append(0)
terms = []

for i in range(1,N+1):
    terms.append(trees[i-1] - trees[i])

n=0
sum=0
height=trees[0]

for i in range(0,N):
    n+=1
    if M < sum + n*terms[i]:
        if (M-sum)%n == 0: 
            print(height-((M-sum)//n))
        else: print(height-((M-sum)//n+1)) 
        sys.exit(0)
    sum += n*terms[i]
    height -= terms[i]
print(0)
