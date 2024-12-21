import random

def player_choice():
    while True:
        choice = input("Enter you choice (rock, paper, scissors):")
        if choice not in ['rock', 'paper', 'scissors']:
            print("Please choose either rock, paper or scissors")
        else:
            return choice
        
def computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def win_lose(player, computer, player_score, computer_score):
    if player == computer:
        print("Its's a tie!")
    elif(player == 'rock' and computer =='scissors') or\
        (player == 'scissors' and computer =='paper') or\
        (player == 'paper' and computer =='rock'):
        print("You win!")
        player_score += 1
    else:
        print("You lose!")
        computer_score += 1
    
    print (f"Your score: {player_score}     |     Computer's score: {computer_score}")
    return player_score, computer_score

def game():
    player_score = 0
    computer_score = 0
    while True:
        player = player_choice()
        computer = computer_choice()
        print(f"The computer chose: {computer}")

        player_score, computer_score = win_lose(player, computer, player_score, computer_score)

        continue_game = input("Do you want to continue?(yes/no):").lower()
        if continue_game != 'yes':
            print("Exiting game...")
            break
game()

