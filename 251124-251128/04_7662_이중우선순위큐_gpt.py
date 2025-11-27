import heapq

def solution(k, orders):
    min_h = []
    max_h = []
    visited = [False] * k  # 각 연산별로 id 부여

    for idx, order in enumerate(orders):
        cmd, num = order[0], order[1]

        if cmd == "I":
            heapq.heappush(min_h, (num, idx))
            heapq.heappush(max_h, (-num, idx))
            visited[idx] = True

        else:  # cmd == "D"
            if num == 1:  # 최대값 삭제
                while max_h and not visited[max_h[0][1]]:
                    heapq.heappop(max_h)
                if max_h:
                    _, del_id = heapq.heappop(max_h)
                    visited[del_id] = False

            else:  # num == -1, 최소값 삭제
                while min_h and not visited[min_h[0][1]]:
                    heapq.heappop(min_h)
                if min_h:
                    _, del_id = heapq.heappop(min_h)
                    visited[del_id] = False

    # 최종 정리
    while min_h and not visited[min_h[0][1]]:
        heapq.heappop(min_h)
    while max_h and not visited[max_h[0][1]]:
        heapq.heappop(max_h)

    if not min_h or not max_h:
        print("EMPTY")
    else:
        print(-max_h[0][0], min_h[0][0])


## main ##
from collections import deque

T= int(input())
for t in range(T):
    k= int(input())
    orders= []
    for _ in range(k):
        order= list(input().split())
        order[1]= int(order[1])
        orders.append(order)

    solution(k, orders)
