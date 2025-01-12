from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque([])
    
    # 작업의 진도와 속도를 함께 반복
    for p, s in zip(progresses, speeds):
        # 남은 작업을 속도로 나눈 몫과 나머지 계산
        a, b = divmod(100-p, s)
        # 나머지가 있을 경우 작업을 끝내는데 하루 더 소모됨
        if b != 0:
            a += 1
        # 기능의 순서대로 큐에 작업을 끝내는데 필요한 일자를 넣음
        queue.append(a)

    # 한번의 배포되는 기능 개수 초기화
    cnt = 0
    
    while queue:
        # 배포 완료된 첫 번째 기능
        d = queue.popleft()
        cnt += 1
        
        # 다음 기능들이 남은 경우
        if queue:
            # 다음 기능이 첫 번째 기능보다 먼저 완료된 경우 같이 배포
            while queue[0] <= d:
                queue.popleft()
                cnt += 1
                
                if not queue:
                    break
        
        # 한번에 배포 가능한 기능들의 총 개수
        answer.append(cnt)
        cnt = 0

    return answer