from numpy import inf
from graph import graph

def brent(graph):
    vertices = graph.getVertices()
    # start with power and lambda equal to 1
    power = lam = 1
    # start slow at the first node and fast at the second
    slow_node = next(iter(vertices))
    fast_node = next(iter(vertices))
    fast_node = graph.getNeighbours(fast_node)[0]

    while fast_node != slow_node:
        if power == lam:
            slow_node = fast_node
            power *= 2
            lam = 0

        # move fast
        # if fast reached the end, no cycle was found
        fast_node = graph.getNeighbours(fast_node)[0]
        if fast_node == None:
            return None
        
        lam += 1
        
    # start both at the first node
    slow_node = next(iter(vertices))
    fast_node = next(iter(vertices))

    # set fast lambda moves apart from slow
    for i in range(lam):
        fast_node = graph.getNeighbours(fast_node)[0]

    # next, fast and slow move at same speed until they agree
    moves = 0
    while fast_node != slow_node:
        slow_node = graph.getNeighbours(slow_node)[0]
        fast_node = graph.getNeighbours(fast_node)[0]
        moves += 1

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
cycle_node = brent(g)
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
cycle_node = brent(g)
print('cycle started at node={}'.format(cycle_node))