class UnionFindSet():
    def __init__(self, n):
        self.ranks = [0] * (n + 1)
        self.parents = [i for i in range(n + 1)] 
    
    # Merge sets that contains u and v
    # Return True if merged, False if u and v are alread in one set
    def Union(self, u, v):
        pu = self.Find(u)
        pv = self.Find(v)
        if pu == pv:
            return False 

        # Merge low rank tree into high rank tree
        if self.ranks[pv] < self.ranks[pu]:
            self.parents[pv] = pu
        elif self.ranks[pv] > self.ranks[pu]:
            self.parents[pu] = pv
        else:
            self.parents[pv] = pu
            self.ranks[pu] += 1
        return True
    
    # Get the parent / root of u
    def Find(self, u):
        # Compress the path during traversal
        if u != self.parents[u]:
            self.parents[u] = self.Find(self.parents[u])
        return self.parents[u]