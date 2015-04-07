def SBM(board, depth, player=None):
	if player is None: 
		player = 1
	elif player is 1: 
		player = 2
	elif player is 2: 
		player = 1
	else: 
		print("ERROR")

	if depth is 0: 
		return 0

	max = -100
	for i in board.available_cols(): 
		value = board.move_value(player, i)
		board.add_piece(player, i)
		value = value + SBM(board, depth-1, player)
		board.rm_piece(i)
		if value > max: 
			max = value
			best_locn = i

	return best_locn

def get_best_move(board, depth, player = None, memo = None): 
	''' 
	board = a class, 
	1 is computer
	2 is player
	visual: 
	   ([0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 1, 0, 2, 0, 0],
		[0, 1, 2, 2, 1, 0, 0])

	returns the column that the computer should put the thing. 
	'''
	# if memo is None: 
		# memo = dict()
	# print("depth", depth, "player", player)

	if player is None: 
		player = 1

	if depth == 0: 
		# print("depth is 0 return 0")
		return (0,0)

	if player is 2: 
		pos_val = [(board.move_value(player, col), col) for col in board.available_cols()]
		max_col = max(pos_val)[1]
		board.add_piece(2, max_col) #'''this is a problem'''	
		player = 1
		# print("I'm guessing you're going to play ", max_col)
		return get_best_move(board, depth, player) # memo

	if player is 1: 
		pos_val = []
		for i, col in enumerate(board.available_cols()): 
			pos_val.append((board.move_value(player, col) + get_best_move(board, depth-1, 2)[0], i)) # memo

		# print("list of possible values", pos_val)
		max_val = max(pos_val)
		print(max_val)
		max_col = max_val[1]
		board.add_piece(1, max_col)
		player = 2
		return max_val #max(pos_val)[0]

	#######################################################
