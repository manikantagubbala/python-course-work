print("Snake_Ladder_Game".center(60,"*"))
import random
import sys

def dice():
    return random.randint(1,6)


player1=input("Enter Name of the Player1: ").capitalize()
player2=input("Enter Name of the Player2: ").capitalize()

snakes={17:7, 54:34, 62:19, 64:60, 87:36, 93:73, 94:75, 98:79}
ladders={1:38, 4:14, 9:31, 21:42, 28:84, 51:67, 72:91, 80:99}

player1_score=0
player2_score=0

winning_point=100

while player1_score < winning_point and player2_score < winning_point:
    player1_status=input(f"\n{player1} want to [C]ontinue or [E]xit: ").upper()
    if player1_status == 'C':
        player1_turn = dice()
        player1_score += player1_turn
        if player1_score in snakes:
            player1_score = snakes[player1_score]
            print(f"\n{player1}'s turn: \nDice: {player1_turn} \n----Snake Bite----\n{player1} Board Position: {player1_score}")
        elif player1_score in ladders:
            player1_score = ladders[player1_score]
            print(f"\n{player1}'s turn: \nDice: {player1_turn} \n----Ladder----\n{player1} Board Position: {player1_score}")
        else:
            print(f"\n{player1}'s turn: \nDice: {player1_turn} \n{player1} Board Position: {player1_score}") 

    elif player1_status == 'E':
        print(f"\n{player1} quit the Game \n {player2} Won the Game!!!!!!")
        sys.exit()


    player2_status = input(f"\n{player2} want to [C]ontinue or [E]xit: ").upper()
    if player2_status == 'C':
        player2_turn = dice()
        player2_score += player2_turn
        if player2_score in snakes:
            player2_score = snakes[player2_score]
            print(f"\n{player2}'s turn: \nDice: {player2_turn} \n----Snake Bite----\n{player2} Board Position: {player2_score}")
        elif player2_score in ladders:
            player2_score = ladders[player2_score]
            print(f"\n{player2}'turn: \nDice: {player2_turn} \n----Ladder----\n{player2} Board Position: {player2_score}")
        else:
            print(f"\n{player2}'s turn: \nDice: {player2_turn} \n{player2} Board Position: {player2_score}")


    elif player2_status == 'E':
        print(f"\n{player2} quit the Game \n {player1} Won the Game!!!!!!!")
        sys.exit()

else:
    if player1_score > player2_score:
        print(f"\n\n{player1} Won the Game!!! ")
    elif player1_score == player2_score:
        print("\n\n Tie")
    else:
        print(f"\n\n{player2} Won the Game!!! ")        


