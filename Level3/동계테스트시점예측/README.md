풀이방법
1. 우선 while True 로 계속 돌려가면서 하는 방법을 선택했다. arr를 계속 바꿔줘야 했기 때문에

```python
while True:
    if sum(sum(row) for row in arr) == 0:
        break
        
    else:
        check(0, 0)
        answer += 1

```
2. 2차 배열의 모든 항목이 0 임을 sum ( for ) 를 통해 알아 내었다.

```python
sum(sum(row) for row in arr) == 0
```

3. bfs()를 통해 범위 안의 not visited 모두 돌면서 Q에 넣고 1을 발견하면 += 1 하고 Q에 넣지 않는다.

```python
def check(r, c):
    Q = deque()
    Q.append((r, c))
    visited = [[0]*M for _ in range(N)]
    visited[r][c] = 1
    while Q:
        sr, sc = Q.popleft()
        for d in range(4):
            nr = sr + dr[d]
            nc = sc + dc[d]
            if 0 <= nr < N and 0 <= nc < M:
                # 1 보이면 바로 += 1 끝.
                if arr[nr][nc] == 1:
                    visited[nr][nc] += 1

                if visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    Q.append((nr,nc))

```

4. visited도 갱신필요하고 2이상이면 arr을 0으로 바꾼다.

```python
    for x in range(N):
        for y in range(M):
            if visited[x][y] >= 2:
                arr[x][y] = 0

```
