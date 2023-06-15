# 풀이 과정
0. DFS는 Stack이다2. (1은 이미지프로세싱)
1. 초깃값이 있다면 while의 조건문이다.
2. append가 아니라면 파라미터 변수의 변화다
3. 파라미터바뀌는 부분에 재귀가 돈다.
4. 대신 return값으로 처리해야 한다.


1. 일단 기록 단축을 위해선 Binary Search가 불가피해 보인다는 것을 파악해야함.
```python
#LogN 시간 = 먼저 최댓값이란 미드값을 찾고
# DFS
def bSearch(start, end):
    if start == end:
        return start

    mid = (start + end + 1) // 2
    if test(mid):
        return bSearch(mid, end)
    else:
        return bSearch(start, mid - 1)


# while - 최댓값 start
def bSearch(start, end):
    while start < end:
        mid = (start + end + 1) // 2
        if test(mid):
            start = mid
        else:
            end = mid - 1
    return start

```
2. 그 mid값이 딱 조건에 해당 되는 값인지를 확인한다.

```python

def test(mid):
    S = [0]*N
    S[0] = C[0] # 최솟값 넣고
    for i in range(N-1):
        if S[i] >= mid: # C만 넣은게 괜찮다면
            S[i+1] = C[i+1] + D[i] # 다음 값에 C값에 D값까지 넣어주고
        elif S[i] + D[i] >= mid: # C랑 D를 넣은게 괜찮다면
            S[i+1] = C[i+1] + (S[i] + D[i] - mid) # 다음 값에는 C에다 남은 것만 넣을 수 있다.
        else: # 안괜찮으면
            return False # 통과 X -> end를 내리시게 mid - 1 로

    if S[N-1] >= mid: # 마지막값까지도 괜찮다면
        return True # 통과 O -> start를 높여보시게 mid 로
    else:
        return False # 통과 X -> end를 내리시게 mid - 1 로

```