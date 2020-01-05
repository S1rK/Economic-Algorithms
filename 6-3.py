from typing import List

# weights[i] = the i-th player's weight
weights = []
# the maximum weight
max_weight = 100

class A():
	@staticmethod
	def choices(values: List[float]) -> List[bool]:
		"""
		Sort in descending order. Select the first items that can fit in.
		:param values: The values of the items.
		:return: A list that represents if an item as chosen.
		"""
		# a list that represent if an item were chosen
		chosen = [False for _ in values]
		# the value list, but sorted in descending order
		copy_sorted = values
		copy_sorted.sort(reverse=True)
		# the current weight
		current_weight = 0
		# while there is still space\weight in the bag
		while current_weight < max_weight:
			# get the first item in the sorted list
			item = copy_sorted[0]
			# get the item's original index
			item_index = weights[values.index(item)]
			# if we will add it and will exceed the maximum weight, then we finished. break
			if current_weight + weights[item_index] > max_weight:
				break
			# else, add the item to the chosen list
			chosen[item_index] = True
			# remove the item from the sorted list
			copy_sorted.remove(item)
		# return the chosen list
		return chosen

	@staticmethod
	def payments(values: List[float]) -> List[float]:
		"""

		:param values:
		:return:
		"""
		# a list of every player how much he should pay
		payments_list = [0 for _ in values]
		# get the choices
		chosen = A.choices(values)
		# convert it to a list that contains the indexes of the chosen items
		chosen_indexes = [chosen.index(item) for item in chosen]
		# copy the  values list and sort it in descending order
		copy_sorted = values
		copy_sorted.sort(reverse=True)
		# the value of the highest value item that isn't in the list is:
		highest_not_included_value = copy_sorted[len(chosen)]
		for chosen_index in chosen_indexes:
			payments_list[int(chosen_index)] = highest_not_included_value

		return payments_list




def choices(values: List[float]) -> List[bool]:
	"""

	:param values:
	:return:
	"""
	raise NotImplementedError()


def payments(values: List[float]) -> List[float]:
	"""

	:param values:
	:return:
	"""
	raise NotImplementedError()