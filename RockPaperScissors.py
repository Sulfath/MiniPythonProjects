import random

def play():
    player = input("What is you choice? r for Rock, p for Paper and S for scissors. \n")
    opponent = random.choice(['r','p','s'])
    print(opponent)
    if player==opponent:
       return "It /'s a tie"
    if is_win(player,opponent):
        return "You win"
    
    return "You lost!!"

def is_win(player,opponent):
    if (player == "r" and opponent == "p") or (player == "r" and opponent == "s") or (player == "s" and opponent == "p"):
        return True



print(play())