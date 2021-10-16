import random
from BlackJack_Art import logo
playgame=(input("Do you want to play a game of Blackjack? Type 'y' or 'n':"))
if playgame=='y':
    print(logo)
    a=random.randint(1,13)
    b=random.randint(1,13)
    c=random.randint(1,13)
    d=random.randint(1,13)
    e=random.randint(1,10)
    x=a+b
    y=c+d
    print(f'Your Cards are: [{a},{b}]')
    print(f"Computer's first card:{c}")
    anothercardchoice=input("Type 'y' to get another cards, type 'n' to pass:")
    if anothercardchoice=='y': 
        x+=e
    if a>=10 and b>=10 and c>=10:
        a=10
        c=10
        b=10
    if x>21 or x<y:
        print(f"Computer's Final Hand:[{c},{d}]")
        print(f"Yours's Final Hand:[{a},{b},{e}]")
        print("Computer Wins")
    else:
        print(f"Computer's Final Hand:[{c},{d}]")
        print(f"Yours's Final Hand:[{a},{b},{e}]")
        print("You Wins")
else:
    print("Ok, Bye")  