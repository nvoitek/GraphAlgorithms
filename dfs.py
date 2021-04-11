from graph import graph

def bfs(graph):
    # all vertices are not vistied at the start
    visited = [False] * len(graph.graph)

    # using queue because we will take elements from the front while adding to the back
    queue = []

    # pick the source node to start with
    source = next(iter(graph.graph[0]))

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
        for i in graph.graph[source]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

g = graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

bfs(g)