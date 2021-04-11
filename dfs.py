from graph import graph

def bfs(graph):
    # all vertices are not vistied at the start
    visited = [False] * len(graph.graph)

    # using stack because we will take elements and add elements to the front
    stack = []

    # pick the source node to start with
    source = next(iter(graph.graph[0]))

    # mark the source node as visited and put it on the stack
    visited[source] = True
    stack.append(source)

    # while there are elements in the stack
    while stack:
        # take element off the stack and print it
        source = stack.pop()
        print (source, end = " ")

        # then take all adjacent elements that weren't visited
        # mark them as visited and add them to the back
        # this way we are looking at the shallow elements first
        for i in graph.graph[source]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)

g = graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

bfs(g)