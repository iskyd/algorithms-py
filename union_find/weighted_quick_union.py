class WeightedQuickUnion():
    def __init__(self, N):
        self.id = {}
        for i in range(N):
            self.id[i] = {'root': i, 'size': 1}

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)

        parent, child = (j, i) if self.id[i]['size'] < self.id[j]['size'] else (i, j)

        self.id[child]['root'] = self.id[parent]['root']
        self.id[parent]['size'] += self.id[child]['size']

    def root(self, i):
        while(i != self.id[i]['root']):
            i = self.id[i]['root']

        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)