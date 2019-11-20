# Enter your code here. Read input from STDIN. Print output to STDOUT
import math


def is_prime(case):
    if case == 1:
        return "Not prime"
    elif case == 2:
        return "Prime"
    elif (case % 2) == 0:
        return "Not prime"
    else:
        for i in range(2, int(math.sqrt(case)) + 1):
            if case % (i) == 0:
                return "Not prime"
    return "Prime"


'''
class Eratosthenes:
    def __init__(self,max_num):
        self.max_num = max_num+1
        self.is_prime_odd = [True for _ in range(int(max_num/2)+1)]
        self.is_prime_odd[0] = False
        self.find_eratosthenes()
    def is_prime(self, value):
        if value == 2 :
            return True
        elif value%2 == 0:
            return False
        else:
            return self.is_prime_odd[int(value/2)]

    def set_false_odd(self, value):
        if value%2 == 0:
            pass
        else:
            self.is_prime_odd[int(value/2)] = False

    def find_eratosthenes(self):
        for i in range(3, int(math.sqrt(self.max_num))):
            if self.is_prime(i) == True:
                for j in range(i*i, self.max_num, i):
                    self.set_false_odd(j)
'''
n = int(input())
def iter_case():
    for _ in range(n):
        yield int(input())

for case in iter_case():
    # print("Prime" if eratos.is_prime(case) else "Not prime")
    print(is_prime(case))