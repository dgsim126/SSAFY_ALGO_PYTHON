


## git thset
## main ##
M, N, H= map(int, input().split()) # 가로, 세로, 높이
box= [] # 토마토를 담은 곳

for i in range(H):
    floor= []
    for j in range(N):
        row= list(map(int, input().split()))
        floor.append(row)
    box.append(floor)

solution()
