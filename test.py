W = 3
H = 3
a=[[1,1,1],[0,1,1],[0,0,1]]

def drop_bricks(brick):
    for w in range(W):
        for h in range(H).__reversed__():
            if brick[h][w] != 0:
                pass
            else:
                for h_offset in range(1, h+1):
                    if brick[h-h_offset][w] == 0:
                        pass
                    else:
                        brick[h][w] = brick[h-h_offset][w]
                        brick[h-h_offset][w] = 0
                        break
drop_bricks(a)
print(1)