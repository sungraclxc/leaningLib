t=[2, [7,[3,[6,[5,11]]],15]]

def tree_handler(n):
	new_lst = []
	depth = 0
	def unwrap(m):
		nonlocal depth
		nonlocal new_lst
		for i in m:
			if type(i) == list:
				unwrap(i)
			else:
				new_lst = new_lst + [i]
		depth = depth +1
		print("height", depth)
		return new_lst
	if len(n) > 0:
		return unwrap(n)
	return new_lst
	
def tree_max(n):
	if len(n) > 0:
		return max(tree_handler(n))
	return 0
	
	
def square_tree(n):
	if len(n) > 0:
		return [x*x for x in tree_handler(n)]
	return 0 
