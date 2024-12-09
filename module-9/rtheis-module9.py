#Rachel Theis
#CSD 325
#Module 9.2 Assignment 
#12.8.24

#This program will produce data from a randomly generated deck of cards using an API, and print the data in a formatted and unformatted version. 

import requests
import json

#API with no formatting 
response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/")
print(response.json())


#API with formatting 
response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/")

if response.status_code == 200:

    data = response.json()
    deck_id = data["deck_id"]

    print(f"Deck ID: {deck_id}")
    print(f"Shuffled Deck Remaining Cards: {data['remaining']} cards")

    draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
    draw_response = requests.get(draw_url)

    if draw_response.status_code == 200:
        draw_data = draw_response.json()
        print("\nDrawn Cards:")
        for card in draw_data["cards"]:
            print(f"{card['value']} of {card['suit']}")
    else:
        print(f"Error: Unable to draw cards. Status code: {draw_response.status_code}")

