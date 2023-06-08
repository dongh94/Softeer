풀이 방식
1. 고정값에서 최댓값 등 개수 등 찾을 때는 순서를 잘 지키며 돌리면 된다.
# 순서 중요함
```python
for i in range(len(STR)): # 왼쪽에서 부터
    if STR[i] == 'P': # 찾으면
        for j in range(i-K, i+K+1): # 그 범위내로
            if j >= 0 and j < len(STR) and STR[j] == 'H': # 연결짓고
                STR[j] = 'O' # 바꾼후
                answer += 1 # 마무리
```