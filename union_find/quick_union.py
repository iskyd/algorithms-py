class QuickUnion():
    def __init__(self, N):
        self.id = {}
        for i in range(N):
            self.id[i] = i

    def union(self, p, q):
        self.id[q] = p

    def root(self, i):
        while(i != self.id[i]):
            i = self.id[i]

        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)