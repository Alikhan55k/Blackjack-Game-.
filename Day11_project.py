logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
import random
my_card1=random.choice(cards)
my_card2=random.choice(cards)
com_card1=random.choice(cards)
com_card2=random.choice(cards)
your_list=[my_card1,my_card2]
com_list=[com_card1,com_card2]
wish=input("Do you want to play blackjack:")
if wish=="yes":
    print(f"Your cards:{your_list}, current score: {my_card1+my_card2}")
    print(f"Computer's first card:{com_card1}")
    another=input("Type y to get another card: ")
    if another=="y":
        my_card3=random.choice(cards)
        if my_card3==11 and (my_card1+my_card2)>9:
            my_card3=1
        your_list.append(my_card3)
        my_total=my_card1+my_card2+my_card3
        com_total=com_card1+com_card2
        if my_total<17:
            my_card4=random.choice(cards)
            my_total+=my_card4
            your_list.append(my_card4)
            if my_total<17:
                my_card5=random.choice(cards)
                my_total+=my_card5
                your_list.append(my_card5)
        print(f"Your cards {your_list}, current score: {my_total}")
        if com_total<17:
            com_card3=random.choice(cards)
            com_total+=com_card3
            com_list.append(com_card3)
            if com_total<17:
                com_card4=random.choice(cards)
                com_total+=com_card4
                com_list.append(com_card4)
        print(f"Computer's final hand {com_list}, final score: {com_total}")
        if my_total==com_total:
            print("\nDraw")
        elif my_total>21:
            print("You loss")
        elif com_total>21:
            print("You Win")
        elif my_total>com_total:
            print("You Win")
        elif com_total>my_total:
            print("You loss")
