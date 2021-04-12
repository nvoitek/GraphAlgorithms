from numpy import inf
from graph import graph

def floyd(graph):
    vertices = graph.getVertices()
    # start both at the first node
    slow_node = next(iter(vertices))
    fast_node = next(iter(vertices))

    while (True):
        # move fast twice
        # if fast reached the end, no cycle was found
        fast_node = graph.getNeighbours(fast_node)[0]
        if fast_node == None:
            return None
            
        fast_node = graph.getNeighbours(fast_node)[0]
        if fast_node == None:
            return None

        # move slow once
        slow_node = graph.getNeighbours(slow_node)[0]

        # if fast and slow met, that means there is a cycle
        if fast_node == slow_node:
            break
    
    # create a new slow at the start
    temp_node = next(iter(vertices))

    # move two slow until they meet
    while temp_node != slow_node:
        temp_node = graph.getNeighbours(temp_node)[0]
        slow_node = graph.getNeighbours(slow_node)[0]
        
    # where they met is the beginning of the cycle
    return slow_node

graph_elements = { "a" : ["b"],
                "b" : ["c"],
                "c" : ["d"],
                "d" : ["e"],
                "e" : ["f"],
                "f" : ["g"],
                "g" : ["h"],
                "h" : [ None ]
                }

g = graph(graph_elements)
cycle_node = floyd(g)
print('cycle started at node={}'.format(cycle_node))

graph_elements = { "a" : ["b"],
                "b" : ["c"],
                "c" : ["d"],
                "d" : ["e"],
                "e" : ["f"],
                "f" : ["g"],
                "g" : ["h"],
                "h" : ["e"]
                }
                
g = graph(graph_elements)
cycle_node = floyd(g)
print('cycle started at node={}'.format(cycle_node))