import random
import curses

s = curses.initscr()
curses.curs_set(0)

# Making the map

sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

# Create Snake Initial Position

snk_x = sw/4
snk_y = sh/2

# Creating the body of the snake

snake = [
	[snk_y, snk_x],
	[snk_y, snk_x-1],
	[snk_y, snk_x-2]
	]

# Add the food to the screen

food = [sh/2, sw/2]
w.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT

# The infinite loop

while True:
	next_key = w.getch()
	key = key if next_key == -1 else next_key

	# Check if lost the game

	if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
		curses.endwin()
		quit()

	# Making new head 

	new_head = [snake[0][0], snake[0][1]]

	# Looking for key press

	if key == curses.KEY_DOWN:
		new_head[0] += 1
	if key == curses.KEY_UP:
		new_head[0] -= 1			
	if key == curses.KEY_LEFT:
		new_head[1] -= 1
	if key == curses.KEY_RIGHT:
		new_head[1] += 1

	# Insert new head of the snake

	snake.insert(0, new_head)

	# Checking if snake ate the food?

	if snake[0] == food:
		food = None
		while food is None:

			# Make new food location

			nf = [
				random.randint(1, sh-1),
				random.randint(1, sw-1)
				]

			# Check the food 

			food = nf if nf not in snake else None

		# Add the food

		w.addch(food[0], food[1], curses.ACS_PI)
	else:
		tail = snake.pop()

		# Growing the tail	

		w.addch(tail[0], tail[1], ' ')

	#Update the screen with new body	
	
	w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)