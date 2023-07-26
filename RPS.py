import random
random=random.randint(1,3)
operation=int(input(" enter 1 for rock,2 for paper and 3 for scissor: "))
word1="1"
word2="2"
word3="3"
if (operation==word1 and random==word1) or (operation==word2 and random==word2) or (operation==word3 and random==word3):
    print("its a tie")
if (operation==word1 and random==word3) or (operation==word2 and random==word1) or (operation==word3 and random==word2):
    print("you win")
if (operation==word1 and random==word2) or (operation==word2 and random==word3) or (operation==word3 and random==word1):
    print("you loose try again you bot")