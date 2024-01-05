# https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    

    for row in range(1,len(triangle)):
        for i in range(row+1):
            if i==0: 
                triangle[row][i] = triangle[row][i]+triangle[row-1][i]
            elif i==len(triangle[row])-1: 
                triangle[row][i] = triangle[row][i]+triangle[row-1][i-1]
            else: 
                triangle[row][i] = triangle[row][i]+max(triangle[row-1][i],triangle[row-1][i-1])


    answer = max(triangle[len(triangle)-1])
    return answer
