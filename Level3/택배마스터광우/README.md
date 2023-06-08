### 풀이과정

1. dfs로 '어떤 순서'의 모든 경우를 만든다.
```python
used = [False] * N
result = [0]*N
def dfs(k):
    global answer
    if k == N:
        return
    for i in range(N):
            if used[i] == False:
                used[i] = True
                result[k] = arr[i]
                dfs(k + 1)
                used[i] = False
```

2. 한 경우마다 조건문을 돌린다 (인덱스가 계속 회전하는 것이 특징)
```python
total = 0
idx = 0
for n in range(K):
    box = 0
    while True:
        box += result[idx]
        idx = (idx+1) % N  # while 문과 %의 활용으로 무한 회전 가능.
        if box + result[idx] > M:
            break
    total += box
answer = min(answer, total)
```