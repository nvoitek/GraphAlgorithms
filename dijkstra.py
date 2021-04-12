from numpy import inf
from graph import graph

def dijkstra(graph, source, target):
    # all vertices are not vistied at the start
    vertices = graph.getVertices()

    # distances set to max, nodes marked as unvisited
    distances = dict.fromkeys(vertices, inf)
    visited = dict.fromkeys(vertices, False)
    # pick the source node distance to 0
    distances[source] = 0

    parents = {}

    nextNode = source

    # for a given node we look at the neighbours and if the distance is to the neighbour is lower than the recorded one then we update our distance dictionary
    # in the first survey all distances will be updated and all steps will be recorded
    while nextNode != target:
        for neighbour in graph.getNeighbours(nextNode):
            if neighbour in distances and distances[neighbour] > graph.getNeighbours(nextNode)[neighbour] + distances[nextNode]:
                distances[neighbour] = graph.getNeighbours(nextNode)[neighbour] + distances[nextNode]
                parents[neighbour] = nextNode

        # once a node has been explored it is no longer a candidate for stepping to as paths cannot loop back onto themselves
        del distances[nextNode]

        # we then determine the shortest path we can pursue by looking for the minimum element of our distances dictionary
        nextNode = min(distances, key=distances.get)


    node = target
    backpath = [target]

    while node != source:
        backpath.append(parents[node])
        node = parents[node]
    
    backpath.reverse()

    return backpath

graph_elements = { "a" : {"b" : 4, "c" : 2, "d" : 3, "e" : 1, "f" : 1},
                "b" : {"a" : 4, "f" : 2, "g" : 3},
                "c" : {"a" : 2, "h" : 2},
                "d" : {"a" : 3},
                "e" : {"a" : 1},
                "f" : {"a" : 1, "b" : 2},
                "g" : {"b" : 3, "h" : 1},
                "h" : {"c" : 2, "g" : 1}
                }
                
g = graph(graph_elements)
result = dijkstra(g, "a", "g")
print('shortest path={}'.format(result))