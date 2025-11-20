'''
색상은 R G B
적록색약은 (R G) (B) 두 개로 구분
일반은 (R) (G) (B)로 구분

문제해결
bsf를 돌면서 구역을 나눈다.

그런데 어떻게 하면 좀 더 효율적으로 두 개를 돌릴 수 있을까?
그냥 bfs를 두 번 돌리는 방법 밖에는 없나?

N의 사이즈가 100이라 2번 돌려도 시간이 문제되지는 않을 것 같다.
'''
from collections import deque

def solution(N, maps, visited, normal, un_normal):
    dy= [-1, 0, 1, 0] # 북 동 남 서
    dx= [0, 1, 0, -1]

    # 적녹색약 아닌
    queue= deque()

    for y in range(N):
        for x in range(N):
            if(visited[y][x]==0):
                queue.append([y, x])
                normal+=1
                visited[y][x]=1

            while(len(queue)!=0):
                temp= queue.popleft()
                for i in range(4):
                    n_y= temp[0]+dy[i]
                    n_x= temp[1]+dx[i]

                    if(0<=n_y<N and 0<=n_x<N and
                            visited[n_y][n_x]==0 and
                            maps[n_y][n_x]==maps[temp[0]][temp[1]]):
                        visited[n_y][n_x]= 1
                        queue.append([n_y, n_x])

    # 적녹색약
    visited = [[0 for _ in range(N)] for _ in range(N)]
    queue = deque()

    for y in range(N):
        for x in range(N):
            if (visited[y][x] == 0):
                queue.append([y, x])
                un_normal += 1
                visited[y][x] = 1

            while (len(queue) != 0):
                temp = queue.popleft()
                for i in range(4):
                    n_y = temp[0] + dy[i]
                    n_x = temp[1] + dx[i]

                    if (0 <= n_y < N and 0 <= n_x < N and
                            visited[n_y][n_x] == 0):
                        if((maps[y][x] in ["R", "G"] and maps[n_y][n_x] in ["R", "G"]) or (maps[n_y][n_x]==maps[temp[0]][temp[1]])):
                            visited[n_y][n_x] = 1
                            queue.append([n_y, n_x])



    print(normal, un_normal)




## main ##
N= int(input()) # 한 변의 크기
maps= []
visited= [[0 for _ in range(N)] for _ in range(N)] # 방문여부 처리

normal= 0; # 적녹색약 x
un_normal= 0; # 적녹색약

for i in range(N):
    maps.append(list(input().strip()))

solution(N, maps, visited, normal, un_normal)
