#update comments pre github
###THE BASICS

#initial conditions
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
turn = 0
move_counter = 0
print ""
print "#####################################"
print "#                                   #"
print "#                                   #"
print "#      Welcome to TIC TAC TOE       #"
print "#                                   #"
print "#             by Aliza              #"
print "#                                   #"
print "#                                   #"
print "#####################################"
print ""

#This increments the turn
def update_turn():
 	global turn
 	turn += 1
 	return turn

#This increments the move counter so that the program can declare a cat's game. 
def update_move_counter():
	global move_counter
	move_counter += 1
	return move_counter

#do you want to go first?
def go_first():
	print "Would you like to go first? (y/n)"
	answer = raw_input()
	if ("y" not in answer) and ("n" not in answer):
		print "Type y or n, please."
		go_first()
	elif ("y" in answer) and ("n" in answer):
		print "Dude. Come on."
		go_first()
	elif "y" in answer:
		print "Great, you'll go first."
	else:
		update_turn()
#Note: this will mean that the computer only goes on odd turns
		print "Okay, the computer will go first"

#This lets the human pick their letter
def x_or_o():
	def success1():
		print "Okay, you'll be ",human_play_letter, "and the computer will be ",robot_play_letter
	global human_play_letter
	global robot_play_letter
	print "Would you like to be X or O?"
	human_letter = raw_input()
	if human_letter == "X" or human_letter == "x":
		human_play_letter = "x"
		robot_play_letter = "o"
		success1()
	elif human_letter == "O" or human_letter == "o":
		human_play_letter = "o"	
		robot_play_letter = "x"
		success1()
	else:
		print "Nope. Try again."
		x_or_o()
	


#You can choose your level of difficulty. You can beat robots 1 and 2. You can't beat 3
def smart_robot():
	global challenge_level
	print "Which opponent would you like to play? (Select 1, 2 or 3)"
	print "1 - Your cousin in kindergarten who just learned tic-tac-toe."
	print "2 - A veritable tic-tac-foe."
	print "3 - Indominus Rex(and oh)"
	answer = raw_input()
	if not answer.isdigit() or int(answer) < 1 or int(answer) > 3:
		print "Choose 1, 2 or 3"
		smart_robot()
		return ""
	else:
		challenge_level = int(answer)
		print "Okay... Have fun!"

#this alters the board to add the human and robot moves. it turns 100 into the human's move letter and 600 into the robot's letter.
def create_displayboard():
	global display_board
	display_board = []
	for d in board:
		if d==100:
			display_board.append(human_play_letter)
		elif d==600:
			display_board.append(robot_play_letter)
		else:
			display_board.append(d)
	print_board()

#This prints the calculated display board on the grid humans recognize	
def print_board():
	print " ", display_board[0], "|", display_board[1], "|", display_board[2]
	print "--------------"
	print " ", display_board[3], "|", display_board[4], "|", display_board[5]
	print "--------------"
	print " ", display_board[6], "|", display_board[7], "|", display_board[8]

#This runs the whole opening sequence.
def opening():
	go_first()
	x_or_o()
	smart_robot()
	if turn == 0:
		create_displayboard()


###HUMAN MOVE
#You are the human. You figure out your strategy.
		
#human move
def your_move():
	global move 
	move = raw_input("What space do you want? ")
	if not move.isdigit():
		print "Choose a number."
		your_move()
	else: 
		move = int(move)
		if move not in board or move > 9:
			print "That's not an option. Choose again."
			your_move()
		else:
			board[move-1] = 100
			

###ROBOT STRATEGY AND MOVE PLACEMENT SECTION

#winsets are the 8 ways you could win tic tac toe. this updates the winsets from the latest state of the board
def create_winsets():
	global winsets
	win_1 = [board[1-1], board[2-1], board[3-1]]
	win_2 = [board[4-1], board[5-1], board[6-1]]
	win_3 = [board[7-1], board[8-1], board[9-1]]
	win_4 = [board[1-1], board[4-1], board[7-1]]
	win_5 = [board[2-1], board[5-1], board[8-1]]
	win_6 = [board[3-1], board[6-1], board[9-1]]
	win_7 = [board[1-1], board[5-1], board[9-1]]
	win_8 = [board[3-1], board[5-1], board[7-1]]
	#switched order to prevent issue with 5 move on first human turn
	winsets=[win_1, win_2, win_3, win_4, win_5, win_6, win_7, win_8]
	

#finding the sums of the winsets to create a simplified list of 9 values. The robot will be able to make a decision about which line to act on --either offensively or defensively--based on these values. 
def create_sum():
	create_winsets()
	global sum_winsets
	sum_winsets = []
	#print count_winsets
	for list in winsets:
		sum_winsets.append(sum(list))
	return sum_winsets

#looks for a place to clinch a win. It's looking for a line where it has placed two letters.
def line1():
	for x in range (1199,1210):
		if x in sum_winsets:
			return sum_winsets.index(x)	
	
#looks for a place to block the human's win. That is, it's looking for a line where the human has placed two letters. 
def line2():
	for x in range (199,310):
		if x in sum_winsets:
			return sum_winsets.index(x)	
	
#needed for line3 to find the most common element in the flattened list
def most_common(lst):
    return max(set(lst), key=lst.count)
    

#this looks for the number that is in the most number of threat sets and plays it. left the printing in since it is complicated and have needed it on and off to debug.     		
def line3():
	#global line_3_attack
	#global sneaky_pick
#looks for all the places where human has one move	
	sneaky = []
	#print sum_winsets
	for x in sum_winsets:
		if x in range (100,200):
			sneaky.append(x)
	#print sneaky
	
#looks for which winsets those are	
	sneaky2 = []
	for y in sneaky:
		if y in sum_winsets:
			sneaky2.append(sum_winsets.index(y))
	#print sneaky2
#finds the winsets and shows the remaining options under 100	
	sneaky3 = []
	for z in sneaky2:
		sneaky3.append(winsets[z])
	#print sneaky3
#flattens the list	
	sneaky3_flat = sum(sneaky3, [])
	#print sneaky3_flat
#leaves only the remaining spaces
	sneaky4 = []
	for h in sneaky3_flat:
		if h <100:
			sneaky4.append(h)
	#print sneaky4
#returns the most common space, which is the space where you can prevent two line win	
	#print most_common(sneaky4)
	return most_common(sneaky4)
	

#this will just look for the first place available on the board, regardless of strategy
def line4():
	for x in range (0,4500):
		if x in sum_winsets:
			return sum_winsets.index(x)
	

#how the robot decides which line to act on. i left printing in for debugging if the wrong line was firing
def pick_the_move():
	global skip_choice
	skip_choice = 0
#regardless of challenge level, if robot has 2 in a row, they'll go for the win
	create_sum()	
	if line1() >= 0:
		#print "line1"
		return line1()
#challenge level 1 is not smart enough to block the human's win yet	
	elif challenge_level > 1:
		if line1() is None:
			if line2() >= 0:
				#print "line2"
				return line2()
			else: 
				if all(i >= 100 for i in sum_winsets):
					#"print line4"
					return line4()
#this is important. if the robot has both taken a winning line or defended against a win, if it is at the top skill level, it needs to evaluate multiple lines. i used skip choice to have it avoid robot_choice_in_line logic. probably a better way to factor this out.				
				else:
					if challenge_level == 3:
						skip_choice = 1
						return ""
					else:
						#print "line4"
						return line4()
	else: 
		#print "line4"
		return line4()

#once the robot has picked the line it is going for, it chooses the space in the line. it knows something hasn't been picked if it is <10 (as choices are either 100 or 600). in line1() and line 2(), there is only 1 available option. for line4() which only fires in erratic play, it will pick the lowest integer. 
def robot_choice_in_line():
 	pick_the_move()
 	if skip_choice == 1:
 		#print "line3"
 		return line3()
 	else:
 		create_winsets()
 		for a in winsets[pick_the_move()]:
			if a < 10:
				return a

#how the robot places the move. the indominus robot is named as such because it will always go for the center (5) if available, and the edge (2, 4, 6, 8). that will block any human from winning. 			
def robot_move():
	#global sneaky_pick
#always start with the middle if available	
	if move_counter == 1 or move_counter == 0 and challenge_level == 3:
		if 5 in board:
			board[4] = 600
#if opponent starts in the middle, you must pick a corner		
		elif 5 not in board:
			board[0] = 600
		else:
			board[robot_choice_in_line()-1] = 600
#an old hard-coded move which I replaced with line 3, which was more abstract
	#elif move_counter == 5 and challenge_level == 3:
	#	for f in board:
	#		if f % 2 == 0 and f < 10:
	#			board[f-1] = 600
	#			print f
	#			return f
	#elif challenge_level == 3:
	#	print line3()
	#	board[line3()-1] = 600
	else:
		board[robot_choice_in_line()-1] = 600
	

###GAME PLAY
#This function moves the game forward and ends it at the right time. 	
def whose_turn():
	for h in range(10):
		create_winsets()
		create_sum()		
		if 300 in sum_winsets:
			print ""
			print "You win! The human wins!"
			return "done"
		elif 1800 in sum_winsets:
			print ""
			print "You have been beaten at tic-tac-toe by a computer."
			return "done"	
		elif move_counter == 9:
			print ""
			print "Tie. Cat's game. Meow."
			return ""
		elif turn % 2 == 0:
			your_move()
		else:
			robot_move()
		create_displayboard()
		update_turn()
		update_move_counter()	
			
			
###THE PROGRAM 
opening()
whose_turn()





