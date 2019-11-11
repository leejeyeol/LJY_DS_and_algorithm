class Test_envs():
    def __init__(self, filename):
        self.filename = filename
        self.load_test_input_output()
    def load_test_input_output(self):
        with open(r'data/%s'%self.filename, 'r') as f:
            x = f.read().splitlines()
        diidx = x.index('-')
        self.input = x[:diidx]
        self.output = x[diidx+1:]

