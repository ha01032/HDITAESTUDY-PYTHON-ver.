# https://school.programmers.co.kr/learn/courses/30/lessons/60062

import itertools
#프로그래머스 외벽점검
#처음엔 각각의 간격을 이용하고, 이동거리긴 사람을 먼저 적용시키는 그리디 접근을 시도했으나 예외사항이 계속 떠오름
#결국 문제범위상 시간복잡도가 완전탐색이 가능해보여서 완전탐색을 할수밖에 없겠다는 생각까진 이르렀으나,,
#어떻게 완전탐색 구현할지는 전혀 감이 안와서 인터넷 해설보고 풀었습니다..

def solution(n, weak, dist):
   weakNum = len(weak)
   distNum = len(dist)
   #시계반대방향도 적용시키기 위해서, 선형으로 만들어준다.(마지막껀 안넣음)
   for i in range(weakNum-1):
        weak += [weak[i]+n]         
   
   #최소를 구하는 문제기에 최대값인 distNum보다 1큰값으로 임의로 지정
   #(어떤 수보다 큰 무한대로 지정해도 됨)
   minCnt = distNum+1
   
   #시작 지점 인덱스
   for start in range(weakNum):
       #점검하는사람순서 모든 경우의수(순열)중 하나
       for orderDist in itertools.permutations(dist, len(dist)):
            #해당 시작점인덱스(start)의 점검지점에서, 마지막 점검지점까지
            #해당 점검하는사람순서의경우의수(orderDist)에서, 사람이 차례대로 최종 cnt만큼 나와서
            #각자 최대한 점검을 진행하는 본격 점검의 시작! 
            cnt = 1 #투입인원수
            firstPos = start #처음 점검지점 인덱스
            for i in range(1, weakNum):
                #다음 점검지점 인덱스
                nextPos = start+i
                #처음점검지점에서 다음점검지점까지 거리
                diff = weak[nextPos]-weak[firstPos]
                if diff > orderDist[cnt-1]: #현재 점검하는 사람이 갈수있는 최대거리보다 총 점검지점간간격이 더 길면,
                    firstPos = nextPos #다음점검지점이 다음 점검하는사람의 시작점검지점이 된다.
                    cnt+=1 #점검하는 사람수 증가
                    if cnt == distNum+1: break #총사람수를 초과했다는것은 모든 사람으로도 점검이 불가능하단 것이다.
            #점검이 끝났으니, 점검 최소인원을 최신화
            minCnt = min(minCnt, cnt)
    #모든 시작점에 대한 모든 점검하는사람순서의 최소인원 비교를 다 진행하였다.
   if minCnt <= distNum: return minCnt
   return -1
