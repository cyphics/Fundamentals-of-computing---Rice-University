"""
Some creation and computation
on graphs
"""

import matplotlib.pyplot as plt
import math

import compute_functions as compute
import alg_load_graph as load_graph
import alg_dpa_trial as dpa

# Plot options
STANDARD = True
LOGLOG = False


def build_plot(degree_distribution):
    """
    Build plot of the number of increments in mystery function
    """
    plot = [[], []]
    for degree in degree_distribution:
        # counter += 1
        plot[0].append(degree)
        plot[1].append(degree_distribution[degree])
    return plot



# Citations graph
citations_graph = load_graph.citation_graph
in_degree_distribution_citations = compute.in_degree_distribution(citations_graph)
out_degree_distribution_citations = compute.compute_out_degrees(citations_graph)
normalized_citations = compute.normalize_in_degree_graph(in_degree_distribution_citations, len(citations_graph))

average_out = 0
for node in out_degree_distribution_citations:
    average_out += out_degree_distribution_citations[node]

# print average_out / len(out_degree_distribution_citations)


# Random graph
random_graph = compute.modified_ER(5000, 0.5)
in_degree_distribution_random = compute.in_degree_distribution(random_graph)
normalized_random = compute.normalize_in_degree_graph(in_degree_distribution_random, len(random_graph))

# DPA graph
dpa_graph = compute.DPA(27700, 12)
in_degree_distribution_dpa = compute.in_degree_distribution(dpa_graph)
normalized_dpa = compute.normalize_in_degree_graph(in_degree_distribution_dpa, len(dpa_graph))



# print dpa_graph
plot_type = STANDARD
plot_size = 40


# Create plot
# plot_citations = build_plot(normalized_citations)
plot_random = build_plot(normalized_random)
# plot_dpa = build_plot(normalized_dpa)


plt.plot(plot_random[0], plot_random[1], 'bo', label="Random graph")
# plt.plot(plot_citations[0], plot_citations[1], 'ro', label="Citations graph")
# plt.plot(plot_dpa[0], plot_dpa[1], 'go', label="DPA graph")

plt.ylabel("papers normalized")
plt.xlabel("citations")
plt.title("Citation graph (Log/log)")
plt.xscale('log')
plt.yscale('log')
plt.legend(bbox_to_anchor=(0.05, 1), loc=2, borderaxespad=0.)
plt.show()
