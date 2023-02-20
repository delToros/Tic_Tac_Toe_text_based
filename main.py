import random
import os

# -------- First Setup of vars -------- #

def the_game():

    list_of_spaces = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }

    field = f"{list_of_spaces['1']} | {list_of_spaces['2']} | {list_of_spaces['3']}\n" \
            f"---------\n" \
            f"{list_of_spaces['4']} | {list_of_spaces['5']} | {list_of_spaces['6']}\n" \
            f"---------\n" \
            f"{list_of_spaces['7']} | {list_of_spaces['8']} | {list_of_spaces['9']}\n"

    # This dic is for computer to be more aggressive. He can't just choose any empty field. He has to choose field next to user input
    comp_choice_dic = {
        '1': [2, 5, 4],
        '2': [3, 1, 5],
        '3': [6, 2, 5],
        '4': [1, 5, 7],
        '5': [2, 8, 1, 9, 3, 4, 6, 7],
        '6': [3, 9, 5],
        '7': [4, 5, 8],
        '8': [5, 7, 9],
        '9': [6, 5, 8],
    }

    game_is_on = True
# ----------------------------------- #

# -------- Game Begins. Choose User input type-------- #
    print("Hello! Welcome to text-based TicTacToe game!")

    user_symbol = input("Please choose your symbol: O or X\n").upper()

    if user_symbol == "O":
        computer_symbol = "X"
    elif user_symbol == "X":
        computer_symbol = "O"
    else:
        print("Bzzz! Wrong symbol! Only x or o. Try again!")
        ser_symbol = input("Please choose your symbol: O or X\n").upper()
        if user_symbol == "O":
            computer_symbol = "X"
        elif user_symbol == "X":
            computer_symbol = "O"
        else:
            print("This is unbelievable! Goodbye!")
            raise SystemExit

    print("This is your field")
    print(field)
# ----------------------------------- #

# -------- Game Loop-------- #
    while game_is_on:
        # User Moves
        any_moves_left = [list_of_spaces[item] for item in list_of_spaces if isinstance(list_of_spaces[item], int)]
        user_move = str(input(f"Please select number were you want to place {user_symbol}\n"))

        # Checking if user chose empty field
        if int(user_move) in any_moves_left:
            pass
        else:
            print(f"Sorry you can't choose '{user_move}' - it is already been chosen. Try Again.")
            user_move = str(input(f"Please select number were you want to place {user_symbol}\n"))
            if int(user_move) in any_moves_left:
                pass
            else:
                print(f"What did I just say? Goodbye. It is impossible to play with you.")
                raise SystemExit

        # Deleting the field (that user chose) from computer choices
        for i in comp_choice_dic:
            for a in comp_choice_dic[i]:
                if a == int(user_move):
                    comp_choice_dic[i].remove(a)

        # Putting user choice on the field
        list_of_spaces[user_move] = user_symbol
        field = f"{list_of_spaces['1']} | {list_of_spaces['2']} | {list_of_spaces['3']}\n" \
                f"---------\n" \
                f"{list_of_spaces['4']} | {list_of_spaces['5']} | {list_of_spaces['6']}\n" \
                f"---------\n" \
                f"{list_of_spaces['7']} | {list_of_spaces['8']} | {list_of_spaces['9']}\n"
        print(field)
        print("-----------------------------------------------")

        # Checking if it was a winning move
        if (list_of_spaces['1'] == list_of_spaces['2'] == list_of_spaces['3']) or \
           (list_of_spaces['4'] == list_of_spaces['5'] == list_of_spaces['6']) or \
           (list_of_spaces['7'] == list_of_spaces['8'] == list_of_spaces['9']) or \
           (list_of_spaces['1'] == list_of_spaces['5'] == list_of_spaces['9']) or \
           (list_of_spaces['3'] == list_of_spaces['5'] == list_of_spaces['7']) or \
           (list_of_spaces['1'] == list_of_spaces['4'] == list_of_spaces['7']) or \
           (list_of_spaces['2'] == list_of_spaces['5'] == list_of_spaces['8']) or \
           (list_of_spaces['3'] == list_of_spaces['6'] == list_of_spaces['9']):
            game_is_on = False
            print("Game over. You Won")
            new_game = input("Would you like to play another game? Y/N\n").upper()
            if new_game == "Y":
                os.system('cls')
                the_game()
            else:
                print("Goodbye!")
                raise SystemExit

        # If not won, we are checking if there are any other possible moves
        any_moves_left = [list_of_spaces[item] for item in list_of_spaces if isinstance(list_of_spaces[item], int)]
        if len(any_moves_left) > 0:
            pass
        else:
            print("Game Over. Its a draw, no more moves left.")
            game_is_on = False
            new_game = input("Would you like to play another game? Y/N\n").upper()
            if new_game == "Y":
                os.system('cls')
                the_game()
            else:
                print("Goodbye!")
                raise SystemExit

        # Computer moves. Except if only limited number of moves are available (see vars)
        print('Computer moves')

        # Long line of code to check if user already put
        if (list_of_spaces['1'] == list_of_spaces['2']) and isinstance(list_of_spaces['3'], int):
            computer_move = '3'
        elif (list_of_spaces['4'] == list_of_spaces['5']) and isinstance(list_of_spaces['6'], int):
            computer_move = '6'
        elif (list_of_spaces['7'] == list_of_spaces['8']) and isinstance(list_of_spaces['9'], int):
            computer_move = '9'
        elif (list_of_spaces['1'] == list_of_spaces['5']) and isinstance(list_of_spaces['9'], int):
            computer_move = '9'
        elif (list_of_spaces['3'] == list_of_spaces['5']) and isinstance(list_of_spaces['7'], int):
            computer_move = '7'
        elif (list_of_spaces['1'] == list_of_spaces['4']) and isinstance(list_of_spaces['7'], int):
            computer_move = '7'
        elif (list_of_spaces['2'] == list_of_spaces['5']) and isinstance(list_of_spaces['8'], int):
            computer_move = '8'
        elif (list_of_spaces['3'] == list_of_spaces['6']) and isinstance(list_of_spaces['9'], int):
            computer_move = '9'

        elif (list_of_spaces['1'] == list_of_spaces['3']) and isinstance(list_of_spaces['2'], int):
            computer_move = '2'
        elif (list_of_spaces['4'] == list_of_spaces['6']) and isinstance(list_of_spaces['5'], int):
            computer_move = '5'
        elif (list_of_spaces['7'] == list_of_spaces['9']) and isinstance(list_of_spaces['8'], int):
            computer_move = '8'
        elif (list_of_spaces['1'] == list_of_spaces['9']) and isinstance(list_of_spaces['5'], int):
            computer_move = '5'
        elif (list_of_spaces['3'] == list_of_spaces['7']) and isinstance(list_of_spaces['5'], int):
            computer_move = '5'
        elif (list_of_spaces['1'] == list_of_spaces['7']) and isinstance(list_of_spaces['4'], int):
            computer_move = '4'
        elif (list_of_spaces['2'] == list_of_spaces['8']) and isinstance(list_of_spaces['5'], int):
            computer_move = '5'
        elif (list_of_spaces['3'] == list_of_spaces['9']) and isinstance(list_of_spaces['6'], int):
            computer_move = '6'

        elif (list_of_spaces['2'] == list_of_spaces['3']) and isinstance(list_of_spaces['1'], int):
            computer_move = '1'
        elif (list_of_spaces['5'] == list_of_spaces['6']) and isinstance(list_of_spaces['4'], int):
            computer_move = '4'
        elif (list_of_spaces['8'] == list_of_spaces['9']) and isinstance(list_of_spaces['7'], int):
            computer_move = '7'
        elif (list_of_spaces['5'] == list_of_spaces['9']) and isinstance(list_of_spaces['1'], int):
            computer_move = '1'
        elif (list_of_spaces['5'] == list_of_spaces['7']) and isinstance(list_of_spaces['3'], int):
            computer_move = '3'
        elif (list_of_spaces['4'] == list_of_spaces['7']) and isinstance(list_of_spaces['1'], int):
            computer_move = '1'
        elif (list_of_spaces['5'] == list_of_spaces['8']) and isinstance(list_of_spaces['2'], int):
            computer_move = '2'
        elif (list_of_spaces['6'] == list_of_spaces['9']) and isinstance(list_of_spaces['3'], int):
            computer_move = '3'
        else:
            try:
                computer_move = str(random.choice(comp_choice_dic[user_move]))
            except IndexError:
                computer_move = str(random.choice(str(any_moves_left)))

        # Deleting the field (that computer chose) from computer choices
        for i in comp_choice_dic:
            for a in comp_choice_dic[i]:
                if a == int(computer_move):
                    comp_choice_dic[i].remove(a)

        # Putting computer choice on the field
        list_of_spaces[computer_move] = computer_symbol
        field = f"{list_of_spaces['1']} | {list_of_spaces['2']} | {list_of_spaces['3']}\n" \
                f"---------\n" \
                f"{list_of_spaces['4']} | {list_of_spaces['5']} | {list_of_spaces['6']}\n" \
                f"---------\n" \
                f"{list_of_spaces['7']} | {list_of_spaces['8']} | {list_of_spaces['9']}\n"
        print(field)

        # Checking if it was a winning move
        if (list_of_spaces['1'] == list_of_spaces['2'] == list_of_spaces['3']) or \
           (list_of_spaces['4'] == list_of_spaces['5'] == list_of_spaces['6']) or \
           (list_of_spaces['7'] == list_of_spaces['8'] == list_of_spaces['9']) or \
           (list_of_spaces['1'] == list_of_spaces['5'] == list_of_spaces['9']) or \
           (list_of_spaces['3'] == list_of_spaces['5'] == list_of_spaces['7']) or \
           (list_of_spaces['1'] == list_of_spaces['4'] == list_of_spaces['7']) or \
           (list_of_spaces['2'] == list_of_spaces['5'] == list_of_spaces['8']) or \
           (list_of_spaces['3'] == list_of_spaces['6'] == list_of_spaces['9']):
            print("Game Over. Computer Won.")
            game_is_on = False
            new_game = input("Would you like to play another game? Y/N\n").upper()
            if new_game == "Y":
                os.system('cls')
                the_game()
            else:
                print("Goodbye!")
                raise SystemExit

        # If not won, we are checking if there are any other possible moves
        any_moves_left = [list_of_spaces[item] for item in list_of_spaces if isinstance(list_of_spaces[item], int)]
        if len(any_moves_left) > 0:
            pass
        else:
            print("Game Over. Its a draw, no more moves left.")
            game_is_on = False
            new_game = input("Would you like to play another game? Y/N\n").upper()
            if new_game == "Y":
                os.system('cls')
                the_game()
            else:
                print("Goodbye!")
                raise SystemExit


the_game()


