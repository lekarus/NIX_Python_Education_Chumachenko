"""
    Module for playing in tic-tac-toe
"""
import os
import logging


logging.basicConfig(level=logging.INFO,
    filename='file.log', filemode='a', format='%(asctime)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S')

def print_menu():
    """Print main menu
    """
    print('1. Play game')
    print('2. Check victory logs')
    print('3. Clean logs')
    print('4. Exit')

def main_menu():
    """
        Method for selecting an item from the main menu
    """
    print_menu()
    chose = input()
    while chose not in ('1', '2', '3', '4'):
        os.system('clear')
        print_menu()
        chose = input()
    if chose == '1':
        play()
    if chose == '2':
        os.system('clear')
        print('victory logs:')
        with open('file.log', 'r', encoding ='utf-8') as log_file:
            for line in log_file:
                print(line, end ='')
        print('',end='\n\n')
        main_menu()
    if chose == '3':
        os.system('clear')
        with open('file.log', 'w', encoding='utf-8') as log_file:
            log_file.write('')
        print('logs cleared successfully')
        main_menu()
    if chose == '4':
        print('Bye!')
        return

def play():
    """
        Method for assisgning player names
    """
    os.system('clear')
    print('Enter your name:', end=' ')
    first_name = input()
    print('Enter opponent`s name:', end=' ')
    second_name = input()
    game_procces(first_name, second_name)

def game_procces(first_name, second_name, prev_score=(0, 0)):
    """
        Main method in which all the logic of the game takes place

        Args:

            first_name (str): first player name
            second_name (str): second player name
            score (list): default argument, which is needed if players play more than 1 game
    """
    score = list(prev_score)
    first_player_move = True
    field = [[f'{i+1}' for i in range(3)],[f'{i+4}' for i in range(3)],[f'{i+7}' for i in range(3)]]
    counter = 0

    while True:
        os.system('clear')
        print_field(field)
        if check_winner(field) == 'first':
            score[0] = score[0] + 1
            print(f'My congrats, {first_name}!')
            break
        if check_winner(field) == 'second':
            score[1] = score[1] + 1
            print(f'My congrats, {second_name}!')
            break
        if counter == 9:
            print('Draw')
            break

        print(f'{first_name if first_player_move else second_name} chose your cell:', end=' ')
        buf = input()
        while buf not in ('1', '2', '3', '4', '5', '6', '7', '8', '9')  :
            print(f'{first_name if first_player_move else second_name} chose your cell:', end=' ')
            buf = input()

        if (field[(int(buf)-1)//3][(int(buf)-1)%3] == 'x' or
            field[(int(buf)-1)//3][(int(buf)-1)%3] == 'o'):
            continue
        field[(int(buf)-1)//3][(int(buf)-1)%3] = 'x' if first_player_move else 'o'
        counter += 1
        first_player_move = not first_player_move

    print('Do you wanna play revenge?[y/n]:', end=' ')
    chose = input()
    while chose not in ('y', 'n'):
        print('Do you wanna play revenge?[y/n]:', end=' ')
        chose = input()
    if chose == 'y':
        game_procces(first_name, second_name, score)
    else:
        if score == [0, 0]:
            logging.info('%s / %s - draw', first_name, second_name)
        elif score in ([0, 1], [1, 0]):
            logging.info('%s won', first_name if score[0] == 1 else second_name)
        else:
            logging.info('Part score: %s - %i\t%s - %i',
                first_name, score[0], second_name, score[1])
        main_menu()


def check_winner(field):
    """
        Mehod for checking if there is a winner now

        Args:
            field (list): playing field
        Returns:
            str: 'first' if the first player wins or 'second' if the second player wins
    """
    first = False
    second = False
    for row in field:
        first_win = True
        second_win = True
        for cell in row:
            first_win = first_win and cell == 'x'
            second_win = second_win and cell == 'o'
        if first_win:
            first = True
            break
        if second_win:
            second = True
            break

    for coll in range(3):
        first_win = True
        second_win = True
        for cell in range(3):
            first_win = first_win and field[cell][coll] == 'x'
            second_win = second_win and field[cell][coll] == 'o'
        if first_win:
            first = True
            break
        if second_win:
            second = True
            break

    if ((field[0][0] == 'x' and field[2][2] == 'x') or
        (field[0][2] == 'x' and field[2][0] == 'x')) and field[1][1] == 'x':
        first = True
    if ((field[0][0] == 'o' and field[2][2] == 'o') or
        field[0][2] == 'o' and field[2][0] == 'o') and field[1][1] == 'o':
        second = True

    if first:
        return 'first'
    if second:
        return 'second'
    return 'None'

def print_field(field):
    """
        Mehod for print the playing field

        Args:
            field (list): playing field
    """
    for row in field:
        for cell in row:
            print(cell, end = '\t')
        print()

if __name__ == '__main__':
    main_menu()
