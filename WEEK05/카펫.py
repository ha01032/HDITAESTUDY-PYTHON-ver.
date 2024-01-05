#프로그래머스 카펫
def solution(brown, yellow):
    area = brown + yellow
    answer = []
    for w in range(1,area+1):
        if w >= (area/w):
            if (w-2)*((area/w)-2) == yellow:
                answer = [w, area//w]
                break
                 
            
    return answer

print(solution(10,2))
