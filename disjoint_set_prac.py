# Disjoint Set with path compression and size tracking
from function_visualizer import FunctionVisualizer

visualizer = FunctionVisualizer()


class DisjointSet:
    def __init__(self):
        self.parent = dict()
        self.size = dict()

    @visualizer.visualize(param_names=["x"])
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root != y_root:
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1

    def get_size(self, x):
        return self.size[self.find(x)]

# 테스트
ds = DisjointSet()

relations = [
    ("Fred", "Barney"),
    ("Barney", "Betty"),
    ("Betty", "Wilma")
]

for a, b in relations:
    ds.add(a)
    ds.add(b)
    ds.union(a, b)
    print(f"{a}와 {b}의 네트워크 크기:", ds.get_size(a))

visualizer.render("disjoint-set")