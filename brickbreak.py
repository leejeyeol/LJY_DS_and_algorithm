# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo
import utils
from itertools import product

def dfs(w, h):
    return 0

def calc_explosion(brick, h, w):

    return 0
def drop_bricks(brick):
    return 0
def calc_remained_bricks(brick):
    return 0

def solution(test_case, N, W, H, brick):
    min_remained_bricks = 9999
    # 블록이 가장 적게 남았을 때 얼마나 남았는지 저장. 대충 큰 수로 초기화
    for set in list(product([num for num in range(W)], repeat=N)):
        # 완전 탐색을 위한 중복 순열
        non_brick_flag = False
        set_brick = brick.copy()
        for i in range(N):
            # set[i] = 이번 set 이번 단계에서 구슬을 쏜 위치
            w = set[i]
            for h in range(H):
                if set_brick[h][w] != 0:
                    # 구슬에 맞은 벽돌에 대해
                    calc_explosion(set_brick, h, w)
                    break
            # 만약 구슬을 쏜 위치에 아무것도 없다면 즉시 break 후 해당 set을 결과에서 제외.
            non_brick_flag = True
            break

        if non_brick_flag is False:
            remained_bricks = calc_remained_bricks(set_brick)
            if remained_bricks < min_remained_bricks :
                min_remained_bricks = remained_bricks
    return 0

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