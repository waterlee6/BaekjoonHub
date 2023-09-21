# 10952. A + B -5
# 0 0이 들어올 때까지 A+B를 출력하는 문제 -> 무한루프를 활용

while True:
    A, B = map(int, input().split())
    if A + B == 0:
        break
    else:
        print(A+B)
