# https://school.programmers.co.kr/learn/courses/30/lessons/150367

import sys
import math
def dfs(parent):
    global level, binLevel, binNumber 
    
    if level == binLevel: return 1

    #두 자식노드 확인
    leftChild = parent - 2**(binLevel-level-1)
    if(binNumber[parent]=='0' and binNumber[leftChild] != '0'):return 0
    rightChild = parent + 2**(binLevel-level-1)
    if(binNumber[parent]=='0' and binNumber[rightChild] != '0'):return 0
    level+=1
    if(dfs(leftChild)==0): return 0
    if(dfs(rightChild)==0): return 0
    level-=1
    return 1
    
def canBinaryTree(number):
    if(number==1): return 1
    global level, binLevel, binNumber
    #이진수 자리수
    binDigit = math.floor(math.log2(number))+1
    #포화이진트리변환 level
    binLevel = math.floor(math.log2(binDigit))+1
    #이진수 변환
    binNumber = bin(number)[2:].zfill(2**binLevel-1)  
    #DFS 수행
    level = 1
    return dfs(2**(binLevel-1)-1)

def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(canBinaryTree(number))
    return answer
