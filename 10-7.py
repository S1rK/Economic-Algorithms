"""
Economic Algorithms
Exercise 10 , Question 7
AUTHOR: Tal Nakar
SINCE:  4-1-2020
"""
from typing import List, Tuple


def get_other_couple(given_number: int, index_in_marriage: int, marriage_list: List[Tuple[int, int]]) -> int:
	"""
	Returns the significant other's number.
	:param given_number: The number of one of the couple.
	:param index_in_marriage: The given_number's index in the tuple of marriage.
	:param marriage_list: The list of marriages.
	:return: int.
	"""
	return [marry[1-index_in_marriage] for marry in marriage_list if marry[index_in_marriage] is given_number][0]


def check_if_stable_marriage(first_side_pref: List[List[int]], second_side_pref: List[List[int]], marriage: List[Tuple[int, int]]) -> bool:
	"""
	Checks for a given preferences and marriage, if the marriage is stable.
	:param first_side_pref: The first side's preferences (list of list on int).
	:param second_side_pref: The second side's preferences (list of list on int).
	:param marriage: The marriage (list of tuples of int).
	:return: bool.
	"""
	# for every a in first side
	for a in range(len(first_side_pref)):
		# get his pref
		first_pref = first_side_pref[a]
		# get his marriage
		married = get_other_couple(a, 0, marriage)

		# go over a's prefs
		for b in first_pref:
			# if b is the married, then there marriage is stable. go check the next ones.
			if b is married:
				continue
			# if it's not
			# get b's pref
			second_pref = second_side_pref[b]
			# get b's couple
			bs_couple = get_other_couple(b, 1, marriage)
			# check if b prefers a then his married couple
			if second_pref.index(bs_couple) > second_pref.index(a):
				return False
		# every marriage is stable, return True
		return True


def main():
	check_if_stable_marriage()


if __name__ == "__main__":
	main()
