import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors \n" )
    computer = random.choice(['r', 'p', 's'])

    print(f'user chose {user}')
    print(f'computer chose  {computer}')
    if user == computer:
     print('tie')

    if is_win(user, computer):
        return 'You win!'
      
   
def is_win(player, opponent):
    return 'empty'
play()