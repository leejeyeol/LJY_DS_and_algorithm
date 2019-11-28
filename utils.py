import sys
class Test_envs():
    def __init__(self, filename):
        self.filename = filename
        self.load_test_input_output()
        self.case_start_index = 0
    def index_up(self):
        self.case_start_index = self.case_start_index + 1

    def load_test_input_output(self):
        with open(r'data/%s'%self.filename, 'r') as f:
            x = f.read().splitlines()
        diidx = x.index('-')
        self.input = x[:diidx]
        self.output = x[diidx+1:]

