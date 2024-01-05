# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    kinds = []
    for c in clothes:
        kinds += [c[1]]
    setKinds = set(kinds)
    answer = 1
    for kind in setKinds:
        answer *= (kinds.count(kind)+1)
        


    answer = answer-1
    return answer
