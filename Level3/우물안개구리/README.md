1. 모두 통일된 정보 리스트 활용
```python
totalcheck = [1]*(N+1)
totalcheck[0] = 0
...

answer = totalcheck.count(1)
```
2. 딱 비교군만 for문
```python
for m in range(M):
    if W[friend[m][0]] > W[friend[m][1]]:
        totalcheck[friend[m][1]] = 0

    elif W[friend[m][0]] < W[friend[m][1]]:
        totalcheck[friend[m][0]] = 0
    else:
        totalcheck[friend[m][1]] = 0
        totalcheck[friend[m][0]] = 0
```

3. 처음에 그래프처럼 만들어서 2중 포문활용 (이전보다 2배 처리 비효율)
```python
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
```