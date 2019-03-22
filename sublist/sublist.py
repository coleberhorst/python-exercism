SUBLIST, SUPERLIST, EQUAL, UNEQUAL = range(4)


def check_lists(first_list, second_list):
	first, second = str(first_list)[1:-1], str(second_list)[1:-1]
	if first == second:
		return EQUAL
	elif first in second:
		return SUBLIST
	elif second in first:
		return SUPERLIST
	else:
		return UNEQUAL
