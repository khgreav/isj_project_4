#!/usr/bin/env python3

def can_be_a_set_member_or_frozenset(item):
	"""
	Returns item for items that can be in a set, otherwise returns frozenset.
	"""
	if type(item) == int or type(item) == tuple or type(item) == set:
		return item
	else:
		return frozenset(item)

def all_subsets(lst):
	"""
	Creates a powerset of input list, for each new element,
	use the previous state of powerset and add subsets with the new element.
	"""
	powerset = [[]] # empty subset is in every set
	for elem in lst:
		powerset.extend([subset + [elem] for subset in powerset]) # incremental powerset
	return powerset

def all_subsets_excl_empty(*lst, exclude_empty = True):
	"""
	Creates a powerset of input list, for each new element,
	use the previous state of powerset and add subsets with the new element.
	Empty subset can be excluded.
	"""
	powerset = [[]] # empty subset is in every set unless specified otherwise
	for elem in lst:
		powerset.extend([subset + [elem] for subset in powerset]) # incremental powerset
	if exclude_empty: # exclude empty subset
		powerset.pop(0) # skip first
	return powerset