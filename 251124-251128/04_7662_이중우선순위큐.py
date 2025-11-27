from collections import deque


def solution(k, orders):
    # print(orders)
    lst= deque()

    for order in orders:
        if(order[0]=="I"): # 삽입일 때
            if(len(lst)==0): # lst가 비어있는 경우
                lst.append(order[1])
            else: # lst가 비어있지 않은 경우
                start= 0
                end= len(lst)-1
                while(start<=end):
                    mid= (start+end)//2

                    if(lst[mid]<order[1]):
                        start= mid+1

                    else:
                        end= mid-1

                lst.insert(start, order[1])


        else: # 삭제일 때
            # print("delete")
            if(order[1]==-1): # 최솟값 삭제
                if(len(lst)>0):
                    lst.popleft()
            else: # 최댓값 삭제
                if(len(lst)>0):
                    lst.pop()

    len_lst= len(lst)
    if(len_lst==0):
        print("EMPTY")
    elif(len_lst==1):
        print(lst[0], lst[0])
    else:
        print(lst[-1], lst[0])


## main ##
T= int(input())
for t in range(T):
    k= int(input())
    orders= []
    for _ in range(k):
        order= list(input().split())
        order[1]= int(order[1])
        orders.append(order)

    solution(k, orders)
