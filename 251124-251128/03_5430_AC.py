'''
R(뒤집기): 배열의 순서를 뒤집는다
D(버리기): 배열의 첫 번째 수를 버린다.

배열을 실제로 뒤집는 것보다는 현재 기준으로 배열을 정의하고
flag 변수를 활용해 역순인지 아닌지를 판단하는 것이 좋아보인다.

lst= [1,2,3,4,5]

flag=1인 경우
R: flag=0으로 변경
D: lst.popleft()

flag=0인 경우
R: flag=1로 변경
D: lst.pop()

D를 수행하기 전에는 반드시 lst의 사이즈를 확인한다.
'''

from collections import deque

def solution(p, n, lst): # 명령어, len(lst), 숫자
    flag= 1

    for order in p:
        if(flag==1):
            if(order=="R"):
                flag= 0
            else:
                if(len(lst)<=0):
                    return "error"
                lst.popleft()
        else:
            if(order=="R"):
                flag= 1
            else:
                if(len(lst)<=0):
                    return "error"
                lst.pop()

    lst= list(lst)
    if(flag==0):
        lst.reverse()
    # return lst
    return "[" + ",".join(lst) + "]"

## main ##
T= int(input())

for _ in range(T):
    p= list(input().strip())
    n= int(input())
    lst= list(input().strip())

    if(n==0):
        empty_list= deque()
        print(solution(p, 0, empty_list))
    else:
        lst= lst[1:-1]
        lst_str= ""
        for a in lst:
            lst_str+=a

        lst= deque(list(lst_str.split(",")))
        print(solution(p, n, lst))



