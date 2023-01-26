import sys;
sys.stdin = open('금고털이.txt')

W, N = map(int, input().split())
arr = []
for _ in range(N):
    m, p = map(int, input().split())
    arr.append((m,p))

s_arr = sorted(arr, key=lambda x: x[1], reverse=True)
answer = 0
for i in range(N):
    if W >= s_arr[i][0]:
        W -= s_arr[i][0]
        answer += s_arr[i][0] * s_arr[i][1]

    elif W < s_arr[i][0]:
        answer += W * s_arr[i][1]
        break

print(answer)






