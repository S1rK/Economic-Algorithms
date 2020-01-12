"""
Economic Algorithms
Exercise 11 , Question 5
AUTHOR: Tal Nakar
SINCE:  10-1-2020
"""
import networkx as nx
from typing import List, Tuple


def find_max_matches_recursive(graph: nx.DiGraph) -> List[List[int]]:
	"""
	A recursive function that finds cycles with a length of 2 or 3, such that the sum of the cycle's lengths is max.
	:param graph: A nx.DiGraph (directed graph).
	:return: The cycles.
	"""
	# get all the cycles in the graph
	cycles = list(nx.simple_cycles(graph))

	# if the graph doesn't have any cycles, stop the recursive calling and return an empty cycle
	if len(cycles) == 0:
		return []

	children = []
	# for all the cycles
	for cycle in cycles:
		# if their length is 2 or 3
		if len(cycle) == 2 or len(cycle) == 3:
			# copy the graph
			copy_graph = graph
			# remove the nodes in the cycle
			copy_graph.remove_nodes_from(cycle)
			# call the recursive function with the copyed graph, and to the children's list the returned value
			# (list of cycles in the copyed graph) with the cycle
			children.append([cycle] + find_max_matches_recursive(graph))

	# get the child with the max transplanted
	max_child = children[0]
	max_child_val = 0
	for child in children:
		child_value = sum([len(cycle) for cycle in child])
		if child_value > max_child_val:
			max_child = child
			max_child_val = child_value

	return max_child


def find_max_matches(compatible: List[List[bool]]):
	"""
	Finds cycles with a length of 2 or 3, such that the sum of the cycle's lengths is max, and print them
	:param compatible: A matrix such that if compatible[i,j]=True then i can donate a kidney to j.
	:return: Nothing, void. Prints the cycles.
	"""
	# create the graph from the matrix
	graph = nx.DiGraph()
	for i in range(len(compatible)):
		for j in range(len(compatible[0])):
			if compatible[i][j]:
				graph.add_edge(i, j)

	# find the maximum matching in the graph
	# maximum_matching = nx.max_weight_matching(graph)
	maximum_matching = find_max_matches_recursive(graph)

	# print it
	for cycle in maximum_matching:
		print(f"Length {len(cycle)} cycle: ", end="")
		for i in range(len(cycle)-1):
			print(f"{cycle[i]}->{cycle[i+1]} and ", end="")
		print(f"{cycle[-1]}->{cycle[0]}")


def test():
	"""Testing the find_max_matches function"""
	print("-----------TESTING-----------")
	# create matrix
	comp = [[False for _ in range(7)] for _ in range(7)]
	# 0->1
	comp[0][1] = True
	# 2->0
	comp[2][0] = True
	# 1->3
	comp[1][3] = True
	# 1->2
	comp[1][2] = True
	# 5->4
	comp[5][4] = True
	# 4->3
	comp[4][3] = True
	# 3->5
	comp[3][5] = True
	# 5->6
	comp[5][6] = True
	# 6->5
	comp[6][5] = True

	print("THE GRAPH:")
	for i in range(len(comp)):
		for j in range(len(comp[i])):
			if comp[i][j]:
				print(f"{i}->{j}")
	print("THE CYCLES:")
	find_max_matches(comp)


if __name__ == "__main__":
	test()
