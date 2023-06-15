import sys
sys.stdin = open("코딩테스트세트.txt")

N, T = map(int, input().split())
print(N, T)

def test(mid):
    S = [0]*N
    S[0] = C[0] # [2,0,0]
    for i in range(N-1):
        if S[i] >= mid: # [2,3,4]
            S[i+1] = C[i+1] + D[i]
        elif S[i] + D[i] >= mid: # [2,0,0]
            S[i+1] = C[i+1] + (S[i] + D[i] - mid)
        else:
            return False

    if S[N-1] >= mid:
        return True
    else:
        return False

#LogN 시간 = 먼저 최댓값이란 미드값을 찾고
def bSearch(start, end):
    if start == end:
        return start

    mid = (start + end + 1) // 2
    if test(mid):
        return bSearch(mid, end)
    else:
        return bSearch(start, mid - 1)


for i in range(T):
    C = [0] * N
    D = [0] * N
    Temp = list(map(int, input().split()))
    for i in range(N-1):
        C[i] = Temp[2*i]
        D[i] = Temp[2*i+1]
    C[N-1] = Temp[2*(N-1)]
    print(C)
    print(D)
    answer = bSearch(0, 10**12 + 1)
    print(answer)
