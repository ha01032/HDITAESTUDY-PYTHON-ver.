# https://school.programmers.co.kr/learn/courses/30/lessons/12952

answer=0
arrX=[]
arrY=[]
arrPlus = []
arrMinus = []

def solution(n):
    def makeQ(x):
        global answer, arrX, arrY, arrPlus, arrMinus
        if len(arrX) == n: 
            answer+=1
            return

        for y in range(n):
                if(not x in arrX and not y in arrY and not (x+y) in arrPlus and not (x-y) in arrMinus):

                    arrX.append(x)
                    arrY.append(y)
                    arrPlus.append(x+y)
                    arrMinus.append(x-y)
                    makeQ(x+1)
                    arrX.pop()
                    arrY.pop()
                    arrPlus.pop()
                    arrMinus.pop()
    makeQ(1)
    return answer
