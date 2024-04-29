# Define the number of nodes
n = 3
# Use infinity as the large enough value
inf = 99999
# Define the function and the parameters
def FloydRecursive(graph)
    # Define distance as the shortest route between each node
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
