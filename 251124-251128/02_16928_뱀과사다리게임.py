from collections import deque

def solution(N, M, moves, visited, min_cnt):
    result= 10000000
    queue= deque()
    queue.append([1, 0]) # 현재 인덱스, cnt

    while(queue):
        current, cnt= queue.popleft()

        if(current==100 and result>cnt):
            result= cnt
            break
        if(current>100):
            break


        for i in range(1, 7):
            new_current= current+i
            new_cnt= cnt+1

            flag= 1

            if(visited[new_current]==0): # 해당 위치가 처음 방문된 곳이라면
                visited[new_current]=1
                min_cnt[new_current]= new_cnt
            else: # 이미 방문이 한 번 되었던 곳이라면
                if(min_cnt[new_current]>new_cnt): # 기존 > 새로운
                    min_cnt[new_current]= new_cnt
                else:
                    flag= 0

            # 뱀이나 사다리가 있다면 해당 위치로 이동시켜야 함
            if(flag==1):
                for move in moves:
                    if(move[0]==new_current): # 해당 위치에 뱀이나 사다리가 있는 경우
                        new_current= move[1]

                        if(visited[new_current]==0):  # 해당 위치가 처음 방문된 곳이라면
                            visited[new_current]= 1
                            min_cnt[new_current]= new_cnt
                        else:  # 이미 방문이 한 번 되었던 곳이라면
                            if(min_cnt[new_current]>cnt):  # 기존 > 새로운
                                min_cnt[new_current]= new_cnt
                            else:
                                flag= 0
                        break

            if(flag==1):
                queue.append([new_current, new_cnt])

    return result




## main ##
N, M= map(int, input().split()) # 사다리의 수, 뱀위 수
visited= [0 for _ in range(110)]
min_cnt= [0 for _ in range(110)]
moves= []
for i in range(N):
    start, end= map(int, input().split())
    moves.append([start, end])
for i in range(M):
    start, end= map(int, input().split())
    moves.append([start, end])

print(solution(N, M, moves, visited, min_cnt))


