def dfs(start):
    global answer, ticketNum, adjMap
    if len(answer) == ticketNum+1:
        return True
    if start not in adjMap: return False
    for i in range(len(adjMap[start])):
        if adjMap[start][i] != "visited":
            end = adjMap[start][i]
            adjMap[start][i] = "visited"
            answer.append(end)
            if dfs(end):
                return True
            answer.pop()
            adjMap[start][i] = end
            

def solution(tickets):
    global answer, ticketNum, adjMap
    adjMap = {}
    ticketNum = len(tickets)
    for ticket in tickets:
        if not ticket[0] in adjMap:
            adjMap[ticket[0]] = []    
        adjMap[ticket[0]].append(ticket[1]) 
    for key in adjMap.keys():
        adjMap[key].sort()
    answer = ["ICN"]
    dfs("ICN")
    return answer
