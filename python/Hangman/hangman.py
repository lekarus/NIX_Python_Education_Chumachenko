import random


def main_menu():
    print('Выберите действие:')
    print('1. Начать игру')
    print('2. Посмотреть прошлые слова')
    print('3. Выход')
    chose = input()
    while chose not in ('1', '2', '3'):
        print('Выберите действие:')
        print('1. Начать игру')
        print('2. Посмотреть прошлые слова')
        print('3. Выход')
        chose = input()
    if chose == '1':
        start_game()
    elif chose == '2':
        prev_words()
    else:
        return


def start_game():
    conceived_words = []
    guessed_words = []
    all_words = open('words.txt', 'r')
    file_guessed_words = open('prev_words.txt', 'r')
    for line in all_words:
        if line[-1] == '\n':
            conceived_words.append(line[:-1])
        else:
            conceived_words.append(line)
    for line in file_guessed_words:
        if line[-1] == '\n':
            guessed_words.append(line[:-1])
        else:
            guessed_words.append(line)
    try_counter = 9
    conceived_words = list(set(conceived_words) - set(guessed_words))
    if len(conceived_words) == 0:
        print('К сожалению, слова закончились')
        return
    real_word = random.choice(conceived_words).lower()
    main_word = ['*' for i in real_word]
    main_game(try_counter, main_word, real_word)
    all_words.close()
    file_guessed_words.close()


def prev_words():
    f = open('prev_words.txt', 'r')
    words = []
    for line in f:
        words.append(line)
    if len(words) == 0:
        print('Вы еще ничего не угадали.\n\n')
    else:
        print(f'У вас {len(words)} угаданных слов(а):')
        for word in words:
            print(word, end='')
    print('\n\n')
    main_menu()


def main_game(t_c, m_w, r_w):
    try_letters = []
    while t_c != 0:
        print(f'Осталось ходов: {t_c}')
        print(f'Слово: {str(m_w)}')
        print(f'Испробованые буквы: {try_letters}')
        print('Введите вашу букву: ', end='')
        letter = input().lower()
        while letter in try_letters or len(letter) != 1:
            if len(letter) != 1:
                print('Некорректный ввод, введите 1 букву: ', end='')
            else:
                print('Вы уже использовали эту букву, попробуйте другую: ', end='')
            letter = input().lower()
        try_letters.append(letter)
        if letter in r_w:
            print(f'Поздравляю, вы открыли {r_w.count(letter)} букву/ы\n\n')
            tmp = 0
            for i in range(r_w.count(letter)):
                cur_l = r_w.lower().index(letter, tmp, len(r_w))
                m_w[cur_l] = r_w[cur_l]
                tmp = cur_l + 1
        else:
            print('Вы не открыли ни одной буквы\n\n')
            t_c -= 1
        if m_w.count('*') == 0:
            print(f'Поздравляю, вы отгадали слово: {r_w.capitalize()}')
            f = open('prev_words.txt', 'a')
            f.write(r_w.capitalize() + '\n')
            f.close()
            break
        if t_c == 0:
            print('К сожалению, вы проиграли')
    main_menu()


if __name__ == '__main__':
    clear_prev = open('prev_words.txt', 'w')
    clear_prev.close()
    main_menu()
