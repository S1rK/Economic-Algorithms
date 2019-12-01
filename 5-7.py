"""
Economic Algorithms
Exercise 5 , Question 7
AUTHOR: Tal Nakar
SINCE:  01-12-2019
"""

import networkx as nx


def vcg_cheapest_path(graph: nx.Graph, source, target):
    """
    A function that prints the cost of every edge in the graph, via VCG algorithm.
    :param graph: A graph.
    :param source: The source node.
    :param target: The target node.
    :return: Nothing, void.
    """
    # first, find the shortest path between the source and the target
    main_path = nx.dijkstra_path(graph, source, target, "weight")
    # convert the main path to contain tuples that represents edges
    main_path = [tuple(main_path[i: i+2]) for i in range(len(main_path)-1)]
    # find it's cost
    main_cost = nx.dijkstra_path_length(graph, source, target, 'weight')

    # now calc every edge's cost
    for (s, t, w) in graph.edges.data('weight'):
        # the edge
        e = (s, t)
        # if the edge in the main path
        if e in main_path:
            # calc the shortest path without this edge
            # duplicate the graph
            temp_graph = nx.Graph.copy(graph)
            # remove the current edge
            temp_graph.remove_edges_from([(s, t), (t, s)])
            # calc the new shortest path
            current_cost = nx.dijkstra_path_length(temp_graph, source, target, 'weight')
            # the cost of the edge is: the main cost -(current cost + the edge's weight)
            cost = main_cost - (current_cost + w)
            print("(%s, %s) cost is %d" % (s, t, cost))
        # else, the edge isn't in the main path
        else:
            # then its cost is 0
            print("(%s, %s) cost is 0" % (s, t))


def test():
    """
    Test the vcg_cheapest_path function with an example from the slides.
    :return: Nothing, void.
    """
    # print the title
    print("TESTING WITH THE EXAMPLE FROM THE SLIDES")

    # create a graph
    graph = nx.Graph()
    # NO NEED, when adding the edges it adds the nodes too
    # add nodes: a, b, c, d
    # G.add_nodes_from(['a', 'b', 'c', 'd'])
    # add weighted edges
    weighted_edges = [('a', 'b', 3), ('a', 'c', 5), ('a', 'd', 10), ('b', 'c', 1), ('b', 'd', 4), ('c', 'd', 1)]
    graph.add_weighted_edges_from(weighted_edges)

    # print the nodes
    print("THE NODES:")
    print(graph.nodes)
    # print the edges
    print("THE EDGES:")
    for (s, t, w) in graph.edges.data('weight'):
        print("(%s, %s) with weight %d" % (s, t, w))

    # print a title
    print("THE EDGE'S COSTS:")
    # run the function
    vcg_cheapest_path(graph, 'a', 'd')


def main():
    test()


if __name__ == "__main__":
    main()
