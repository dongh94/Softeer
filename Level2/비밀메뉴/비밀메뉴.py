import sys; sys.stdin=open('비밀메뉴.txt')
from collections import deque

M, N, K = map(int, input().split())
smenu = list(map(int, input().split()))
order = list(map(int, input().split()))

Q_order = deque(order)
list_smenu = len(smenu)
answer = "normal"
check = 0
while Q_order:
    num = Q_order.popleft()
    cnt = 1
    if len(Q_order) < M-1: break;
    if num == smenu[0]:
        for l in range(list_smenu - 1):
            if smenu[l+1] == Q_order[l]:
                cnt += 1
        if cnt == list_smenu:
            answer = "secret"
            check = 1
    if check:
        break;

print(answer)



