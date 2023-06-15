# 풀이 과정
1. while문을 활용한 투포인터
   1. 정렬을 먼저 해준다.
   2. 인덱스 start, end를 활용한다.
   3. 맨 끝부터 처리한다.
   4. start, end비교를 제일 처음해야 한다. and 구문
   5. 부등호 >= 는 하나만 움직이며 비교할 때, > 는 둘다 움직이며 비교할 때 사용한다.
   6. 같은 구간의 조건이 잘 맞는지 확인하고 안되면 합이나 차를 사용해서 푼다.
   ```python
   
    arr.sort() # 오름차순 정렬
   
    # 끝자락 엣지부터 고려해서 start, end 가지고 놀아보자
    servers = 0
    start = 0
    end = M - 1
    # 600 이상은 하나, 하나만 움직이니까 =
    while end >= start and arr[end] > 600:
        servers += 1
        end -= 1
    # 300, 600 이면 하나, 둘다 움직이니까 >, <
    while end > start and arr[start] == 300 and arr[end] == 600:
        servers += 1
        start += 1
        end -= 1
    # 300이 남으면 문제발생 : 혼자 3번 가능하다.
    num300 = 0
    while end >= start and arr[start] == 300:
        start += 1
        num300 += 1
    # 301 ~ 600까지
    while start < end:
        if arr[start] + arr[end] <= 900:
            servers += 1
            start += 1
            end -= 1
        elif num300 > 0:
            servers += 1
            end -= 1
            num300 -= 1
        else:
            servers += 1
            end -= 1

   ```

2. 마지막에 하나 남는 부분을 조심하자.
```python
    # 그래도 하나 남았다면
    if start == end:
        servers += 1
        if num300 > 0:
            num300 -= 1

    servers += (num300 + 2)// 3
    print(servers)
```