import matplotlib.pyplot as plt
import time
import cProfile
import project
import alg_application2_provided as provided


def time_it(f, *args):
    start = time.clock()
    f(*args)
    return (time.clock() - start) * 1000

##############
# Question 1 #
##############
def question1():
    # Create graphs
    loaded_graph = provided.load_graph(provided.NETWORK_URL)
    ER_graph = project.ER_graph(1239, 0.004)
    upa_graph = project.UPA_graph(1239, 3)

    # Compute resilience
    resilience_loaded = project.compute_resilience(loaded_graph, project.random_order(loaded_graph))
    resilience_ER = project.compute_resilience(ER_graph, project.random_order(ER_graph))
    resilience_UPA = project.compute_resilience(upa_graph, project.random_order(upa_graph))

    # Create plots
    loaded_plot = project.build_plot(resilience_loaded)
    ER_plot = project.build_plot(resilience_ER)
    UPA_plot = project.build_plot(resilience_UPA)

    plt.plot(loaded_plot[0], loaded_plot[1], 'b', label="Loaded graph")
    plt.plot(ER_plot[0], ER_plot[1], 'r', label="ER graph (p = 0.004)")
    plt.plot(UPA_plot[0], UPA_plot[1], 'g', label="UPA graph (m = 3)")

    plt.xlabel("Number of nodes removed")
    plt.ylabel("Size of largest connected component")
    plt.title("Resilience graph (random attack)")
    # plt.xscale('log')
    # plt.yscale('log')
    plt.legend(bbox_to_anchor=(0.05, 1), loc=2, borderaxespad=0.)
    plt.show()


##############
# Question 3 #
##############

def question3():
    time_targeted_order = []
    size_values = []
    time_fast_targeted_order = []
    size_fast_targeted_order = []
    for size in range(10, 1000, 10):
        size_values.append(size)
        time_targeted_order.append(time_it(provided.targeted_order, project.UPA_graph(size, 5)))
        time_fast_targeted_order.append(time_it(provided.fast_targeted_order, project.UPA_graph(size, 5)))

    plt.plot(size_values, time_targeted_order, 'r', label="targeted order algorithm")
    plt.plot(size_values, time_fast_targeted_order, 'b', label="fast targeted order algorithm")
    plt.xlabel("Size of the graph (m = 5)")
    plt.ylabel("Time to process (milliseconds)")
    plt.title("Runtime comparison")
    # plt.xscale('log')
    # plt.yscale('log')
    plt.legend(bbox_to_anchor=(0.05, 1), loc=2, borderaxespad=0.)
    plt.show()



##############
# QUESTION 4 #
##############

def fast_targeted_order(ugraph):
    """
    Take a graph, and return a list of nodes in
    descending degree order.
    """
    DegreeSets = {}
    copy_ugraph = provided.copy_graph(ugraph)
    for degree in range(len(copy_ugraph)):
        DegreeSets[degree] = set([])
    for node in copy_ugraph:  # range(len(copy_ugraph)):
        degree = len(copy_ugraph[node])
        DegreeSets[degree].add(node)
    ordered_nodes = []
    i = 0
    for degree in range(len(copy_ugraph) - 1, -1, -1):
        while DegreeSets[degree]:
            current_node = DegreeSets[degree].pop()
            for neighbor in copy_ugraph[current_node]:
                neighbor_degree = len(copy_ugraph[neighbor])
                DegreeSets[neighbor_degree].remove(neighbor)
                DegreeSets[neighbor_degree - 1].add(neighbor)
            ordered_nodes.append(current_node)
            i += 1
            provided.delete_node(copy_ugraph, current_node)
    return ordered_nodes


def question4():
    # Create graphs
    loaded_graph = provided.load_graph(provided.NETWORK_URL)
    ER_graph = project.ER_graph(1239, 0.004)
    upa_graph = project.UPA_graph(1239, 3)

    # Compute resilience
    resilience_loaded = project.compute_resilience(loaded_graph, fast_targeted_order(loaded_graph))
    resilience_ER = project.compute_resilience(ER_graph, fast_targeted_order(ER_graph))
    resilience_UPA = project.compute_resilience(upa_graph, fast_targeted_order(upa_graph))

    # Create plots
    loaded_plot = project.build_plot(resilience_loaded)
    ER_plot = project.build_plot(resilience_ER)
    UPA_plot = project.build_plot(resilience_UPA)

    plt.plot(loaded_plot[0], loaded_plot[1], 'b', label="Computer graph")
    plt.plot(ER_plot[0], ER_plot[1], 'r', label="ER graph (p = 0.004)")
    plt.plot(UPA_plot[0], UPA_plot[1], 'g', label="UPA graph (m = 3)")

    plt.xlabel("Number of nodes removed")
    plt.ylabel("Size of largest connected component")
    plt.title("Resilience graph (targeted attack)")
    plt.legend(bbox_to_anchor=(0.4, 1), loc=2, borderaxespad=0.)
    plt.show()

question1()
question3()
question4()
