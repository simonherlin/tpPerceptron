import random
import numpy as np

class NeuroneStruct:
    def __init__(self, biais, out, lengthofw):
        self.biais = biais
        self.out = out
        self.w = np.random.rand(lengthofw)
        self.step= 0.01
        #self.step= 0.00001
        #self.step= 0.08
        #self.step= 0.5

    def get_step(self):
        return self.step

    def set_x(self, step):
        self.step = step

    def maj(self, line):
        self.biais += self.step * (line[len(line)-1]- self.out) * -0.5
        for x in range(len(line)-1):
            self.w[x] += self.step * (line[len(line)-1]- self.out) * line[x]

    def calculersortie(self, line):
        score = 0.0
        for x in range(2):
            score += self.w[x]*line[x]
        score -= self.biais
        if score > 0:
            self.out = 1
        else:
            self.out = -1
        if self.out != line[len(line)-1]:
            self.maj(line)
        return self.out

def run(w):
    d = NeuroneStruct(0,0.5,2)
    my_data = np.genfromtxt('result.txt', delimiter=' ')
    for x in range(100):
        nberrors = 0
        for y in range(len(my_data)):
            end = d.calculersortie(my_data[y])
            if end != my_data[y][2]:
                nberrors += 1
        print(nberrors)

run(2)
