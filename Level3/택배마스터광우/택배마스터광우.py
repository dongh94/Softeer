import sys
sys.stdin = open("택배마스터광우.txt")
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

# 어떤 순서
# 그 순서의 총 갯수만큼의 정보 리스트를 만들어
used = [False] * N
result = [0]*N
answer = float('inf')
def dfs(k):
    global answer
    if k == N:
        total = 0
        idx = 0
        for n in range(K):
            box = 0
            while True:
                box += result[idx]
                idx = (idx+1) % N
                if box + result[idx] > M:
                    break
            total += box
        answer = min(answer, total)
        return

    for i in range(N):
        if used[i] == False:
            used[i] = True
            result[k] = arr[i]
            dfs(k + 1)
            used[i] = False
dfs(0)
print(answer)
