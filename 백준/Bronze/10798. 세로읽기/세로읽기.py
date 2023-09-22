# 10798. 세로읽기

# import sys
# sys.stdin = open('input.txt')
arr = [input() for _ in range(5)]

# arr를 열 순회하면서 문자를 새 리스트에 저장하기
ans = []  # 답을 저장할 빈 리스트
for j in range(15):   # 최대 15개의 글자가 주어지므로
    for i in range(5):
        
        # 만약 해당 자리가 비어있을 때
        if len(arr[i]) <= j:
            continue

        # 해당 자리가 정상적으로 차있을 때
        else:
            ans.append(arr[i][j])

# 그냥 출력하면 중간에 공백이 포함되므로 sep값으로 공백을 제거
print(*ans, sep='')
