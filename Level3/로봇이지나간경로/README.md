## 풀이방식

1. 출발점을 찾아야하므로 # 을 찾아서 상좌하우에 #이 하나밖에 없는 지점을 찾는다. 총 2개가 나온다.
```python
def findStart(arr):
    for r in range(N):
        for c in range(M):
            if arr[r][c] == '#':
                direct = findD(r, c)
                if direct != -1:
                    return r, c, direct
```
2. 기점을 시작으로 범위안에 #이 있으면 방향 정보를 가져온다.

```python

def findD(r, c):
    count = 0
    direct = -1
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == '#':
            count += 1
            direct = d
    return direct if count == 1 else -1
```
3. 기점을 시작으로 while True를 활용하고 return 조건을 생각한다.
4. return 조건은 방향을 찾을 때 더이상 #이 존재하지 않아 방향을 못찾는 경우가 된다.

```python

def navi(r, c, d):
    newD = preD = d
    arr[r][c] = '.'
    while True:
        while newD == preD:
            print('A', end="")
            for _ in range(2):
                r = r + dr[newD]
                c = c + dc[newD]
                arr[r][c] = '.'

            preD = newD
            newD = findD(r, c)

        # 상좌하우 0, 1, 2, 3 pre
        # 좌하우상 1, 2, 3, 0 new = 1, 1, 1, -3 => ((-3 % 4) + 4) % 4
        # 우상좌하 3, 0, 1, 2 new = 3, -1, -1, -1 => ((-1 % 4) + 4) % 4
        if newD == -1: # 종료조건
            return
        elif (newD - preD) % 4 == 1:
            print('L', end="")
        elif (newD - preD) % 4 == 3:
            print('R', end="")
        preD = newD
```
5. 그 전까지 새로운 방향과 이전 방향이 같으면 2번 전진하며 A를 print하고
6. 그렇지 않고 newD - preD % 4 == 1이면 L 로 회전함을 의미 (-3%4 = 1)
7. newD - preD % 4 == 3 이면 R로 회전함을 의미한다.
# 상좌하우 0, 1, 2, 3 pre
# 좌하우상 1, 2, 3, 0 new = 1, 1, 1, -3 => ((-3 % 4) + 4) % 4
# 우상좌하 3, 0, 1, 2 new = 3, -1, -1, -1 => ((-1 % 4) + 4) % 4