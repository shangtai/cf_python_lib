class UnionFind:
    def __init__(self, n):
        self.setSize = [1] * n
        self.numSets = n
        self.rank = [0] * n
        self.p = [i for i in range(n)]
    def findSet(self, i):
        if self.p[i] == i:
            return i
        else:
            self.p[i] = self.findSet(self.p[i])
            return self.p[i]
    def isSameSet(self, i, j):
        return self.findSet(i) == self.findSet(j)
    def unionSet(self, i, j):
        if not self.isSameSet(i, j):
            self.numSets -= 1
            x = self.findSet(i)
            y = self.findSet(j)
            if self.rank[x] > self.rank[y]:
                self.p[y] = x
                self.setSize[x] += self.setSize[y]
            else:
                self.p[x] = y
                self.setSize[y] += self.setSize[x]
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1
    def numDisjointSets(self):
        return self.numSets
    def sizeOfSet(self, i):
        return self.setSize[self.findSet(i)]
