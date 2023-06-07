import sys
sys.stdin = open("조립라인.txt")

N = int(input())
A = [0] * N
AtoB = [0] * N
B = [0] * N
BtoA = [0] * N

temp_A = 0
temp_B = 0
work_A = 0
work_B = 0
for n in range(N):
    info = list(map(int, input().split()))
    A[n] = info[0]
    B[n] = info[1]
    if n == N-1: break;
    AtoB[n] = info[2]
    BtoA[n] = info[3]


for i in range(N-1):

    temp_A = min(A[i] + work_A, B[i] + BtoA[i] + work_B)
    temp_B = min(B[i] + work_B, A[i] + AtoB[i] + work_A)
    work_A = temp_A
    work_B = temp_B

temp_A += A[N-1]
temp_B += B[N-1]

print(min(temp_A, temp_B))




