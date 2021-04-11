from graph import graph

def bfs(graph):
    # all vertices are not vistied at the start
    vertices = graph.getVertices()

    # using queue because we will take elements from the front while adding to the back
    queue = []

    # visited nodes will be marked in the dictionary
    visited = dict.fromkeys(vertices, False)

    # pick the source node to start with
    source = next(iter(vertices))

    # mark the source node as visited and enqueue it
    visited[source] = True
    queue.append(source)

    # while there are elements in the queue
    while queue:
        # dequeue an element and print it
        source = queue.pop(0)
        print (source, end = " ")

        # then take all adjacent elements that weren't visited
        # mark them as visited and add them to the back
        # this way we are looking at the shallow elements first
        for i in graph.getNeighbours(source):
            if not visited[i]:
                visited[i] = True
                queue.append(i)

graph_elements = { "a" : ["b","c","d","e"],
                "b" : ["a", "f", "g"],
                "c" : ["a", "h"],
                "d" : ["a"],
                "e" : ["a"],
                "f" : ["b"],
                "g" : ["b"],
                "h" : ["c"]
                }

g = graph(graph_elements)

bfs(g)