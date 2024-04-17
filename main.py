from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        ###TODO
        pass
    return result
def reachable(graph, start_node):
    """
    Returns the set of nodes reachable from start_node
    """
    
    result = set([start_node])
    frontier = set([start_node])

    while len(frontier) != 0:
        current_node = frontier.pop()  # remove and get an element from the frontier
        for neighbor in graph[current_node]:
            if neighbor not in result:
                frontier.add(neighbor)
                result.add(neighbor)

    return result


def connected(graph):
    if not graph:
        return True  # An empty graph is connected
    
    # Start from any node; here we take the first node in the graph dictionary
    start_node = next(iter(graph))
    
    # Use the reachable function to get all nodes reachable from the start node
    reachable_nodes = reachable(graph, start_node)
    
    # The graph is connected if the number of reachable nodes is equal to the number of nodes in the graph
    return len(reachable_nodes) == len(graph)




def n_components(graph):
    """
    Returns the number of connected components in an undirected graph
    """
    visited = set()
    component_count = 0
    
    for node in graph:
        if node not in visited:
            # Node not visited, so it's a start of a new component
            reachable_nodes = reachable(graph, node)
            visited.update(reachable_nodes)
            component_count += 1
            
    return component_count

