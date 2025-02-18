"""
A script with an algorithm that removes the least number
of nodes so that no edges are left.
"""
# Import libraries
import networkx as nx
from itertools import combinations


def remove_edges(data):
    """
    A function that removes the least number of nodes
    so that no edges are left.
    """
    # Create a graph
    G = nx.from_pandas_edgelist(data, source="node1", target="node2")

    # Get all nodes in the graph
    nodes = list(G.nodes())
    # Print the nodes
    print(nodes)
    # Set minimun nodes to None
    min_nodes = None

    # Check all possible subsets of nodes starting from the smallest size
    for size in range(len(nodes) + 1):
        print(f"\n\nThis is the size {size}\n\n")
        # Generate all the combinations 
        for subset in combinations(nodes, size):
            print(subset)
            # Check for each of the subset of the edges
            is_cover: bool = all(u in subset or v in subset for u, v in G.edges())
            # If its true
            if is_cover==True:
                # Defient the subset with minimun nodes removal
                min_nodes = set(subset)
                # Break if is True
                break
        # Break if minimum nodes have been found 
        if min_nodes is not None:
            break

    # Display the nodes that will be removed
    print("Nodes removed:", min_nodes)

    # Remove the nodes from the graph
    G.remove_nodes_from(min_nodes)

    # Verify that no edges remain
    assert len(G.edges()) == 0, "Edges still remain!"

    # Reture the nodes
    return min_nodes


if __name__=="__main__":
    remove_edges()
