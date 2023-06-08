import sys
sys.stdin= open("우물안개구리.txt")
input = sys.stdin.readline
N, M = map(int, input().split())
W = [0] + list(map(int, input().split()))
friend = [list(map(int, input().split())) for _ in range(M)]

totalcheck = [1]*(N+1)
totalcheck[0] = 0
for m in range(M):
    if W[friend[m][0]] > W[friend[m][1]]:
        totalcheck[friend[m][1]] = 0

    elif W[friend[m][0]] < W[friend[m][1]]:
        totalcheck[friend[m][0]] = 0
    else:
        totalcheck[friend[m][1]] = 0
        totalcheck[friend[m][0]] = 0

answer = totalcheck.count(1)
print(answer)





