# Beat-the-odds

Version requirements:

Python 3.8.5
pygame 2.0.1


Card game where players take chances predicting the color, value or suit of a card. 

*About the game:*
Each player will start with a deck of 52 cards.
Player automatically loses if they run out of cards. 
Up to 9 players can play at a time.
Card value ranking is as follow: Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King.


Start:

You will start by selecting the number of players and hitting "Start".
![Intro](https://user-images.githubusercontent.com/64381840/198891966-1b668f8d-a9a4-4afa-a8c4-f2561fd8b830.png)

Round 1:

The game will randomly select a player to start. They must guess the color of the card.
![start of the game](https://user-images.githubusercontent.com/64381840/198894641-cdc35f0f-7666-416d-83a9-6e6d8317912c.png)

Round 2:
You will need to guess if the next card is higher or lower (in value) to your previous card. Guessing incorrectly will sent you back to round 1.
(You will lose if the value is the same)
![start of the game](https://user-images.githubusercontent.com/64381840/198895338-0447b99d-f786-4ea4-a1df-d82083460027.png)

Round 3:
Players will guess whether it will be inside (value more than 1st card and less than 2nd card) or outside (Value less than 1st card and more than 2nd card). If the 3rd card is the same as either the 1st or 2nd card you lose for both outside and inside guesses. Guessing incorrectly will sent you back to round 1.
![3 round](https://user-images.githubusercontent.com/64381840/198895587-c919c2f2-49a9-43fd-9027-7f31fedceca1.png)

Round 4:
Last round will have players guess the suit of the next card (clubs (♣), diamonds (♦), hearts (♥), and spades (♠)). Guessing incorrectly will sent you back to round 1.
![4 round](https://user-images.githubusercontent.com/64381840/198896087-e3a29487-e6ed-43a4-a980-dc0599a3341c.png)

