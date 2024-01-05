def canChange(start, end):
    global wordLen
    notSame = 0
    for i in range(wordLen):
        if start[i] != end[i]: notSame+=1
        if notSame == 2: return False
    return True



def solution(begin, target, words):
    global wordLen   
    wordLen = len(begin)
    
    answer = 0
    # bfs 시작
    q = []
    levelq = []
    q.append(begin)
    if words.count(begin):
        words.remove(begin) 
    levelq.append(0)
    
    while(q):
        start = q[0]
        level = levelq[0]
        q = q[1:]
        levelq = levelq[1:]
        for end in words:
            if canChange(start, end):
                if end==target:
                    return level+1
                q.append(end)
                levelq.append(level+1)
                words.remove(end)        
    return 0
