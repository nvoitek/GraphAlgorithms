from collections import defaultdict
from collections import namedtuple

# adjacency list graph

class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def getVertices(self):
        return list(self.gdict.keys())

    def getEdges(self):
        edges = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edges:
                    Edge = namedtuple('Edge', ['fromVrtx', 'toVrtx', 'edgeWeight']) 
                    edges.append(Edge(vrtx, nxtvrtx, self.gdict[vrtx][nxtvrtx]))
        return edges

    def getNeighbours(self, vrtx):
        return self.gdict[vrtx]
