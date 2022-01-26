from cgitb import handler, text
from tkinter import *
from random import choice
import random

root = Tk()
root.title("Blackjack")
root.geometry("300x300")

ace = {"Ace": 11}
king = {"King": 10}
queen = {"Queen": 10}
jack = {"Jack": 10}
nine = {"Nine": 9}
eight = {"Eight" : 8}
seven = {"Seven": 7}
six = {"Six": 6}
five = {"Five": 5}
four = {"Four": 4}
three = {"Three": 3}
two = {"Two": 2}
one = {"One": 1}


def start_game(widget):
    global hand_total
    hand = [choice([ace["Ace"],king["King"],queen["Queen"],jack["Jack"],nine["Nine"],eight["Eight"],seven["Seven"],six["Six"],five["Five"],four["Four"],three["Three"],two["Two"],one["One"]]),choice([ace["Ace"],king["King"],queen["Queen"],jack["Jack"],nine["Nine"],eight["Eight"],seven["Seven"],six["Six"],five["Five"],four["Four"],three["Three"],two["Two"],one["One"]])]
    hand_total = sum(hand)
    widget.pack_forget()
    Hand_Display.config(text=f"Hand Total: {hand_total}")
    hit_button.pack()
    stand_button.pack()
    Dealer_Hand_Display.pack()
    game_status.pack()

def hit(total_cards):
    global hand_total
    card = choice([ace["Ace"],king["King"],queen["Queen"],jack["Jack"],nine["Nine"],eight["Eight"],seven["Seven"],six["Six"],five["Five"],four["Four"],three["Three"],two["Two"],one["One"]])
    hand_total = hand_total + card
    print(hand_total)
    Hand_Display.config(text=f"Hand Total: {hand_total}")
    if hand_total >= 22:
        game_status.config(text="YOU LOST (BUST)", fg="#FF0000")

dealer_hand = sum([choice([ace["Ace"],king["King"],queen["Queen"],jack["Jack"],nine["Nine"],eight["Eight"],seven["Seven"],six["Six"],five["Five"],four["Four"],three["Three"],two["Two"],one["One"]]),choice([ace["Ace"],king["King"],queen["Queen"],jack["Jack"],nine["Nine"],eight["Eight"],seven["Seven"],six["Six"],five["Five"],four["Four"],three["Three"],two["Two"],one["One"]])])
def stand():
    global dealer_hand
    if dealer_hand <= 17:
        card = choice([ace["Ace"],king["King"],queen["Queen"],jack["Jack"],nine["Nine"],eight["Eight"],seven["Seven"],six["Six"],five["Five"],four["Four"],three["Three"],two["Two"],one["One"]])
        dealer_hand = dealer_hand + card
        if dealer_hand <= 17:
            card = choice([ace["Ace"],king["King"],queen["Queen"],jack["Jack"],nine["Nine"],eight["Eight"],seven["Seven"],six["Six"],five["Five"],four["Four"],three["Three"],two["Two"],one["One"]])
            dealer_hand = dealer_hand + card
        elif dealer_hand >= 22:
            Dealer_Hand_Display.config(text=f"Dealer Hand: {dealer_hand}")
            game_status.config(text="YOU WIN (DEALER BUST)", fg="green")
        
        else:
            if dealer_hand >= hand_total:
                game_status.config(text="YOU LOST", fg="green")
                Dealer_Hand_Display.config(text=f"Dealer Hand: {dealer_hand}")
                
            elif dealer_hand <= hand_total:
                game_status.config(text="YOU WIN", fg="green")
                Dealer_Hand_Display.config(text=f"Dealer Hand: {dealer_hand}")

    elif dealer_hand >= 22:
        Dealer_Hand_Display.config(text=f"Dealer Hand: {dealer_hand}")
        game_status.config(text="YOU WIN (DEALER BUST)", fg="green")
        
    else:
        if dealer_hand >= hand_total:
            game_status.config(text="YOU LOST", fg="green")
            Dealer_Hand_Display.config(text=f"Dealer Hand: {dealer_hand}")
            
        elif dealer_hand <= hand_total:
            game_status.config(text="YOU WIN", fg="green")
            Dealer_Hand_Display.config(text=f"Dealer Hand: {dealer_hand}")
            
start_game_button = Button(root, text="Start Game", command=lambda: start_game(start_game_button))
start_game_button.pack()

Hand_Display = Label(root, text="Hand Total:")
Hand_Display.pack()

hit_button = Button(root, text="Hit", command=lambda: hit(hand_total))

stand_button = Button(root, text="Stand", command=stand)

Dealer_Hand_Display = Label(root, text="Dealer Hand: ")

game_status = Label(root, text = "Game Status: NONE")

root.mainloop()