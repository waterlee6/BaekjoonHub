# 10951. A+B-4
# 그냥 while문을 사용하면 입력이 언제 끝나는지 알 수 없어서 무한루프에 걸리는 듯
# try except 구문을 활용해서 EOF(End of FIle)을 지정해 줘야 함

import sys
while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
        print(A+B)
    except:
        break