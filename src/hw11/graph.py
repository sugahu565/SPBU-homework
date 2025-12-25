class Graph:
    def __init__(self, edges: dict[int, list[int]]):
        self.number_vertex = len(edges)
        self.edges = edges
        self.ind = 0
        self.order = []


    def dfs_order(self, vert):
        if vert not in self.edges:
            print("no vertex")
            return []

        order_dfs = []
        visited = set()


        def dfs(now):
            visited.add(now)
            order_dfs.append(now)
            for to in self.edges[now]:
                if to not in visited:
                    dfs(to)

        dfs(vert)
        return order_dfs


    def get_dfs_order(self, vert):
        self.ind = 0
        self.order = self.dfs_order(vert)


    def __iter__(self):
        return self


    def __next__(self):
        # предварительно необходимо использовать get_dfs_order
        stop = len(self.order)
        if self.ind < stop:
            r = self.order[self.ind]
            self.ind += 1
            return r
        raise StopIteration
