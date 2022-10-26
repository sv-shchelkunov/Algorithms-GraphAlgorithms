import math
from graph_algorithms import BreadthFirstSearch as BFS

# this DUNGEON map is from https://www.youtube.com/watch?v=09_LlHjoEiY&t=11342s
# see 48:38 / 6:44:39
DUNGEON = [
[0,0,0,1,0,0,0],
[0,1,0,0,0,1,0],
[0,1,0,0,0,0,0],
[0,0,1,1,0,0,0],
[1,0,1,0,0,1,0],
]

def getNxNyEtc(d):
    Ny =  len(d)
    Nx = len(d[0])
    count = Nx * Ny
    return {'count': count, 'nx': Nx, 'ny': Ny}

def getNodes(d):
    count, Nx, Ny = getNxNyEtc(d).values()
    return [v for v in range(count)]

def getXY(cell, d):
    count, Nx, Ny = getNxNyEtc(d).values()
    y = math.floor(cell / Nx)
    x = math.ceil(cell - (y*Nx))
    return (x, y)

def getCell(x, y, d):
    count, Nx, Ny = getNxNyEtc(d).values()
    return x + (y*Nx)

def getNeighbors(cell, d):
    count, Nx, Ny = getNxNyEtc(d).values()
    if cell < 0 or cell >= count:
        return []

    return list(filter(
        lambda x: x >= 0 and x < count,
        [cell-1, cell+1, cell-Nx, cell+Nx]))

def getOpenNeighbors(cell, d):
    neighbors = getNeighbors(cell, d)
    neighborsXY = [getXY(_each, d) for _each in neighbors]
    availableXY = filter(
        lambda xy: d[xy[1]][xy[0]] == 0,
        neighborsXY)
    return [getCell(xy[0], xy[1], d) for xy in availableXY]

def getEdges(d):
    nodes = getNodes(d)
    edges = {v: {} for v in nodes}

    for cell in nodes:
        x, y = getXY(cell, d)
        if d[y][x] != 0: continue
        for u in getOpenNeighbors(cell, d):
            edges[cell][u] = 1

    return edges

if __name__ == "__main__":
    nodes = getNodes(DUNGEON)
    edges = getEdges(DUNGEON)
    start = getCell(0, 0, DUNGEON)
    end = getCell(3, 4, DUNGEON)
    esc_path = BFS(nodes, edges, start, end, show=True).findPath()
    esc_pathXY = [getXY(v, DUNGEON) for v in esc_path]
    print('path(x,y) =:', esc_pathXY)
    # algorithm =: Breadth First Search
    # start =: 0
    # end =: 31
    # path =: [0, 1, 2, 9, 10, 11, 18, 25, 32, 31]
    # [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3), (4, 4), (3, 4)]

    # print(getNxNyEtc(DUNGEON))
    # print(getXY(34, DUNGEON))
    # print(getCell(6,4, DUNGEON))
    # print(getNeighbors(34, DUNGEON))
    # print(getOpenNeighbors(34, DUNGEON))
    # print(getEdgeInfo(DUNGEON))
    # print(getNodes(DUNGEON))
# [
# [
# [
# [
# [
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
# ]
# ]
# ]
# ]
# ]
