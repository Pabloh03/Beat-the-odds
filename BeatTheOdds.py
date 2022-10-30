import pygame, time
from random import randint, sample, shuffle

pygame.init()

#Setting the dimensions of the Game screen
x = 1100
y = 770

#Setting up colors of text and background
white = (255, 255, 255)
black = (0, 0, 0)

logo_path = "Logo\\"
card_path = "Cards\\"
button_path = "Buttons\\"

#Set up game
screen = pygame.display.set_mode((x,y))
logo_image = pygame.image.load(logo_path + "CardsLogo.png").convert()
logo_image = pygame.transform.scale(logo_image, (400, 350))
back_card = pygame.image.load(card_path + "cardback1.png").convert()
back_card = pygame.transform.scale(back_card, (190, 250))
clock = pygame.time.Clock()


#Every player will have: a hand, the round they are currently in and deck
class Deck: 
	def __init__(self):
		suit = ("hearts", "diamonds", "clubs", "spades")
		num = ('Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king')
		self.cards = [(y,x,"red") if y == 'hearts' or y == 'diamonds' else (y,x,"black") for x in num for y in suit]
	def count(self):
		return len(self.cards)
	def _deal(self, num_cards):
	#takes the num_cards and removes that many cards. Should throw and error if not enough cards to deal. 
		if len(self.cards) == 0:
			raise ValueError['All cards have been dealt']
		else:
			amount_deal = min([self.count(), num_cards])
			hand = sample(self.cards, k=amount_deal)
		for x in hand:
			self.cards.remove(x)
		return hand
	def shuffle(self):
		if len(self.cards) != 52:
			raise ValueError['Only full decks can be shuffled']
		return shuffle(self.cards)
	def deal_card(self):
		#Should deal just one card using _deal. If deck empty it should throw an error. 
		return self._deal(1)[0]
	def deal_hand(self, num):
		#Should deal a number of cards based on the num given. IF not enough it should return error.
		return self._deal(num)
	def __repr__(self):
		return f'Deck of {self.count()} cards'

class Player:
	def __init__(self, username):
		self.username = username
		self.hand = []
		self.round = 1
		self.deck = Deck()
	def __repr__(self):
		return f'{self.username}'
	def add_card(self, card):
		self.hand.append(card)


#Display text on Screen
def message_display(text, location, size):

	def text_objects(text, font):
		textSurface = font.render(text, True, black)
		return textSurface, textSurface.get_rect()

	fontText = pygame.font.SysFont('freesanbold.ttf', size) #Type of font and text
	TextSurf, TextRect = text_objects(text, fontText)
	TextRect.center = location
	screen.blit(TextSurf, TextRect)

	pygame.display.update()

#Make a button clickable 
def ActionButton(Picture, coords, surface, size):
	image = pygame.image.load(button_path + Picture)
	image = pygame.transform.scale(image, size)
	imagerect = image.get_rect()
	imagerect.topright = coords
	surface.blit(image,imagerect)
	return (image,imagerect)

#Used on the first 3 rounds. To ask user select between two buttons.
def UserChoice(button1, button2):
	user_choice = 0
	done = False
	while not done:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					mouse = pygame.mouse.get_pos()
					if button1[1].collidepoint(mouse):
						user_choice = 1
						done = True
					elif button2[1].collidepoint(mouse):
						user_choice = 2
						done = True
	return user_choice

#Looks up card image
def card_lookup(card):
	card_selected = f'{card_path}{card[1]}_of_{card[0]}.png'
	card_image = pygame.image.load(card_selected).convert()
	card_image = pygame.transform.scale(card_image, (190, 250))
	return card_image

#Intro and game 4 rounds.
number_players = 1
def game_intro():
	intro = True
	
	global number_players
	while intro:
		message_display("Beat The Odds", ((550),(77)), 160)
		screen.blit(logo_image, [350, 190])
		Start = ActionButton('Start.png', [x-620, 600], screen, (175, 65))
		Quit = ActionButton('Quit.png', [x-305, 600], screen, (175, 65))
		Plus = ActionButton('Plus.png', [685, 690], screen, (65, 65))
		minus = ActionButton('Minus.png', [480, 690], screen, (65, 65))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			number_value = message_display(str(number_players), ((550), (720)), 90)
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				mouse = pygame.mouse.get_pos()
				if Start[1].collidepoint(mouse):
					intro = False
					#game_parameters()
				elif Quit[1].collidepoint(mouse):
					pygame.quit()
					quit()
				elif Plus[1].collidepoint(mouse):
					if number_players >= 9:
						message_display("Max of 9 players", ((550),(154)), 70)
					else:
						number_players += 1
						pygame.draw.rect(screen, white, (200, 130, 700, 65)) #Clears the Max player message.
						pygame.draw.rect(screen, white, (520, 690, 65, 65)) #Clears the Number of players
				elif minus[1].collidepoint(mouse):
					if number_players > 1:
						number_players -= 1
					pygame.draw.rect(screen, white, (200, 130, 700, 65)) #Clears the Max player message.
					pygame.draw.rect(screen, white, (520, 690, 65, 65)) #Clears the Number of players

		pygame.display.update()
		clock.tick(40)

def round_1(player):
	player_card = player.deck.deal_card()
	#Clears Screen
	screen.fill(white)

	#Displays messages and card
	message_display("Red or Black?", ((550),(77)), 175)
	red = ActionButton('Red.png', [x-620, 600], screen, (175, 65))
	black = ActionButton('Black.png', [x-305, 600], screen, (175, 65))
	message_display(f"{player}", ((550), (192)), 85)
	screen.blit(back_card, [455,260])
	pygame.display.update()

	#Waits for user to make a selection
	selection = UserChoice(red, black)
	pygame.display.update()
	clock.tick(40)
	#Logic for User selection.
	if (selection == 1 and player_card[2] == 'red') or (selection == 2 and player_card[2] == 'black'):
		message_display("Good job!", ((550), (710)), 85)
		screen.blit(card_lookup(player_card), [455,260])
		player.add_card(player_card)
		player.round += 1
		pygame.display.update()
		time.sleep(3)
	else:
		message_display("Wrong!", ((550), (710)), 85)
		screen.blit(card_lookup(player_card), [455,260])
		pygame.display.update()
		time.sleep(3)
		
def round_2(player):
	player_card = player.deck.deal_card()
	#Clears Screen
	screen.fill(white)

	#Set up for round 2
	current_card = player.hand[0]
	card_value = ('Ace',2,3,4,5,6,7,8,9,10,'jack','queen','king')
	
	#Buttons on Screen
	higher = ActionButton('Higher.png', [475, 600], screen, (175, 65))
	lower = ActionButton('Lower.png', [275, 600], screen, (175, 65))
	
	#Messages on Screen.
	message_display("Higher or Lower?", ((550),(77)), 175)
	message_display(f"{player}", ((550), (192)), 85)
	message_display("Next Card", (285, (y*.35)), 55)
	message_display("Your Card", (850, (y*.35)), 55)
	
	#Cards on Screen
	screen.blit(back_card, [190,320])
	screen.blit(card_lookup(current_card), [755, 320])
	
	#Adds buttons, messages and cards to screen
	pygame.display.update()
	
	#User choice
	selection = UserChoice(higher, lower)
	clock.tick(40)

	if selection == 1 and card_value.index(current_card[1]) < card_value.index(player_card[1]):
		message_display("Good job!", ((550), (710)), 85)
		screen.blit(card_lookup(player_card), [190,320])
		player.add_card(player_card)
		player.round += 1
		pygame.display.update()
		time.sleep(3)
	elif selection == 2 and card_value.index(current_card[1]) > card_value.index(player_card[1]):
		message_display("Good job!", ((550), (710)), 85)
		screen.blit(card_lookup(player_card), [190,320])
		player.add_card(player_card)
		player.round += 1
		pygame.display.update()
		time.sleep(3)
	else:
		message_display("Wrong!", ((550), (710)), 85)
		screen.blit(card_lookup(player_card), [190,320])
		player.hand = []
		player.round = 1
		pygame.display.update()
		time.sleep(3)

def round_3(player):
	player_card = player.deck.deal_card()
	screen.fill(white)

	current_cards = player.hand
		
	#Buttons on screen
	inside = ActionButton('Inside.png', [475, 600], screen, (175, 65))
	outside = ActionButton('Outside.png', [275, 600], screen, (175, 65))

	#Messages on Screen	
	message_display("Outside or Inside?", ((550),(77)), 175)
	message_display(f"{player}", ((550), (192)), 85)
	message_display("Next Card", (285, (269)), 55)
	message_display("Your Cards", (840, (269)), 55)
	
	#Cards on screen
	screen.blit(back_card, [190,320])
	screen.blit(card_lookup(current_cards[0]), [625, 320])
	screen.blit(card_lookup(current_cards[1]), [860, 320])
	
	pygame.display.update()
	selection = UserChoice(inside, outside)

	card_value = ('Ace',2,3,4,5,6,7,8,9,10,'jack','queen','king')
	values = [card_value.index(current_cards[0][1]), card_value.index(current_cards[1][1])]
	values.sort()
	clock.tick(40)

	#Logic
	if selection == 1 and card_value.index(player_card[1]) > values[0] and card_value.index(player_card[1]) < values[1]:
		message_display("Good job!", ((550), (710)), 85)
		screen.blit(card_lookup(player_card), [190,320])
		player.add_card(player_card)
		player.round += 1
		pygame.display.update()
		time.sleep(3)
	elif selection == 2 and (card_value.index(player_card[1]) < values[0] or card_value.index(player_card[1]) > values[1]):
		message_display("Good job!", ((550), (710)), 85)
		screen.blit(card_lookup(player_card), [190,320])
		player.add_card(player_card)
		player.round += 1
		pygame.display.update()
		time.sleep(3)
	else:
		message_display("Wrong!", ((550), (710)), 85)
		screen.blit(card_lookup(player_card), [190,320])
		player.hand = []
		player.round = 1
		pygame.display.update()
		time.sleep(3)

def round_4(player):
	player_card = player.deck.deal_card()
	screen.fill(white)
	
	#Text on screen
	message_display(f"{player}", ((550), (192)), 85)
	message_display("Guess a suit.", ((550),(77)), 175)

	#Buttons on screen
	spade = ActionButton('Spade.png', [350, 530], screen, (120, 120))
	heart = ActionButton('Heart.png', [520, 530], screen, (120, 120))
	diamond = ActionButton('Diamond.png', [690, 530], screen, (120, 120))
	club = ActionButton('Club.png', [860, 530], screen, (120, 120))
		
	#Cards on screen
	screen.blit(back_card, [455,245])
	pygame.display.update()
	clock.tick(40)

	#User selection
	done = ''
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				mouse = pygame.mouse.get_pos()
				if spade[1].collidepoint(mouse):
					user_choice = 'spades'
					done = True
				elif heart[1].collidepoint(mouse):
					user_choice = 'hearts'
					done = True
				if diamond[1].collidepoint(mouse):
					user_choice = 'diamonds'
					done = True
				elif club[1].collidepoint(mouse):
					user_choice = 'clubs'
					done = True
		pygame.display.update()

	if user_choice == player_card[0]:
		message_display("Good job!", ((550), (710)), 85)
		screen.blit(card_lookup(player_card), [455,245])
		player.round += 1
		pygame.display.update()
		time.sleep(3)
		message_display(f"{player} Wins!", ((550), (385)), 85)
		time.sleep(3)
		pygame.quit()
		quit()
	else:
		message_display("Wrong!", ((550), (710)), 85)
		screen.blit(card_lookup(player_card), [455,245])
		player.round = 1
		player.hand = []
		pygame.display.update()
		time.sleep(3)		

#The Game Starts
players = []
rounds = [round_1, round_2, round_3, round_4]
screen.fill(white)
game_intro()

#Creates player list and shuffles their card deck
for num in range(1, number_players + 1):
	players.append(Player(f"Player {num}"))
	players[num - 1].deck.shuffle()
	players[num - 1].deck.shuffle()
	players[num - 1].deck.shuffle()

shuffle(players)

while True:
	for player in players:
		if player.deck.count() == 0:
			screen.fill(white)
			message_display(f"{player} All your cards have been dealt. You lose.", ((550), (385)), 85)
			pygame.display.update()
		rounds[player.round - 1](player)


