#import what we need
from random import randint
def Start_game():
    #make secret number
    secret_num = randint(1,20)
    try:
        i = 0

        while i<=3:

            i +=1
            player = input("Can you guess secret number?: ") 

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
Start_game()