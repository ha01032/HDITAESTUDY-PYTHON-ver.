# https://school.programmers.co.kr/learn/courses/30/lessons/12971

def solution(sticker):
    dp1 = [0]*len(sticker)
    dp2 = [0]*len(sticker)
    
    dp1max=0
    dp2max=0
    for i in range(0, len(sticker)):
        if i==0: 
            dp1[i] = (sticker[i])
            dp1max = dp1[i]
        if i==1:
            dp1[i] = dp1[0]
            dp2[i] = sticker[i]
            dp2max = dp2[i]
        if 1<i<=len(sticker)-2:
            dp1[i] = max(dp1[i-2]+sticker[i], dp1[i-1])
            dp1max =dp1[i]
        if 2<=i:
            dp2[i] = max(dp2[i-2]+sticker[i], dp2[i-1])
            dp2max = dp2[i]
    return max(dp1max, dp2max)
