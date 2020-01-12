"""
Economic Algorithms
Exercise 11 , Question 3
AUTHOR: Tal Nakar
SINCE:  10-1-2020
"""
import networkx as nx
from typing import List


class Worker:
	# Worker name, for display
	name: str
	# preferences[0] iss the best shift for the worker
	# preferences[1] iss the 2nd-best shift for the worker. etc...
	preferences: List[int]
	# The shift to which the worker is currently assigned
	current_shift: int

	def __init__(self, name, current_shift, preferences):
		self.name = name
		self.current_shift = current_shift
		self.preferences = preferences


def exchange_shifts(workers: List[Worker]):
	"""
	An implementation of The Top Trading Cycle Algorithm.
	:param workers: A list of workers.
	:return: Prints the exchanges.
	"""
	# initialize the graph from the matrix
	graph = nx.DiGraph()
	# add all nodes
	for worker in workers:
		# add the worker
		graph.add_node(worker)
		# add it's shift
		graph.add_node(worker.current_shift)

	# add all first edges
	for worker in workers:
		# add edge: worker <- it's shift
		graph.add_edge(worker.current_shift, worker)
		# add edge: worker -> wanted shift
		graph.add_edge(worker, worker.preferences[0])

	# go thought cycles until the graph is empty
	while len(graph) > 0:
		# find cycle
		cycle_edges = nx.find_cycle(graph)
		# convert to list of nodes
		cycle = [edge[0] for edge in cycle_edges]
		# if the worker is not first
		if type(cycle[0]) is not Worker:
			# shift by 1
			cycle = cycle[1:] + cycle[:1]

		# print exchanges between workers
		for i in range(0, len(cycle), 2):
			print(f"{cycle[i].name} moves from shift {cycle[i-1]} to shift {cycle[i+1]}.")

		# remove the nodes from the graph
		graph.remove_nodes_from(cycle)

		# update graph
		# for every worker
		for worker in workers:
			# if he's still in the graph
			if graph.has_node(worker):
				# if he doesn't have any edge from him
				if len(list(graph[worker].keys())) == 0:
					# add one (via his preferences)
					for shift in worker.preferences:
						if graph.has_node(shift):
							graph.add_edge(worker, shift)


def test():
	print("-----------TESTING-----------")
	# from https://en.wikipedia.org/wiki/Top_trading_cycle
	a = Worker("Alice", 1, [3, 2, 4, 1])
	b = Worker("Bob", 2, [3, 5, 6, 1])
	c = Worker("Chloe", 3, [3, 1, 2, 4])
	d = Worker("David", 4, [2, 5, 6, 4])
	d.name = 'David'
	e = Worker("Edward", 5, [1, 3, 2])
	f = Worker("Finn", 6, [2, 4, 5, 6])
	workers = [a, b, c, d, e, f]

	# print workers
	print("THE WORKERS:")
	for worker in workers:
		print(f"{worker.name}: current shift={worker.current_shift}, pref={worker.preferences}")

	print("THE EXCHANGES:")
	exchange_shifts(workers)


if __name__ == "__main__":
	test()
