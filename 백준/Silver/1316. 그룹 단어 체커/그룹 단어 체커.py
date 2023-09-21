# 1316. 그룹 단어 체커

# str을 받아, 그룹 단어인지 판단하는 함수
def groupword(word):
    global check

    used = [word[0]]  # 이미 사용한 문자를 저장, word의 첫 글자 저장하고 시작
    M = len(word)

    # word가 한 글자 짜리이면 무조건 그룹 단어이므로 return
    if M == 1:
        return

    else:
        for i in range(1, M):

            # 아직 만난적 없는 문자라면
            if word[i] not in used:
                used.append(word[i])  # used에 저장하고
                continue              # 다음 i로

            # 이미 사용한 적 있는 문자라면
            else:
                if word[i] == word[i-1]:  # 하나 전의 문자와 같으면 pass
                    continue

                else:                     # 하나 전의 문자와 다르다면
                    check = False         # check를 False로 두고
                    break                 # 그룹단어 아니므로 break


# import sys
# sys.stdin = open('input.txt')
N = int(input())  # N: 단어의 개수
arr = []  # N개의 단어를 저장할 리스트
cnt = 0   # 그룹 단어의 개수를 셀 변수
for _ in range(N):
    arr.append(input())
# print(arr)

# 각 단어에 대해서, 그룹 단어인지 판단
for word in arr:
    check = True  # 그룹단어인지 판단할 변수 (매 단어를 탐색하기 전에 True로 초기화)
    groupword(word)
    if check == True:
        cnt += 1
print(cnt)