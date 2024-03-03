def solution(n, times):
    officers = len(times)      # 입국심사관의 수 
    max_time = max(times) * n  # 최대 시간(가장 오래 걸리는 심사관이 모두를 검사)
    start = 1
    end = max_time
    
    # total_people이 n보다 커도 start가 end보다 커지면 while문이 종료되고 그 때의 mid가 정답 
    while start <= end :
        # print('-----------------')
        mid = (start + end) // 2
        # print('mid :', mid, '로 설정')
        
        # 각각의 심사관에게 mid 만큼의 시간을 줬을 때 검사할 수 있는 최대 인원
        total_people = 0  # 특정 시간에 검사할 수 있는 사람의 수 초기화 
        for time in times:
            total_people += mid // time
            
        # print('total_people :', total_people)
        
        # 더 많은 인원 검사 가능 → 일단 OK(answer 갱신), 시간 더 줄일 수 있는지 확인
        if total_people >= n:
            answer = mid
            end = mid - 1
            # print(f'answer 갱신 : {answer}')
            # print(f'더 많은 인원 : {total_people}, end {end}로 변경')
            
        # 적은 인원 검사 가능 → 불가능한 상황이므로 무조건 시간 늘리기
        elif total_people < n:
            start = mid + 1
            # print(f'더 적은 인원 : {total_people}, start {start}로 변경')
            
    return answer