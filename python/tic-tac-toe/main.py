import os
import logging


logging.basicConfig(level=logging.INFO, filename='file.log', filemode='a', format='%(asctime)s - %(message)s')

def print_menu():
	print('1. Play game')
	print('2. Check win log')
	print('3. Clean log')
	print('4. Exit')

def main_menu():
	print_menu()
	chose = input()
	while chose not in ('1', '2', '3', '4'):
		os.system('clear')
		print_menu()
		chose = input()
	if chose == '1':
		play()
	if chose == '2':
		...
	if chose == '3':
		...
	if chose == '4':
		print('Bye!')
		return

def play():
	os.system('clear')
	print('Enter your name:', end=' ')
	first_name = input()
	print('Enter opponent`s name:', end=' ')
	second_name = input()
	game_procces(first_name, second_name)

def game_procces(first_name, second_name, score=[0, 0]):
	score = score
	first_player_move = True
	field = [[f'{i+1}' for i in range(3)],[f'{i+4}' for i in range(3)],[f'{i+7}' for i in range(3)]]
	while True:
		os.system('clear')
		print_map(field)
		if check_winner(field) == 'first':
			score[0] = score[0] + 1
			print(f'My congrats, {first_name}!')
			break
		if check_winner(field) == 'second':
			score[1] = score[1] + 1
			print(f'My congrats, {second_name}!')
			break
		print(f'{first_name if first_player_move else second_name} chose your cell:', end=' ')
		buf = input()
		while buf not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
			print(f'{first_name if first_player_move else second_name} chose your cell:', end=' ')
			buf = input()
		field[(int(buf)-1)//3][(int(buf)-1)%3] = 'x' if first_player_move else 'o'
		first_player_move = not first_player_move
	print('Do you wanna play revenge?[y/n]:', end=' ')
	chose = input()
	while chose not in ('y', 'n'):
		print('Do you wanna play revenge?[y/n]:', end=' ')
		chose = input()
	if chose == 'y':
		game_procces(first_name, second_name, score)
	if score == [0, 1] or score == [1, 0]:
		logging.info(f'{first_name if score[0] == 1 else second_name} win')
	else:
		logging.info(f'Part score: {first_name} - {score[0]}\t{second_name} - {score[1]}')


def check_winner(field):
	for row in field:
		first_win = True
		second_win = True
		for cell in row:
			first_win = first_win and cell == 'x'
			second_win = second_win and cell == 'o'
		if first_win == True:
			return 'first'
		if second_win == True:
			return 'second'

	for coll in range(3):
		first_win = True
		second_win = True
		for cell in range(3):
			first_win = first_win and field[cell][coll] == 'x'
			second_win = second_win and field[cell][coll] == 'o'
		if first_win == True:
			return 'first'
		if second_win == True:
			return 'second'

	if field[0][0] == 'x' and field[1][1] == 'x' and field[2][2] == 'x':
		return 'first'
	if field[0][0] == 'o' and field[1][1] == 'o' and field[2][2] == 'o':
		return 'second'
	if field[0][2] == 'x' and field[1][1] == 'x' and field[2][0] == 'x':
		return 'first'
	if field[0][2] == 'x' and field[1][1] == 'x' and field[2][0] == 'x':
		return 'second'	

def print_map(field):
	for row in field:
		for cell in row:
			print(cell, end = '\t')
		print()

if __name__ == '__main__':
	main_menu()
