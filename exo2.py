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

    def set_step(self, step):
        self.step = step

    def maj(self, line):
        self.biais += self.step * (line[len(line)-1]- self.out) * -0.5
        for x in range(len(line)-1):
            self.w[x] += self.step * (line[len(line)-1]- self.out) * line[x]

    def calculersortie(self, line, maj):
        score = 0.0
        for x in range(2):
            score += self.w[x]*line[x]
        score -= self.biais
        if score > 0:
            self.out = 1
        else:
            self.out = -1
        if self.out != line[len(line)-1] and maj == True:
            self.maj(line)
        return self.out

def app(neurone, datas):

    ErrorsList = []
    nberrors = 1

    while nberrors != 0:
        nberrors = 0

        for y in range(len(datas)):
            end = neurone.calculersortie(datas[y],maj=True)

            if end != datas[y][2]:
                nberrors += 1

        print(nberrors)
        ErrorsList.append(nberrors);

    return ErrorsList

def generalisation(neurone, datas):

        nberrors = 0

        for y in range(len(datas)):
            end = neurone.calculersortie(datas[y],maj=False)

            if end != datas[y][2]:
                nberrors += 1

        print(nberrors)

def lines(datas):

    plt.plot(datas)
    plt.show()




myneurone = NeuroneStruct(0,0.5,2)
app_datas = np.genfromtxt('app.csv', delimiter=' ')
errorsarray=app(myneurone, app_datas)
print("Generalisation -----------------------")
gen_datas = np.genfromtxt('gen.csv', delimiter=' ')
generalisation(myneurone,gen_datas)


lines(errorsarray)
