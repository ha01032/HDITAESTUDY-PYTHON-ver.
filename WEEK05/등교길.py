def solution(m, n, puddles):
    
    DP = [[0]*(m+1) for _ in range(n+1)]

    for puddle in puddles:
        DP[puddle[1]][puddle[0]] = -1

    #집과 학교는 물에 잠기지 않는다.
    DP[1][1] = 1
    M= 1000000007
    for y in range(1,n+1):
        for x in range(1,m+1):
            #장애물이면 DP 계산 안함
            if DP[y][x] == -1: continue
            if 1 <= y-1:
                if DP[y-1][x] != -1:
                    DP[y][x] = ((DP[y][x] % M) + (DP[y-1][x] % M)) % M
            if 1 <= x-1:
                if DP[y][x-1] != -1:
                    DP[y][x] = ((DP[y][x] % M) + (DP[y][x-1] % M)) % M
    return DP[n][m] % M
