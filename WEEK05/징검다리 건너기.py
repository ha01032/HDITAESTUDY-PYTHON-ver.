stones = []
k = 0
def solution(stonesParam, kParam):
    global stones, k
    stones = stonesParam
    k = kParam
    #모든사람 이동을 이진탐색
    minNum = 1 #최소 한명은 이동
    maxNum = 200000000 #문제에서 준 최대값
    mid = (minNum+maxNum)//2
    while(minNum <= maxNum):
        if isAllCanCross(mid): minNum = mid+1
        else: maxNum = mid-1
        mid = (minNum+maxNum)//2
    return mid

#(함수) 모든 사람 이동할때 가능 여부를 체크하는 함수
#"연속적으로" 못밟는 돌의 수가 늘어나면 점프간격도 그 수만큼 늘어남
#점프간격이 k보다 커지는 순간 모두 못건넌다고 판단.
def isAllCanCross(peopleNum):
    global stones, k
    jump=1 #점프간격(바로앞에 돌 밟을수있을땐, 1)
    for stone in stones:#첫번째돌부터 탐색
        if stone < peopleNum: #해당 돌을 모든 사람이 밟을 수 없을때,
            jump += 1#못밟는 사람들이 해당 돌앞에서 점프해야 하는 간격 증가
            if(jump > k): #점프 간격이 k보다 클때,
                return False #모두 못건넌다(함수종료)
        else: jump = 1 #해당 돌을 모든 사람이 밟을 수 있을때,
                       #점프해야하는 간격 초기화
    return True #for문 끝까지 수행 ->모든 사람들이 다 건넜다.
