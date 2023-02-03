import sys; sys.stdin=open("업무처리.txt")
input = sys.stdin.readline
# 아이디어
# 첫날 말단이 일 => 둘 날 오른쪽 => 셋날 => 왼쪽
# H 는 1이면 2, 2: 4, 3: 8 4: 16 5: 32
# K 는 말단의 일 갯수
# R 은 날짜 => 결과의 기준이 됨 ( 결과 : R일날 완료된 업무 번호의 합)
#조직도의 높이 H, 리말단에 대기하는 업무의 개수 K, 업무가 진행되는 날짜 수
H, K, R = map(int, input().split())

