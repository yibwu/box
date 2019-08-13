class UnionFind:
    
    def __init__(self, size):
        self.nums = [-1 for _ in range(size + 1)]

    def find(self, x):
        if self.nums[x] < 0:
            return x 
        else:
            self.nums[x] = self.find(self.nums[x])
            return self.nums[x]
            
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        else:
            self.nums[px] += self.nums[py]
            self.nums[py] = px

    def count(self, x):
        px = self.find(x)
        return abs(self.nums[px])


if __name__ == '__main__':
    obj = UnionFind(100)
    obj.union(1, 2)
    obj.union(2, 3)
    print(obj.find(1) == obj.find(2))
    print(obj.find(2) == obj.find(3))
    print(obj.count(2))
    print(obj.count(1))
