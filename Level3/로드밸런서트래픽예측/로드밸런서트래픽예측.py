import sys
from collections import deque
sys.stdin = open("로드밸런서트래픽예측.txt")



def calcIndegree(dag):
    indegree = [0] * (N+1)
    for i in range(1, N+1):
        for j in range(1, dag[i][0] + 1):
            indegree[dag[i][j]] += 1
    return indegree


def tsort(dag):
    indegree = calcIndegree(dag)
    # print(indegree)
    Q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            Q.append(i)
    result = []
    while Q:
        node = Q.popleft()
        result.append(node)
        for i in range(1, dag[node][0] + 1):
            child = dag[node][i]
            indegree[child] -= 1
            if indegree[child] == 0:
                Q.append(child)
    return result


# N = n of server , K = n of request
N, K = map(int, input().split())
dag = [[0]]
for i in range(N):
    temp = list(map(int, input().split()))
    dag.append(temp)
# print(dag)
result = tsort(dag)
print(result)

# 카운팅 리스트
traffic = [0] * (N+1)
traffic[1] = K
for i in range(N):
    node = result[i]
    if dag[node][0] == 0: continue;

    request = traffic[node]
    d , m = divmod(request, dag[node][0])
    # 몫을 분배
    for j in range(1, dag[node][0] + 1):
        child = dag[node][j]
        traffic[child] += d
    # 나머지 분배(하나씩)
    for j in range(1, m + 1):
        child = dag[node][j]
        traffic[child] += 1
print(*traffic[1:])


