import sys
sys.stdin = open("코딩테스트세트.txt")

N, T = map(int, input().split())
# print(N, T)

def test(mid):
    S = [0]*N
    S[0] = C[0]
    for i in range(N-1):
        if S[i] >= mid:
            S[i+1] = C[i+1] + D[i]
        elif S[i] + D[i] >= mid:
            S[i+1] = C[i+1] + (S[i] + D[i] - mid)
        else:
            return False

    if S[N-1] >= mid:
        return True
    else:
        return False

def bSearch(start, end):
    while start < end:
        mid = (start + end + 1) // 2
        if test(mid):
            start = mid
        else:
            end = mid - 1
    return start

for i in range(T):
    C = [0] * N
    D = [0] * N
    Temp = list(map(int, input().split()))
    for i in range(N-1):
        C[i] = Temp[2*i]
        D[i] = Temp[2*i+1]
    C[N-1] = Temp[2*(N-1)]
    # print(C)
    # print(D)
    answer = bSearch(0, 2*10**12 + 1)
    print(answer)
