import copy
import networkx as nx

from utils.graph import Graph


def create_graph_from_txt_file(txt_file: str):
    nodes = []
    with open(txt_file) as file:
        line = file.readline()
        while line:
            if "#" not in line:
                n_info = line.replace("\n", "").split(",")
                nodes.append((n_info[0], n_info[1], n_info[2]))

            line = file.readline()

    if len(nodes) > 0:
        g = Graph()
        g.add_node_list(nodes)
        return g

    raise Exception("Wrong input file provided")


def from_numpy_matrix(A, create_using=None):
    """

    :param A:
    :param create_using:
    :return:
    """
    kind_to_python_type = {'f': float,
                           'i': int,
                           'u': int,
                           'b': bool,
                           'c': complex,
                           'S': str,
                           'V': 'void'}

    try:
        import numpy as np
    except ImportError:
        raise ImportError("from_numpy_matrix() requires numpy: http://scipy.org/ ")

    g = Graph(create_using)
    n, m = A.shape

    if n != m:
        raise nx.NetworkXError("Adjacency matrix is not square.",
                               "nx,ny=%s" % (A.shape,))
    dt = A.dtype
    try:
        python_type = kind_to_python_type[dt.kind]
    except:
        raise TypeError("Unknown numpy data type: %s" % dt)

    nodes = list(range(n))
    # Get list of edges
    x, y = np.asarray(A).nonzero()

    # Handle numpy constructed data type
    if python_type == 'void':
        fields = sorted([(offset, dtype, name) for name, (dtype, offset) in
                         A.dtype.fields.items()])
        for (u, v) in zip(x, y):
            attr = {}
            for (offset, dtype, name), val in zip(fields, A[u, v]):
                attr[name] = kind_to_python_type[dtype.kind](val)
            g.add_edge(u, v, attr)
    else:  # Basic data type
        g.add_edges_from((u, v, {'weight': python_type(A[u, v])}) for (u, v) in zip(x, y))

    return g


def get_mst(graph):
    """
    Kruskal's algorithm
    :param graph:
    :return:
    """
    edges = graph.get_edges()
    weighted_edges = {}
    for (u, v) in edges:
        weighted_edges[(u, v)] = int(graph.get_edge_weight(u, v))

    # Sort edges by weight, by value
    weighted_edges = sorted(weighted_edges.items(), key=lambda x: x[1])

    mst_graph = Graph()
    nodes = []
    for itm in weighted_edges:
        u, v = itm[0]
        mst_graph.add_edge(u, v, graph.get_edge_weight(u, v))
        try:
            nx.algorithms.find_cycle(mst_graph.get_graph())
            mst_graph.get_graph().remove_edge(u, v)
        except nx.NetworkXNoCycle:
            nodes.append(u)
            nodes.append(v)

    return mst_graph


def get_degrees(graph):
    """

    :param graph:
    :return:
    """
    degrees = {}

    for d in graph.get_degree():
        degrees[d[0]] = d[1]

    return degrees


def get_nodes_odd_degrees(degrees):
    """
    
    :param degrees: 
    :return: 
    """
    odd_degrees = {}

    for k in degrees.keys():
        if (degrees[k] % 2 != 0):
            odd_degrees[k] = degrees[k]

    return odd_degrees


def print_edges_with_weight(graph):
    """

    :param graph:
    :return:
    """
    if isinstance(graph.get_graph(), nx.MultiGraph):
        for e in graph.get_edges():
            print(f"Edge: ({e[0]}, {e[1]})")
    else:
        for e in graph.get_edges():
            print(f"Edge: ({e[0]}, {e[1]}) = {graph.get_edge_weight(e[0], e[1])}")


def convert_edges_tuples_to_dict(nodes, edge_tuples):
    edges = {}

    # Add all nodes as keys
    for n in nodes:
        edges[n] = []

    for e in edge_tuples:
        edges[e[0]].append((e[1]))
        edges[e[1]].append((e[0]))

    return edges


def create_subgraph(graph, nodes_to_include):
    """

    :param graph:
    :param nodes_to_include:
    :return:
    """
    subgraph = nx.Graph(graph.get_graph().subgraph(nodes_to_include))
    return Graph(nx_graph=subgraph)


def create_minimum_weight_perfect_matching(graph):
    """

    :param graph:
    :return:
    """
    # Create new graph with negative weight
    new_graph = Graph()
    for e in graph.get_edges():
        new_graph.add_edge(e[0], e[1], -int((graph.get_edge_weight(e[0], e[1]))))

    set_matching = nx.max_weight_matching(new_graph.get_graph(), maxcardinality=True)

    matching_graph = Graph()
    for m in set_matching:
        matching_graph.add_edge(m[0], m[1], graph.get_edge_weight(m[0], m[1]))

    return matching_graph


def union_graphs(graph1, graph2):
    """

    :param graph1:
    :param graph2:
    :return:
    """
    multi_graph = Graph(multi_graph=True)
    for e in graph1.get_edges():
        multi_graph.add_edge(e[0], e[1])

    for e in graph2.get_edges():
        multi_graph.add_edge(e[0], e[1])

    return multi_graph


def get_total_cost(graph, path):
    """

    :param graph:
    :param path:
    :return:
    """
    weight = 0
    for i in range(1, len(path)):
        weight += int(graph.get_edge_weight(path[i - 1], path[i]))

    return weight
