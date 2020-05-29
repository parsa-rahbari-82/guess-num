#import what we need
from random import randint




def game_help():
    print('''Hi and welcome to guess-num game!
You should enter a number to guess the secret number
type HELP to see help :)\n ''')



    
def Start_game():
    #make secret number
    secret_num = randint(1,20)
    try:
        i = 0

        while i<=3:

            i +=1
            player = input("Can you guess secret number?: ") 
            if player == 'HELP':
                game_help()
                continue
            player = int(player)

            #Hint to player

            if player == secret_num:
                print("You win! the secret number was",secret_num)
                break

            elif player<secret_num:
                print("""Hint: The secret number is bigger
than your guess number!""")
                   


            elif player>secret_num:
                print("""Hint: The secret number is smaller 
than your guess number!""")



    #if player do not enter a number get an error    
    except ValueError:
        print("Error: PLease Enter a number(integer)!")



#call function to run Game
game_help()
Start_game()
