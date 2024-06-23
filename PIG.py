import random

def roll():
  min = 1
  max = 6
  roll = random.randint(min,max)
  return roll 


while True:
  players = input("\n Enter number of players(2-4) :")
  if players.isdigit():
    players =int(players)
    if(players <2 or players>4):
     print("The number of players should be between 2 and 4")
    else:
      break
  else:
     print("Invalid input")

max_score = 20
players_scores = [0 for _ in range(players)]


while max(players_scores) < max_score:
    for i in range(players):
        current_score=0
        print("Player no. ",i+1," turn has just started.")

        while True:
            choice=input("Do you want to roll (y/n) ?")
            if(choice.lower() == 'y'):
                value= roll()
                print("The value : ",value)
                print("\n The curent score : ",current_score)
                if(value == 1):
                    print("You rolled a 1! Your game finished and your current score : ",current_score)   
                    break
                else:
                    current_score = current_score+value                   
            else:
                print("Invalid input")
        players_scores[i] = current_score      
        print("Your total score is:", players_scores[i])


highest_score = max(players_scores)  
winner =players_scores.index(highest_score)    

print("\n The highest score : ",highest_score, " and the winner is ",winner+1, " player.")


              