class QuickFind():
    def __init__(self, N):
        self.id = {}
        for i in range(N):
            self.id[i] = i

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]

        for key in self.id:
            if self.id[key] == pid:
                self.id[key] = qid
