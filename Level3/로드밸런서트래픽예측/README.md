# 풀이 과정
1. 위상정렬 - 선수과목 Q 
   1. indegree (진입과목 += 1)
   2. 0이면 Q append, result append
   3. child indegree -= 1
   4. 0이면 Q append
   5. return result
   ```python
   # (진입과목 += 1)
   def calcIndegree(dag):
    indegree = [0] * (N+1)
    for i in range(1, N+1):
        for j in range(1, dag[i][0] + 1):
            indegree[dag[i][j]] += 1
    return indegree
   
   # 0이면 Q append , result append
   # child indegree -= 1
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
   ```
2. 카운팅 리스트
   * dp 개념으로도 활용
   * for loop - 카운팅 리스트
   * 2중 for loop - 정보 리스트
* ```python
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
       
    ```