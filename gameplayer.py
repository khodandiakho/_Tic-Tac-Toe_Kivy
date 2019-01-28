import random

class GamePlayer:

	def __init__(self, choice):
		self.choice = choice

    # Main function for bot making a move

	def make_move(self, board, winning_combos):
		self.make_random_move(board, winning_combos)  # Do a random move

    # Makes a random moves and WIN if possible

	def make_random_move(self, board, winning_combos):
		free_buttons = []
		for button in board:

			if len(button.text.strip()) < 1:
				free_buttons.append(button)
		if board[4] in free_buttons:
			free_buttons[free_buttons.index(board[4])].text = self.choice
			return True

		for combo in winning_combos:
			print(combo)
			if board[combo[0]].text == board[combo[1]].text and board[combo[2]].text == '' and board[combo[0]].text == self.choice:
				free_buttons[free_buttons.index(board[combo[2]])].text = self.choice

				return True
			elif board[combo[0]].text == board[combo[2]].text and board[combo[1]].text == '' and board[combo[0]].text == self.choice:
				free_buttons[free_buttons.index(board[combo[1]])].text = self.choice
				return True
			elif board[combo[1]].text == board[combo[2]].text and board[combo[0]].text == '' and board[combo[1]].text == self.choice:
				free_buttons[free_buttons.index(board[combo[0]])].text = self.choice
				return True
		else :
			free_buttons[free_buttons.index(random.choice(free_buttons))].text = self.choice
			return True


