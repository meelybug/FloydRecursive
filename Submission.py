# Define the number of nodes
n = 3
# Use infinity as the large enough value
inf = 99999
# Define the function and the parameters
def FloydRecursive(graph):
    # Define distance as the shortest route between each node
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    # Find the distances between node using each of the nodes as the source node
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Account for k being between i and j on shortest distance path
                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist [k][j]
                                 )

