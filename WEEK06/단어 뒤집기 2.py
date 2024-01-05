import sys
input = sys.stdin.readline

S = input().strip()
reverseS = S[::-1]

reverseStart = 1

wordLen = len(S)
tagMode = False
wordStart = 0

for i in range(wordLen):
    if S[i] == ' ' and tagMode==False:
        print(reverseS[wordLen-i:wordLen-wordStart], end='')
        print(' ', end='')
        wordStart = i+1
    if S[i] == '<':
        print(reverseS[wordLen-i:wordLen-wordStart], end='')
        tagMode = True
    if S[i] == '>':
        print('>',end='')
        tagMode = False
        wordStart = i+1
    if tagMode:
        print(S[i], end='')
print(reverseS[:wordLen-wordStart])
