# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo
import utils
import copy
from itertools import product

def find_adj_node(h, w, explosion_value):
    if explosion_value == 1:
        return []
    else:
        adj_nodes = []
        # 범위를 벗어날 경우 인접 노드에서 제외
        for i in range(1,explosion_value):
            if w + i < W:
                adj_nodes.append((h,w+i))
            if w - i >= 0:
                adj_nodes.append((h,w-i))
            if h + i < H:
                adj_nodes.append((h+i,w))
            if h - i >= 0:
                adj_nodes.append((h-i, w))
        return adj_nodes

def dfs(brick, h, w, dfs_visited_list):
    dfs_stack = []
    # 해당 블럭의 폭발력을 얻고 0으로 바꿈.
    explosion_value = brick[h][w]
    brick[h][w] = 0
    dfs_visited_list.append((h, w))
    dfs_stack.extend(find_adj_node(h, w, explosion_value))
    while dfs_stack:
        check_point = dfs_stack.pop()
        if check_point not in dfs_visited_list:
            dfs(brick, check_point[0], check_point[1], dfs_visited_list)

def calc_explosion(brick, h, w):
    dfs_visited_list = []
    dfs(brick, h, w, dfs_visited_list)

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

def calc_remained_bricks(brick):
    num_all_brick = H * W
    num_zero = 0
    for h in range(H):
        num_zero += brick[h].count(0)
    remained_bricks = num_all_brick - num_zero
    return remained_bricks

def solution(test_case, N, W, H,ori_brick):
    min_remained_bricks = 9999

    # 블록이 가장 적게 남았을 때 얼마나 남았는지 저장. 대충 큰 수로 초기화
    for set in list(product([num for num in range(W)], repeat=N)):
        # 완전 탐색을 위한 중복 순열
        set_brick = copy.deepcopy(ori_brick)
        for i in range(N):
            if calc_remained_bricks(set_brick) == 0:
                min_remained_bricks = 0
            # set[i] = 이번 set 이번 단계에서 구슬을 쏜 위치
            w = set[i]
            is_non_brick = True
            for h in range(H):
                if set_brick[h][w] != 0:
                    # 구슬에 맞은 벽돌에 대해 같이 터지는 블록들을 계산
                    calc_explosion(set_brick, h, w)
                    # 폭발이 계산된 후 남는 블록의 개수 계산.
                    remained_bricks = calc_remained_bricks(set_brick)
                    if remained_bricks is not 0:
                        drop_bricks(set_brick)
                    is_non_brick = False
                    break
            if is_non_brick:
                # 만약 구슬을 쏜 위치에 모든 h가 0이라면 break 후 해당 set을 결과에서 제외하기 위해 flag 저장.
                break
        if not is_non_brick :
            # 구슬을 쏜 위치에 아무것도 없었던 set을 제외하고, 현재 까지 가장 적게 블록이 남은 set일 경우 최소값 갱신
            if remained_bricks < min_remained_bricks:
                min_remained_bricks = remained_bricks
        if min_remained_bricks == 0:
            break

    print("#%d %d"%(test_case,min_remained_bricks))

env = utils.Test_envs("brickbreak")
T = int(env.input[env.case_start_index])
env.index_up()
for test_case in range(T):
    N, W, H = map(int, env.input[env.case_start_index].split(' '))
    env.index_up()
    brick = []
    for i in range(H):
        brick.append(list(map(int,env.input[env.case_start_index].split())))
        env.index_up()
    answer = env.output[test_case]
    print('-------------')
    solution(test_case, N, W, H, brick)
    print(answer)
'''
완전탐색으로 풀기
N이 1~4밖에 안된다. 따라서 고를 수 있는 경우의 수는 많지 않다.
최악의 경우(N=4 W=12 h=15에 벽돌이 전부 차있을 때)에도 중복순열로 20736가지밖에 안된다.

어느 w에 구슬을 쏠 것인지를 중복조합으로 하여 각각의 시뮬레이션을 실행한다.
해당 w에 벽돌이 없을수도 있다(처음부터 없거나 전부 깨버렸을 경우). 이를 경우의 수에서 제외할 수 있따.
구슬은 발사되고 맨 위의 벽돌을 맞추며, 벽돌이 연쇄작용을 일으킨다면 이를 고려한다.
dfs로 이를 구할 수 있다. 어차피 연결된 모든 그래프를 순회해야함으로 dfs가 적절해보인다.
<=bfs로 구현하는경우도 있던데 왜 그런지 생각해보자..

폭발이 끝난 경우 폭발이후 벽돌을 아래쪽으로 내리는 과정을 수행해줘야한다.

모든 블록이 사라지는 경우를 예외처리해줘야 함 


'''