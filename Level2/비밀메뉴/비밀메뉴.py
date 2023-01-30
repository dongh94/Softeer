import sys; sys.stdin=open('비밀메뉴.txt')
from collections import deque

M, N, K = map(int, input().split())
smenu = list(map(int, input().split()))
order = list(map(int, input().split()))

OD = deque(order)
SM = len(smenu)
answer = "normal"

if SM > len(OD):
    print(answer)
else:
    while OD:
        num = OD.popleft()
        cnt = 1
        if num != smenu[0]: continue;
        elif len(OD) < M: break;
        else:
            for l in range(SM - 1):
                if smenu[l+1] == OD[l]:
                    cnt += 1
            if cnt == SM:
                answer = "secret"
                print(answer)
                break

    if answer != "secret":
        print(answer)



