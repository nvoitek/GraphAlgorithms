from graph import graph

def dfs(graph):
    # all vertices are not vistied at the start
    vertices = graph.getVertices()

    # using stack because we will take elements and add elements to the front
    stack = []

    # visited nodes will be marked in the dictionary
    visited = dict.fromkeys(vertices, False)

    # pick the source node to start with
    source = next(iter(vertices))

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
        for i in graph.getNeighbours(source):
            if not visited[i]:
                visited[i] = True
                stack.append(i)

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

dfs(g)