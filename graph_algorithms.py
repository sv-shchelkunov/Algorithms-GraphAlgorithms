# https://www.youtube.com/watch?v=VnTlW572Sc4
# https://www.youtube.com/watch?v=iFdOKsw6x6A
# https://www.youtube.com/watch?v=lyw4FaxrwHg
# https://www.youtube.com/watch?v=09_LlHjoEiY&t=11342s

from collections import deque


NODES=[0,1,2,3,4,5,6,7,8]

EDGES = {
    0: {1: 1.0, 2: 1.5, 3: 2.0},
    1: {0: 1.0, 3: 0.5, 4: 2.5},
    2: {0: 1.5, 3: 1.5},
    3: {0: 2.0, 1: 0.5, 5: 1.0},
    4: {1: 2.5},
    5: {3: 1.0},
    6: {7: 4.0, 8: 2.5},
    7: {6: 4.0},
    8: {}
}


""" Dijkstra's:
1. graphs can be directional or not, and edges can be weighted;
2. all weights must be positive;
3. will find optimal path form a given node to evey other node;
4. optimal means the the sum of weights is minimal compared to any other path;
5. time complexity of Dijkstra's algorithm is O(
usage: dijkstra(NODES, EDGES, start_node)
"""
def dijkstra(nodes, edges, source, show=False):
    path_way = {v: [] for v in nodes}
    # path_way[source].append(source)
    prev_nodes = {v: None for v in nodes}
    path_len = {v: float('inf') for v in nodes}
    path_len[source] = 0

    # dist = {v: {} for v in nodes}
    # for (x,y), _l in edges.items():
    #     # print(x,y,_l)
    #     dist[x][y] = _l
    #     # dist[y][x] = _l #bidirectional graph
    # print(dist)

    unvisited = [v for v in nodes]
    while len(unvisited) > 0:
        pathes = {v: path_len[v] for v in unvisited}
        best = min(pathes, key=pathes.get) # get key of the shortest distance
        unvisited.remove(best) # make best be visited

        for y, _l in edges[best].items():
            new_path_len = path_len[best] + _l
            if (new_path_len < path_len[y]):
                # path_way[y] = [x for x in path_way[best]] # change the pathway to that of the best
                # path_way[y].append(y) # to complete the pathway, add the node/vertex to it
                prev_nodes[y] = best
                path_len[y] = new_path_len


    for e_node in nodes:
        _node = e_node
        while _node is not None:
            path_way[e_node].insert(0, _node)
            _node = prev_nodes[_node]
        if path_way[e_node][0] != source: # check that we can reach the source
            path_way[e_node] = []

    if show:
        print('\n')
        print('algorithm =:', 'Dijkstra\'s')
        print('source =:', source)
        print('path_ways =:', path_way)
        print('prev_nodes=:', prev_nodes)
        print('path_lens =:', path_len)
    return {'source': source, 'path_way': path_way, 'prev_nodes': prev_nodes, 'path_len': path_len}

""" Bellman-Ford:
1. graphs can be directional or not, and edges can be weighted;
2. the weights can both be positive and negative;
3. will find optimal path form a given node to evey other node;
4. optimal means the the sum of weights is minimal compared to any other path;
6. will detect all negative cycles/loops;
5. time complexity of Bellman-Ford algorithm is O( N ⋅ E )
usage: bellman_ford(NODES, EDGES, start_node)
"""
def bellman_ford(nodes, edges, source, show=False):
    path_way = {v: [] for v in nodes}
    prev_nodes = {v: None for v in nodes}
    path_len = {v: float('inf') for v in nodes}
    path_len[source] = 0

    v_1 = len(nodes) - 1
    for _ in range(v_1):
        for _v in edges:
            for _u, _l in edges[_v].items():
                new_path_len = path_len[_v] + _l
                if (new_path_len < path_len[_u]):
                    prev_nodes[_u] = _v
                    path_len[_u] = new_path_len

    for _ in range(v_1):
        for _v in edges:
            for _u, _l in edges[_v].items():
                new_path_len = path_len[_v] + _l
                if (new_path_len < path_len[_u]):
                    prev_nodes[_u] = _v
                    path_len[_u] = -float('inf')

    for e_node in nodes:
        _node = e_node
        while _node is not None:
            path_way[e_node].insert(0, _node)
            _node = prev_nodes[_node]
        if path_way[e_node][0] != source: # check that we can reach the source
            path_way[e_node] = []

    if show:
        print('\n')
        print('algorithm =:', 'Bellman-Ford')
        print('source =:', source)
        print('path_ways =:', path_way)
        print('prev_nodes=:', prev_nodes)
        print('path_lens =:', path_len)
    return {'source': source, 'path_way': path_way, 'prev_nodes': prev_nodes, 'path_len': path_len}

"""Depth First Search (DFS):
1. graphs can be bi-directional or not (true? not?) depending on application;
2. edges must be without any weights (true? not?);
3. here, it can find the nodes that are connected, but it requires bi-directionality;
4. time complexity of Depth First Search algorithm is O( N + E )
usage: DepthFirstSearch(NODES, EDGES).findComponents()
"""
# since, the method findComponents works correctly only when there are
# no directions, the edges are normalized to become bi-directional (weight = 1)
class DepthFirstSearch():
    def __init__(self, nodes, edges, show=False):
        self.show = show
        self.nodes = nodes
        self.edges = self.normalizeEdges(nodes, edges)
        # self.source = source
        self.components = {v: None for v in nodes}
        self.visited = {v: False for v in nodes}
        self.index = -1

    def normalizeEdges(self, nodes, edges):
        norm_edges = {v: {} for v in nodes}
        for v in edges:
            for u, _l in edges[v].items():
                norm_edges[v][u] = 1
                norm_edges[u][v] = 1

        # print('\n')
        # print(norm_edges)
        return norm_edges

    def findComponents(self):
        for v in self.nodes:
            if not self.visited[v]:
                self.index += 1
                self.dfs(v)

        count = self.index + 1
        if self.show:
            print('\n')
            print('algorithm =:','Depth First Search')
            print('count =:', count)
            print('components =:', self.components)
        return {'count': count, 'components': self.components}

    def dfs(self, v):
        self.visited[v] = True
        self.components[v] = self.index

        for u, _l in self.edges[v].items():
            if not self.visited[u]:
                self.dfs(u)

"""Breadth First Search (BFS):
1. graphs must be bi-directional (true? not?);
2. the edges must be unweighted (weight = 1);
3. will find optimal path form a given node to another, specified end node;
4. time complexity of Breadth First Search algorithm is O( N + E )
usage: BreadthFirstSearch(NODES, EDGES, start_node, end_node).findPath()
"""
# BFS works correctly only when(?) there is no directions, and edges have no weigth;
# thus, edges are normalized to become bi-directional and have weight = 1
class BreadthFirstSearch():
    def __init__(self, nodes, edges, source, sink, show=False):
        self.show = show
        self.nodes = nodes
        self.edges = self.normalizeEdges(nodes, edges)
        self.source = source
        self.sink = sink
        self.visited = {v: False for v in nodes}
        self.visited[source] = True
        self.prev_nodes = {v: None for v in nodes}

    def normalizeEdges(self, nodes, edges):
        norm_edges = {v: {} for v in nodes}
        for v in edges:
            for u, _l in edges[v].items():
                norm_edges[v][u] = 1
                norm_edges[u][v] = 1

        # print('\n')
        # print(norm_edges)
        return norm_edges

    def solveBFS(self):
        q = deque()
        q.append(self.source)

        while bool(q):
            v = q.popleft()
            for u, _l in self.edges[v].items():
                if not self.visited[u]:
                    q.append(u)
                    self.visited[u] = True
                    self.prev_nodes[u] = v

    def reconstructPath(self):
        path_way = []
        _node = self.sink
        while _node is not None:
            # print(_node)
            path_way.insert(0, _node)
            _node = self.prev_nodes[_node]

        if path_way[0] == self.source:
            return path_way
        return []

    def findPath(self):
        self.solveBFS()
        reconstructed_path = self.reconstructPath()
        if self.show:
            print('\n')
            print('algorithm =:','Breadth First Search')
            print('start =:', self.source)
            print('end =:', self.sink)
            print('path =:', reconstructed_path)
        return reconstructed_path

"""Topological Sort algorithm (Top Sort):
1. graphs are directed (I suppose the edge weight = 1 (or the same for every edge));
2. graphs must have no cycles, that is, be DAG (directed acyclic graphs);
3. an example is a tree (since by definition, a tree cannot have any cycles);
4. to detect cycles, one can use Tarjan's strongly connected component algorithm;
5. topogical orderings are not unique;
6. time complexity of Topological Sort algorithm is O( N + E )
"""
class TopSort():
    def __init__(self):
        pass

if __name__ == "__main__":
    dijkstra(NODES, EDGES, 5, show=True)
# algorithm =: Dijkstra's
# source =: 5
# path_ways =: {0: [5, 3, 1, 0], 1: [5, 3, 1], 2: [5, 3, 1, 0, 2], 3: [5, 3], 4: [5, 3, 1, 4], 5: [5], 6: [], 7: [], 8: []}
# prev_nodes=: {0: 1, 1: 3, 2: 0, 3: 5, 4: 1, 5: None, 6: None, 7: None, 8: None}
# path_lens =: {0: 2.5, 1: 1.5, 2: 4.0, 3: 1.0, 4: 4.0, 5: 0, 6: inf, 7: inf, 8: inf}
    bellman_ford(NODES, EDGES, 5, show=True)

    DepthFirstSearch(NODES, EDGES, show=True).findComponents()

    BreadthFirstSearch(NODES, EDGES, 5, 0, show=True).findPath()
# [
# [
# [
# [
# [
# [
# [
# [
# [
#
# ]
# ]
# ]
# ]
# ]
# ]
# ]
# ]
# ]
