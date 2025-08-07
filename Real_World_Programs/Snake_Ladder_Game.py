print("Snake_Ladder_Game".center(60,"*"))
import random
import sys


def dice():
    return random.randint(1,6)

def first_player():
    global player1_score
    player1_status = input(f"\n{player1} want to [C]ontinue or [E]xit: ").upper()
    if player1_status == "C":
        player1_turn = dice()
        player1_score += player1_turn
        if player1_score in snakes:
            player1_score = snakes[player1_score]
            print(f"\n{player1}'s turn: \nDice:{player1_turn} \n-----Snake Bite----\nBoard Position: {player1_score}")
        elif player1_score in ladders:
            player1_score = ladders[player1_score]
            print(f"\n{player1}'s turn: \nDice: {player1_turn} \n----ladder----\nBoard Position: {player1_score}")
        else:
            print(f"\n{player1}'s turn: \nDice: {player1_turn} \nBoard Position: {player1_score}")
    elif player1_status == "E":
        print(f'{player1} quit the game.\n\n{player2} Won the Game!!!!!!!!!')
        sys.exit()


def second_player():
    global player2_score
    player2_status = input(f"\n{player2} want to [c]ontinue or [E]xit: ").upper()
    if player2_status == 'C':
        player2_turn = dice()
        player2_score += player2_turn
        if player2_score in snakes:
            player2_score = snakes[player2_score]
            print(f"\n{player2}'s turn: \nDice: {player2_turn} \n----Snake Bite----\nBoard Position: {player2_score}")
        elif player2_score in ladders:
            print(f"\n{player2}'s turn: \nDice: {player2_turn} \n----Ladder----\nBoard Position: {player2_score}")
        else:
            print(f"\n{player2}'s turn: \nDice: {player2_turn} \nBoard Position: {player2_score}")
    elif player2_status == "E":
        print(f"{player2} quit the Game \n\n{player1} Won the Game!!!!!!!!!")
        sys.exit()



player1 = input("Enter player1: ").title()
player2 = input("Enter player2: ").title()

player1_score = 0
player2_score = 0

winning_point = 100

snakes={17:7, 54:34, 62:19, 64:60, 87:36, 93:73, 94:75, 98:79}
ladders={1:38, 4:14, 9:31, 21:42, 28:84, 51:67, 72:91, 80:99}
