from numpy import inf
from graph import graph

def bellman_ford(graph, source):
    vertices = graph.getVertices()
    edges = graph.getEdges()

    distances = dict.fromkeys(vertices, inf)
    predecessors = dict.fromkeys(vertices, None)
    distances[source] = 0

    for i in range(len(vertices)-1):
        for edge in edges:
            if distances[edge.toVrtx] > distances[edge.fromVrtx] + edge.edgeWeight:
                distances[edge.toVrtx] = distances[edge.fromVrtx] + edge.edgeWeight
                predecessors[edge.toVrtx] = edge.fromVrtx

    for edge in edges:
            if distances[edge.toVrtx] > distances[edge.fromVrtx] + edge.edgeWeight:
                print("Graph contains a negative-weight cycle")
                break

    backpaths = []
    for i in vertices:
        if i != source:
            node = i
            backpath = [i]

            while node != source:
                backpath.append(predecessors[node])
                node = predecessors[node]
    
            backpath.reverse()

            backpaths.append(backpath)

    return backpaths

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
result = bellman_ford(g, "a")
print('shortest path to each vertex={}'.format(result))

graph_elements = { "a" : {"b" : 1, "c" : 1},
                "b" : {"a" : 1, "d" : 4, "c" : 1},
                "c" : {"a" : 1, "d" : -6, "b" : 1},
                "d" : {"b" : 4, "c" : -6, "e" : 1, "f" : 1},
                "e" : {"d" : 1, "g" : 1, "f" : 1},
                "f" : {"d" : 1, "g" : 1, "e" : 1},
                "g" : {"e" : 1, "f" : 1}
                }
                
g = graph(graph_elements)
result = bellman_ford(g, "a")
print('shortest path to each vertex={}'.format(result))