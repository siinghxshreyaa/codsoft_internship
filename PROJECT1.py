
   
    #ROCK PAPER SCISSOR GAME

import random
rock= ''''
       ______
_____'   ____)
        (_____)
        (_____)
        (____)
_____'______)
'''

paper='''
     _______
___'    _____)_____
          _________)
          _________)
        __________)
___'__________)
    
'''
scissor='''
     ________
____'     _____)______
              _________)
              __________)
              ____)
____'____________)
'''
game_images=[rock,paper,scissor]
user_choice=int(input("Enter your choice: 0 for ROCK ,1 for Paper,2 for Scissor:"))
if user_choice >= 3 or user_choice <0:
    print("You enterd invalid number,You lose.")
else:
    print(game_images[user_choice])
    comp_choice=random.randint(0,2)
    print("Computer Chose:")
    print(game_images[comp_choice])
    if comp_choice== user_choice:
        print("IT'S A DRAW \n")
        print("PLAY AGAIN")
    elif comp_choice ==0 and user_choice==2:
        print("COMPUTER WON !! YOU LOSE \n")
        print("PLAY AGAIN !!!")
    elif user_choice ==0 and comp_choice==2:
        print("YOU WON !! COMPUTER LOSE\n")
        print("PLAY AGAIN")
    elif comp_choice >user_choice:
        print("CCOMPUTER WON !! YOU LOSE \n")
        print("PLAY AGAIN")
    elif user_choice > comp_choice:
        print("YOU WON !! COMPUTER LOSE \n")
        print("PLAY AGAIN")
        
print("--------------x---------------")
    