높아지는 다리 수 세기

각 리스트인덱스마다 증가하면 +1 한 값을 가지고 있기.
```python
rocks = [1]*length
for i in range(length-1):
    for j in range(i+1, length):
        if arr[i] < arr[j]:
            rocks[j] = max(rocks[j], rocks[i] + 1)
```

