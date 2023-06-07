import sys
sys.stdin = open("조립라인.txt")

N = int(input())
A = [0] * N
AtoB = [0] * N
B = [0] * N
BtoA = [0] * N
for n in range(N):
    info = list(map(int, input().split()))
    A[n] = info[0]
    B[n] = info[1]
    if n == N-1: break;
    AtoB[n] = info[2]
    BtoA[n] = info[3]

dpA = [float('inf')] * ((10 ** 3) + 1)
dpB = [float('inf')] * ((10 ** 3) + 1)
dpA[0] = A[0]
dpB[0] = B[0]
for i in range(N-1):

    dpA[i+1] = min(dpA[i+1], A[i+1] + dpA[i], BtoA[i] + dpB[i] + A[i+1])
    dpB[i+1] = min(dpB[i+1], dpB[i] + B[i+1], AtoB[i] + dpA[i] + B[i+1])

print(min(dpA[N-1], dpB[N-1]))




