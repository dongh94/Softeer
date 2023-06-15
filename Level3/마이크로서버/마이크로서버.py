import sys
sys.stdin = open("마이크로서버.txt")
N = int(input())
for i in range(N):
    M = int(input())
    arr = list(map(int, input().split()))
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

    # 그래도 하나 남았다면
    if start == end:
        servers += 1
        if num300 > 0:
            num300 -= 1

    servers += (num300 + 2)// 3
    print(servers)


