from random import randint
import numpy as np
import math

class Percolation():
    def __init__(self, N):
        self.id = {}
        self.N = N

        N = N * N
        for i in range(N):
            self.id[i] = {'root': i, 'size': 1, 'open': False}

        # Virtual Nodes to improve connected query to check if system percolates
        self.id[N] = {'root': N, 'size': 1, 'open': False}
        self.id[N + 1] = {'root': N + 1, 'size': 1, 'open': False}

        for i in range(self.N):
            self.union(N, i)
        for i in range(self.N):
            self.union(N + 1, (self.N * self.N) - i - 1)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)

        parent, child = (j, i) if self.id[i]['size'] < self.id[j]['size'] else (i, j)

        self.id[child]['root'] = self.id[parent]['root']
        self.id[parent]['size'] += self.id[child]['size']

    def root(self, i):
        while(i != self.id[i]['root']):
            self.id[i]['root'] = self.id[self.id[i]['root']]['root']
            i = self.id[i]['root']

        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def open(self, p):
        self.id[p]['open'] = True
        
        for i in self.get_neighbors(p):
            if self.id[i]['open'] == True:
                self.union(p, i)

    def get_neighbors(self, p):
        neighbors = []

        if (p - 1) >= 0 and (p) % self.N != 0:
            neighbors.append(p - 1)

        if (p + 1) % self.N != 0:
            neighbors.append(p + 1)

        if p - self.N > 0:
            neighbors.append(p - self.N)

        if p + self.N < self.N * self.N:
            neighbors.append(p + self.N)

        return neighbors


if __name__ == '__main__':
    total = 0
    T = 50
    results = []
    for x in range(T):
        p = Percolation(10)
        while(not p.connected(100, 101)):
            p.open(randint(0, 99))
        
        opened = 0
        for i in p.id:
            if p.id[i]['open'] == True:
                opened += 1

        results.append(opened / 100)

    results = np.asarray(results)

    mean = np.mean(results)
    std = np.std(results)

    print('mean: ', mean)
    print('std: ', std)

    # 95% confidence
    confidence = ((1.96 * std) / math.sqrt(T))
    print('confidence interval: [{}-{}]'.format(mean - confidence, mean + confidence))