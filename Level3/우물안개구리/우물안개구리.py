import sys

sys.stdin = open("우물안개구리.txt")
input = sys.stdin.readline
N, M = map(int, input().split())
W = list(map(int, input().split()))
friend = [[] for _ in range(N+1)]

def isKing(i, new):
    if W[i-1] <= W[new-1]:
        return False
    return True

for m in range(M):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

answer = 0
for i in range(1, N+1):
    iamKing = True
    for j in friend[i]:
        if not isKing(i, j):
            iamKing = False
            break
    if iamKing:
        answer += 1
print(answer)






