# 1157. 단어 공부

given = input()
voca = given.upper()
N = len(voca)

# [count 메서드 안 쓰고...;;]
# searched = []  # 한 번 나온 알파벳을 담을 빈 리스트
# counts = []    # 각 알파벳의 개수를 담을 빈 리스트
# for i in range(N-1):
#     if voca[i] not in searched:
#         searched.append(voca[i])
#         cnt = 1  # 알파벳의 개수를 셀 변수 (i마다 초기화, 자기자신 포함이므로 1에서 시작)
# 
#         for j in range(i+1, N):
#             if voca[i] == voca[j]:
#                 cnt += 1
#         counts.append(cnt)
# 
#     else:
#         continue
# # print(searched)  # ['M', 'I', 'S', 'P']
# # print(counts)    # [1, 4, 4, 1]

# [count 메서드 사용]
searched = []  # 한 번 나온 알파벳을 담을 빈 리스트
counts = []    # 각 알파벳의 개수를 담을 빈 리스트
max_used = 0
max_char = ''
check = True   # max 값 중복을 판단할 변수

for char in voca:
    used = 0  # 각 알파벳이 사용된 개수를 셀 변수

    if char not in searched:     # 아직 탐색 안 한 알파벳이면
        searched.append(char)    # 탐색 표시하고
        used = voca.count(char)  # 알파벳의 개수 세기

        if used > max_used:      # max보다 큰 값일 때
            check = True
            max_used = used
            max_char = char

        elif used == max_used:   # max와 같은 값일 때
            check = False
            continue
            
if check == True:  # for문 다 돌고 나와서 chekc 판단
    print(max_char)
else:
    print('?')


