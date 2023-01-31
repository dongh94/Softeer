import sys; sys.stdin=open("전광판.txt")
#최소 변경 횟수 구하기.
#아이디어 : 다섯자리라는 점/ 7 * 5 = 35/
#1. 자릿 수 파악. => 자릿수가 다른만큼 + 그숫자 그대로
#2. 숫자 파악 => 1 - 9 : 1: 2, 2: 5, 3: 5, 4 : 4
#3. 칸 파악 => 칸마다 확인해서 0, 1 로 켜져있는지 딕셔너리 리스트로 정리?

number_dict = {'0': [1,1,1,0,1,1,1], '1': [0,0,1,0,0,1,0], '2':[1,0,1,1,1,0,1],
               '3': [1,0,1,1,0,1,1], '4': [0,1,1,1,0,1,0], '5':[1,1,0,1,0,1,1],
               '6': [1,1,0,1,1,1,1], '7': [1,1,1,0,0,1,0], '8':[1,1,1,1,1,1,1],
               '9': [1,1,1,1,0,1,1], 'z':[0,0,0,0,0,0,0]}
T = int(input())
for t in range(T):
    answer = 0
    A, B = input().split()
    length_a = len(A)
    length_b = len(B)

    new_A = (5 - length_a) * 'z' + A
    new_B = (5 - length_b) * 'z' + B

    for i in range(5):
        for j in range(7):
            answer += (number_dict[new_A[i]][j] != number_dict[new_B[i]][j])
    print(answer)
