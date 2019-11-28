# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRUN9KfZ8DFAUo#none
import utils
def solution(test_case, N, K, question):
    answer_list = []
    num_rotation = len_num = int(N/4)
    dou_question = question + question

    for i in range(num_rotation):
        for j in range(4):
            num = dou_question[j*len_num+i:j*len_num+len_num+i]
            if num in answer_list:
                pass
            else:
                answer_list.append(num)
    answer_list.sort(reverse=True)
    print("#%d"%(test_case+1) + " " + str(int("0x"+answer_list[K-1], 16)))





env = utils.Test_envs("treasure_password")
T = int(env.input[0])
for test_case in range(T):
    N, K = map(int, env.input[test_case*2 + 1].split(' '))
    question = env.input[test_case*2 + 2]
    answer = env.output[test_case]
    print('-------------')
    solution(test_case, N, K, question)
    print(answer)
