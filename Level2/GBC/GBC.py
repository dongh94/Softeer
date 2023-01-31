import sys; sys.stdin=open("GBC.txt")
# 최초 아이디어
# 100개 칸을 만든다.
# 개수만큼 숫자를 채우고
# 카운팅 비교처럼 비교한다. 비교시 스트링 인데 그건 자릿수 비교 등 눈에 보이는 비교
N, M = map(int, input().split())
standard = [0] * 100
prior = 0
for _ in range(N):
    S, E = map(int, input().split())
    for i in range(prior,S+prior):
        standard[i] = E
    prior += S

watch_list = [0] * 100
prior2 = 0
for _ in range(M):
    S, E = map(int, input().split())
    for i in range(prior2,S+prior2):
        watch_list[i] = E
    prior2 += S

max_V = 0
for i in range(100):
    answer = watch_list[i] - standard[i]
    if max_V < answer:
        max_V = answer
print(max_V)
