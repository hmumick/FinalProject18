import random #import the random function in order to randomly select a number, which is used later on in the function
import pygame

#This game sets the size of the pygame display, and titles the name of the pygame window as Magnet Monopoly
pygame.init()
display_width= 880
display_height= 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Magnet Monopoly')

#Sets our created monopoly board as the background image and displays it
BackgroundIMG = pygame.image.load("monopolyboard.png")
gameDisplay.blit(BackgroundIMG, (0,0))

#Downloads the image of our board pieces, a hat and car, and puts them into the file
hatIMG = pygame.image.load("hat.png")
carIMG = pygame.image.load("car.png")

#this function gives the instructions on how to play Monopoly
def instructions():
  """This function gives the user instructions on how to play Magnet Monopoly"""
  print("Welcome to Magnet Monopoly! This is a 2 person game of monopoly, where the board is all Magnet themed! Like regular monopoly, you land on different properties, buy them or pay rent if they are already owned, and build houses and hotels on them if you all the properties of a given color set. There is no trading, and the moment one of you has no money, the game ends. You each start with 1500 dollars, so spend your money wisely, and good luck!")
  print("")
  return 

instructions() #this calls on the instructions function

#this is a class that has defines all of the spaces on the board, including how much they cost, how much each house costs, how much to pay for a given number of houses if someone lands on the space, determining who is the owner of that space, and figuring out their coordinates in the pygame window. 
class board_pieces:

  def __init__(self, name, owner, color, purchase_price, house_price, rent_price, house_1price, house_2price, house3_price, house4_price, hotel_price, location, house_owner, house_2count, house_count, hotel_owner,stationcount1, stationcount2, car_coodinates, hat_coordinates):
    self.name = name
    self.owner= owner
    self.color = color
    self.purchase_price = purchase_price 
    self.house_price = house_price
    self.rent_price = rent_price
    self.house_1price = house_1price
    self.house_2price = house_2price
    self.house3_price = house3_price
    self.house4_price = house4_price
    self.hotel_price= hotel_price
    self.location = location
    self.house_owner = house_owner
    self.house_2count = house_2count
    self.house_count = house_count
    self.hotel_owner = hotel_owner
    self.stationcount1 = stationcount1
    self.stationcount2 = stationcount2
    self.car_coordinates = car_coodinates
    self.hat_coordinates = hat_coordinates


Go= board_pieces('Go', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A',0, 0 , 0, 0 , 'none',0,0,(750,520), (750,520))
Pinto= board_pieces('Pinto', 'none', 'purple', 60,50, 2, 10,30,90,160,250,1, 'none', 0 , 0, 'none',0,0,(650, 520), (670, 520))
Chance1= board_pieces('Chance', 'Chance', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 2, 0 , 0 ,0, 'none',0 ,0, (580, 520), (600, 520))
Arnold= board_pieces('Arnold', 'none', 'purple',60,50,4,20,60,180,320,450, 3, 'none', 0 , 0, 'none',0,0, (510, 520), (530, 520))
Tax1= board_pieces('Tax', 'Tax', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 4, 'none',0 ,0 , 'none',0,0, (440, 520), (460, 520))
MakerSpaceStation= board_pieces('MakerSpace Station', "station", 'black', 200, 25 , 25, 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 5, 'none', 0 , 0, 'none',0,0, (370, 520), (390, 520))
Raite= board_pieces('Raite', 'none', 'light blue', 100,50,6,30,90,270,400,550,6, 'none', 0 , 0, 'none',0,0, (300, 520), (320, 520))
Chance2= board_pieces('Chance', 'Chance', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 7, 'none', 0 ,0 , 'none',0,0, (230, 520), (250, 520))
Gupta= board_pieces('Gupta', 'none', 'light blue',100,50,6,30,90,270,400,550,8, 'none',0 , 0, 'none',0,0, (160, 520), (180, 520))
Wickerhauser= board_pieces('Wickerhauser', 'none', 'light blue',120,50,8,40,100,300,450,600,9, 'none',0 , 0, 'none',0,0, (90, 520),(110, 520))
LOP= board_pieces('LOP', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 10, 'none', 0 ,0 , 'none',0,0, (0, 520),(0, 520))
Tenanbaum= board_pieces("Tenanbaum", 'none', 'pink',140, 100, 10,50, 150, 450, 25, 750, 11, 'none',0 , 0, 'none',0,0, (0, 440), (0, 455))
Chance3= board_pieces('Chance', 'Chance', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 12, 'none',0 , 0 , 'none',0,0, (0, 390), (0,410))
Nowakowski= board_pieces("Nowakowski", 'none', 'pink',140, 100, 10,50, 150, 450, 25, 750, 13, 'none',0 , 0, 'none',0,0, (0, 340), (0, 365))
Mcmenamin= board_pieces('Mcmenamin', 'none', 'pink',160, 100, 12,60, 180, 500, 700, 900, 15, 'none',0 , 0, 'none',0,0, (0, 290), (0,320))
GymStation= board_pieces("Gym Station", "station", 'N/A', 200, 25, 25, 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 16, 'none', 0 , 0, 'none',0,0, (0, 240), (0,275))
M_O= board_pieces('Mansfield Office' , 'none', 'orange',180, 100, 14, 70, 200, 550, 750, 950, 17, 'none',0 , 0, 'none',0,0, (0,190), (0, 225))
Chance4= board_pieces('Chance', 'Chance', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 18, 'none',0 , 0 , 'none', 0,0, (0,140), (0, 180))
Valverde= board_pieces("Valverde", 'none', 'orange',180,100, 14, 70, 200, 550, 750, 950, 19, 'none', 0 , 0, 'none',0,0, (0,90), (0,135))
Mejia= board_pieces("Mejia", 'none', 'orange',200, 100, 16, 80,220, 600, 800, 1000, 20, 'none', 0 ,0, 'none',0,0, (0,40), (0, 90))
Free_Parking= board_pieces('Free_Parking', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 21, 'none', 0 ,0 , 'none',0,0, (0,0), (0, 0))
Sanservino= board_pieces("Sanservino", 'none', "red", 260, 150, 22, 110, 330, 800, 975, 1150, 22, 'none',0 , 0, 'none',0,0, (90,0), (110, 0))
Valley= board_pieces("Valley", 'none', 'red', 260, 150, 22, 110, 330, 800, 975, 1150, 23, 'none',0 , 0, 'none',0,0, (160,0), (180, 0))
Chance5= board_pieces('Chance', 'Chance', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 24, 'none',0 , 0 , 'none',0,0, (230, 0), (250, 0))
Draesel= board_pieces("Draesel", 'none', "red", 280, 150, 24, 120, 360, 850, 1025, 1200, 25, 'none', 0 ,0, 'none',0,0, (300,0), (320, 0))
LabStation= board_pieces('Lab Station', 'station', 'N/A', 200, 25 , 25, 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 26, 'none', 0 ,0, 'none',0,0, (370,0), (390, 0))
Weisser= board_pieces("Weisser", 'none', "yellow",300, 200, 26, 130, 390, 900, 1100, 1275, 27, 'none', 0 ,0, 'none',0,0, (440,0), (460,0))
Fang= board_pieces("Fang", 'none', "yellow",300, 200, 26, 130, 390, 900, 1100, 1275, 28, 'none', 0 , 0, 'none',0,0, (510,0), (530,0))
Chance6= board_pieces('Chance', 'Chance', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 29, 'none', 0 , 0, 'none',0,0, (580, 0), (600,0))
Gerstein= board_pieces("Gerstein", 'none', "yellow",320, 200, 28, 150, 450, 1000, 1200, 1400, 30, 'none', 0 , 0, 'none',0,0, (650,0), (670,0))
GoToLOP= board_pieces("GoToLOP", 'GoToLOP', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 31, 'none', 0 ,0 , 'none',0,0,(750, 0), (750, 0))
OConnor= board_pieces('OConnor', 'none', "green", 220, 150, 18, 90, 250, 700, 875, 1050, 32, 'none',0 , 0, 'none',0,0, (750, 40), (750, 90))
Liu= board_pieces("Liu", 'none', "green",220, 150, 18, 90, 250, 700, 875, 1050, 33, 'none',0 , 0, 'none',0,0, (750, 90), (750, 135))
Chance7=  board_pieces('Chance', 'Chance', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 34, 'none', 0 ,0 , 'none',0,0, (750, 140), (750, 180))
Moskowitz= board_pieces("Moskowitz", 'none', "green",240, 150, 20,100,300,750,925, 1100, 35, 'none',0 , 0, 'none',0,0, (750, 190), (750, 225))
AuditoriumStation= board_pieces('Auditorium Station', "station", 'N/A', 200, 25 , 25, 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 36, 'none', 0 ,0, 'none',0,0, (750, 240), (750, 275))
Chance8=  board_pieces('Chance', 'Chance', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 37, 'none', 0 ,0 , 'none',0,0, (750, 290), (750, 320))
Guidance= board_pieces("guidance", 'none', "dark blue",400,200, 50, 200, 600, 1400, 1700, 2000, 38, 'none', 0 , 0, 'none',0,0, (750, 340), (750, 365))
Tax2= board_pieces('Tax', 'Tax', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 39, 'none', 0 ,0 , 'none',0,0,(750, 390), (750, 410))
RafOffice= board_pieces("Rafolowski's Office", 'none', "dark blue",350, 200, 35, 175, 500, 1100, 1300, 1500, 40, 'none',0 , 0, 'none',0,0, (750, 440), (750, 455))

#This class defines the 2 players in the game, including their name, where they are on the board, how much money they have, and how many stations they own
class Player:
  def __init__(self, name, location, money, station):
    self.name = name
    self.location = location 
    self.money = money
    self.station = station

#This list defines all the spacces on the board in order. That way, this list can be used as a way to determine where the player is on the board, and set their location to that space.
board= [Go, Pinto, Chance1, Arnold, Tax1, MakerSpaceStation, Raite, Chance2, Gupta, Wickerhauser, LOP, Tenanbaum, Chance3, Nowakowski, Mcmenamin, GymStation, M_O, Chance4, Valverde, Mejia, Free_Parking, Sanservino, Chance5, Valley, Draesel, LabStation, Weisser, Fang, Chance6, Gerstein, GoToLOP, OConnor, Liu, Chance7, Moskowitz, AuditoriumStation, Chance8, RafOffice, Tax2, Guidance]

#Initializing player 1, who starts at location 0 which is Go, has 1500 dollars, and doesn't own any stations
player1name = input("Player one, input your name. You will go first. ")
player1= Player(player1name, 0, 1500, 0)
#Tells the player he starts at Go
print(f"You are starting at {board[player1.location].name}") 

#Initializing player 2
player2name = input("Player two, input your name. ") 
player2= Player(player2name, 0, 1500, 0 )
#Tells the player he starts at Go
print(f"You are starting at {board[player2.location].name}") 

#Sets the minimum places the person can move at 2, and the maximum places the person can move at 12, just like rolling 2 dice
min = 2
max = 12

#Lists to see if the player owns all the spaces of a certain color, so they can start building houses and hotels on those spaces
color1=[]
color2=[]

#This loop escapes the game if you close the pygame window
for e in pygame.event.get():
    if e.type == pygame.QUIT:  
      quit()
#Sets a list of where the coordinates of the car and hat are. That way, when it's time to change the location of the car or hat, the previous image of the car/hat can be removed and replaced with the coordinates of the new image
player1character = []
player2character = []

#Game only occurs when the players have money
while player1.money > 0 and player2.money > 0:
  dice_answer1= input(f"{player1.name}, are you ready to roll the dice? Click enter to roll.")
#Pick a random integer between 2 and 12 for the player to move
  move = int(random.randint(min,max))
  print(f"{player1.name} rolled a {move}")
#Move the player to that location
  player1.location = player1.location + move

  if player1.location < 40:
#Set the image of the car to the coordinates of the location where the player is currently at 
    gameDisplay.blit(carIMG, (board[player1.location].car_coordinates))
#Display the image and the current location of the image to the list that tracks where the car was previously. That way, when it goes through the loop again, this previous image of the car can be replaced in the list by the image of the car at the new location.
    pygame.display.update()
    player1character.append(carIMG)
#if the number is greater than 40, take the mod of that number to find the location of where the player is on the board
  if player1.location >= 40:
    player1.location = player1.location % 40
    player1.money= player1.money + 200
#Set the image, display the image, and add it to the list that tracks the car's location
    gameDisplay.blit(carIMG, (board[player1.location].car_coordinates))
    pygame.display.update()
    player1character.append(carIMG)
#Since the player passes go when it goes through all 40 spaces, they get 200 dollars
    print(f"{player1.name} now has {player1.money} because they got 200 dollars for passing Go.")
#When the list that tracks the car's location is greater than 1, you keep the image of the car that was just added to the list, and get rid of the old image of it's location
  if len(player1character) > 1:
    player1character.pop(0)
  print(f"{player1.name} is at {board[player1.location].name}")
#When the player lands on chance, randomly pick between them getting or losing 50 dollars, and change their money total as a result.
  if board[player1.location].owner == 'Chance':
    chance1= [player1.money - 50]
    chance3= [player1.money + 50]
    chances= [chance1, chance3]
    randomchance = random.choice(chances)
    result = int(randomchance[0])
    player1.money = result
    print(f"{player1.name} now has {player1.money} dollars because they landed on a chance spot. ")
#If the player lands on Go To LOP, they go to LOP
  elif board[player1.location].name == 'GoToLOP':
    player1.location = board.index(LOP)
    print(f"Oh no, you are at LOP because you landed on Go To LOP!")
#If the player lands on a station and it's owner is still no one, they can buy the station at a certain price. If they do buy it, you change their money total based on how much it cost, and make them the owner
  elif board[player1.location].owner == 'station':
    answerS= input(f"Would you like to buy this property for {board[player1.location].purchase_price}? ").lower()
    if answerS == 'yes':
      player1.money= player1.money - board[player1.location].purchase_price
      print(f"{player1.name} now has {player1.money} dollars. ")
      board[player1.location].owner = player1.name
      print(f"The owner of {board[player1.location].name} is {board[player1.location].owner}")
#You add 1 to the player's station count, because if they get more stations, the other player has to pay more when they land on one of their stations, so we need to keep track of how many stations each player owns
      player1.station= player1.station + 1
      board[player1.location].stationcount1= board[player1.location].stationcount1 +1
#If the player lands on a station the other player owns and they own 1 station, you pay them the rent price for owning 1 station ($25), and they get $25
  elif board[player1.location].owner == player2.name and player2.station == 1 and board[player1.location].stationcount2 == 1:
    player1.money= player1.money - 25
    player2.money= player2.money + 25
    print(f"{player1.name} has to pay 25 dollars and now has {player1.money} dollars because they landed on a station owned by player 2.")
    print(f"{player2.name} now has {player2.money} dollars after collecting it from Player 1.")
#if the player lands on a station the other player owns and they own 2 stations, you pay them the rent price for owning 2 stations ($50), and they get $50
  elif board[player1.location].owner == player2.name and player2.station == 2 and board[player1.location].stationcount2 == 1:
    player1.money= player1.money - 50
    player2.money= player2.money + 50
    print(f"{player1.name} has to pay 50 dollars and now has {player1.money} dollars because they landed on a station owned by player 2 (who owns two stations).")
    print(f"{player2.name} now has {player2.money} dollars after collecting it from Player 1.")
#if the player lands on a station the other player owns and they own 3 stations, you pay them the rent price for owning 3 stations ($75), and they get $75
  elif board[player1.location].owner == player2.name and player2.station == 3 and board[player1.location].stationcount2 == 1:
    player1.money= player1.money - 75
    player2.money= player2.money + 75
    print(f"{player1.name} has to pay 75 dollars and now has {player1.money} dollars because they landed on a station owned by player 2 (who owns three stations).")
    print(f"{player2.name} now has {player2.money} dollars after collecting it from Player 1.")
 #if the player lands on a station the other player owns and they own 4 stations, you pay them the rent price for owning 4 stations ($100), and they get $100
  elif board[player1.location].owner == player2.name and player2.station == 4 and board[player1.location].stationcount2 == 1:
    player1.money= player1.money - 100
    player2.money= player2.money + 100
    print(f"{player1.name} has to pay 100 dollars and now has {player1.money} dollars because they landed on a station owned by player 2 (who owns four stations).")
    print(f"{player2.name} now has {player2.money} dollars after collecting it from Player 1.")
#If the player lands on tax, subtract 50 dollars from their total
  elif board[player1.location].owner == 'Tax':
    player1.money= player1.money - 50
    print(f"{player1.name} has to pay 50 dollars and now has {player1.money} dollars.")
#If the player lands on an unowned property, ask them if they want to buy it. If they say yes, you subtract the price to buy it from them, and make them the owner of the property
  elif board[player1.location].owner == 'none':
    answer1= input(f"Would you like to buy this property for {board[player1.location].purchase_price}? ")
    if answer1 == 'yes':
      player1.money= player1.money - board[player1.location].purchase_price
      print(f"{player1.name} now has {player1.money} dollars. ")
      board[player1.location].owner = player1.name
      print(f"The owner of {board[player1.location].name} is {board[player1.location].owner}")
#Add the location of the space the player owns to the list that tracks if they own all the spaces of a certain color, to see if they can buy houses or hotels later
      color1.append(board[player1.location].color)
#If the player lands on a the other player's space and they have a hotel there, the player pays the hotel price to the other player
  elif board[player1.location].hotel_owner == player2.name:
    player1.money= player1.money - board[player1.location].hotel_price
    player2.money = player2.money + board[player1.location].hotel_price
    print(f"{player1.name} now has {player1.money} dollars because they landed on Player Two's Property that has a hotel on it. ")
    print(f"{player2.name} now has {player2.money} dollars after collecting it from Player 1.")
#If the player lands on a the other player's space and they have 1 house there, the player pays the price of that space when it has 1 house to the other player
  elif board[player1.location].house_owner == player2.name and board[player1.location].house_2count == 1:
    player1.money= player1.money - board[player1.location].house_1price
    player2.money = player2.money + board[player1.location].house1_price
    print(f"{player1.name} now has {player1.money} dollars because they landed on Player Two's Property that has a house on it. ")
    print(f"{player2.name} now has {player2.money} dollars after collecting it from Player 1.")
#If the player lands on a the other player's space and they have 2 houses there, the player pays the price of that space when it has 2 houses to the other player
  elif board[player1.location].house_owner == player2.name and board[player1.location].house_2count == 2:
    player1.money= player1.money - board[player1.location].house_2price
    player2.money = player2.money + board[player1.location].house2_price
    print(f"{player1.name} now has {player1.money} dollars because they landed on Player Two's Property that has two houses on it. ")
    print(f"{player2.name} now has {player2.money} dollars after collecting it from Player 1.")
#If the player lands on a the other player's space and they have 3 houses there, the player pays the price of that space when it has 3 houses to the other player
  elif board[player1.location].house_owner == player2.name and board[player1.location].house_2count == 3:
    player1.money= player1.money - board[player1.location].house3_price
    player2.money = player2.money + board[player1.location].house3_price
    print(f"{player1.name} now has {player1.money} dollars because they landed on Player Two's Property that has three houses on it. ")
    print(f"{player2.name} now has {player2.money} dollars after collecting it from Player 1.")
#If the player lands on a the other player's space and they have 4 houses there, the player pays the price of that space when it has 4 houses to the other player
  elif board[player1.location].house_owner == player2.name and board[player1.location].house_2count == 4:
    player1.money= player1.money - board[player1.location].house4_price
    player2.money = player2.money + board[player1.location].house4_price
    print(f"{player1.name} now has {player1.money} dollars because they landed on Player Two's Property that has four houses on it. ")
    print(f"{player2.name} now has {player2.money} dollars after collecting it from Player 1.")
#If the player lands on a the other player's space and they have 0 houses there, the player pays the rent price of that space to the other player
  elif board[player1.location].owner == player2.name:
    player1.money= player1.money - board[player1.location].rent_price
    player2.money = player2.money + board[player1.location].rent_price
    print(f"{player1.name} now has {player1.money} dollars because they landed on Player Two's Property at {board[player1.location].name}. ")
    print(f"{player2.name} now has {player2.money} dollars after collecting it from Player 1.")
#If the player lands on their property, nothing happens
  elif board[player1.location].owner == player1.name:
    print("This location is your property, so you don't have to pay money!")
#If the player has all the purple spaces and they are on one of those spaces, they can buy a house for that space. If they say yes, you subtract the price to buy a house, and add a house to that location
  if color1.count('purple')== 2 and board[player1.location].color=='purple':
    P_house_answer= input(f'Congrats, you have all of the purple properties, would you like to buy a house for {board[player1.location].house_price}? Type yes if you want to!').lower()
    if P_house_answer == 'yes':
      player1.money= player1.money- board[player1.location].house_price
      print(f'You now have {player1.money} dollars and a house at {board[player1.location].name}.')
      board[player1.location].house_owner = player1.name
      board[player1.location].house_count +=1
#If the player has all the light blue spaces and they are on one of those spaces, they can buy a house for that space. If they say yes, you subtract the price to buy a house, and add a house to that location
  elif color1.count('light blue') == 3 and board[player1.location].color == 'light blue':
    LB_house_answer= input(f'Congrats, you have all of the light blue properties, would you like to buy a house for {board[player1.location].house_price}? Type yes if you want to!').lower()
    if LB_house_answer == 'yes' and board[player1.location].color == 'light blue':
      player1.money= player1.money- board[player1.location].house_price
      print(f'You now have {player1.money} dollars and a house at {board[player1.location].name}.')
      board[player1.location].house_owner = player1.name
      board[player1.location].house_count +=1
#If the player has all the pink spaces and they are on one of those spaces, they can buy a house for that space. If they say yes, you subtract the price to buy a house, and add a house to that location
  elif color1.count('pink') == 3 and board[player1.location].color == 'pink':
    P_house_answer= input(f'Congrats, you have all of the pink properties, would you like to buy a house for {board[player1.location].house_price}? Type yes if you want to!').lower()
    if P_house_answer == 'yes':
      player1.money= player1.money- board[player1.location].house_price
      print(f'You now have {player1.money} dollars and a house at {board[player1.location].name}.')
      board[player1.location].house_owner = player1.name
      board[player1.location].house_count +=1
#If the player has all the orange spaces and they are on one of those spaces, they can buy a house for that space. If they say yes, you subtract the price to buy a house, and add a house to that location
  elif color1.count('orange') == 3 and board[player1.location].color == 'orange':
    O_house_answer= input(f'Congrats, you have all of the pink properties, would you like to buy a house for {board[player1.location].house_price}? Type yes if you want to!').lower()
    if O_house_answer == 'yes':
      player1.money= player1.money- board[player1.location].house_price
      print(f'You now have {player1.money} dollars and a house at {board[player1.location].name}.')
      board[player1.location].house_owner = player1.name
      board[player1.location].house_count +=1
#If the player has all the red spaces and they are on one of those spaces, they can buy a house for that space. If they say yes, you subtract the price to buy a house, and add a house to that location
  elif color1.count('red') == 3 and board[player1.location].color == 'red':
    R_house_answer= input(f'Congrats, you have all of the pink properties, would you like to buy a house for {board[player1.location].house_price}? Type yes if you want to!').lower()
    if R_house_answer == 'yes':
      player1.money= player1.money- board[player1.location].house_price
      print(f'You now have {player1.money} dollars and a house at {board[player1.location].name}.')
      board[player1.location].house_owner = player1.name
      board[player1.location].house_count +=1
#If the player has all the yellow spaces and they are on one of those spaces, they can buy a house for that space. If they say yes, you subtract the price to buy a house, and add a house to that location
  elif color1.count('yellow') == 3 and board[player1.location].color == 'yellow':
    Y_house_answer= input(f'Congrats, you have all of the pink properties, would you like to buy a house for {board[player1.location].house_price}? Type yes if you want to!').lower()
    if Y_house_answer == 'yes':
      player1.money= player1.money- board[player1.location].house_price
      print(f'You now have {player1.money} dollars and a house at {board[player1.location].name}.')
      board[player1.location].house_owner = player1.name
      board[player1.location].house_count +=1
#If the player has all the green spaces and they are on one of those spaces, they can buy a house for that space. If they say yes, you subtract the price to buy a house, and add a house to that location
  elif color1.count('green') == 3 and board[player1.location].color == 'green':
    G_house_answer= input(f'Congrats, you have all of the pink properties, would you like to buy a house for {board[player1.location].house_price}? Type yes if you want to!').lower()
    if G_house_answer == 'yes':
      player1.money= player1.money- board[player1.location].house_price
      print(f'You now have {player1.money} dollars and a house at {board[player1.location].name}.')
      board[player1.location].house_owner = player1.name
      board[player1.location].house_count +=1
#If the player has all the dark blue spaces and they are on one of those spaces, they can buy a house for that space. If they say yes, you subtract the price to buy a house, and add a house to that location
  elif color1.count('dark blue') == 2 and board[player1.location].color == 'dark blue':
    DB_house_answer= input(f'Congrats, you have all of the dark blue properties, would you like to buy a house for {board[player1.location].house_price}? Type yes if you want to!').lower()
    if DB_house_answer == 'yes':
      player1.money= player1.money- board[player1.location].house_price
      print(f'You now have {player1.money} dollars and a house at {board[player1.location].name}.')
      board[player1.location].house_owner = player1.name
      board[player1.location].house_count +=1
#If the player lands on a space of a place they already have 4 houses on, they can buy a hotel. If they say yes, subtract the hotel price and add a hotel to their location
  elif board[player1.location].house_count == 4:
    hotel_answer= input("You have four houses at this location, would you like to buy a hotel here?").lower()
    if hotel_answer == 'yes':
      board[player1.location].house_count +=1
      player1.money= player1.money- board[player1.location].house_price
      board[player1.location].hotel_owner == player1.name
      print(f"Congrats, you now own a hotel at {board[player1.location]} and you have {player1.money} dollars.")

#Pick a random integer between 2 and 12 for the player to move
  dice_answer2= input(f"{player2.name}, are you ready to roll the dice? Click enter to roll.")
#Move the player to that location
  move2 = int(random.randint(min,max))
  print(f"{player2.name} rolled a {move2}")
  player2.location = player2.location + move2

  if player2.location < 40:
#Set the image of the hat to the coordinates of the location where the player is currently at 
    gameDisplay.blit(hatIMG, (board[player2.location].hat_coordinates))
#Display the image and the current location of the image to the list that tracks where the car was previously. That way, when it goes through the loop again, this previous image of the car can be replaced in the list by the image of the car at the new location.
    pygame.display.update()
    player2character.append(hatIMG)
#If the number is greater than 40, take the mod of that number to find the location of where the player is on the board
  if player2.location >= 40:
    player2.location = player2.location % 40
    player2.money = player2.money + 200
#Set the image, display the image, and add it to the list that tracks the car's location
    gameDisplay.blit(hatIMG, (board[player2.location].hat_coordinates))
    pygame.display.update()
    player2character.append(hatIMG)
#Since the player passes go when it goes through all 40 spaces, they get 200 dollars
    print(f"{player2.name} now has {player2.money} because they got 200 dollars for passing Go.")
#When the list that tracks the car's location is greater than 1, you keep the image of the car that was just added to the list, and get rid of the old image of it's location
  if len(player2character) > 1:
    player2character.pop(0)
  print(f"{player2.name} is at {board[player2.location].name}")
#When the player lands on chance, randomly pick between them getting or losing 50 dollars, and change their money total as a result.
  if board[player2.location].owner == 'Chance':
    chance1= [player1.money - 50]
    chance2= [player2.money - 50]
    chance3= [player1.money + 50]
    chance4= [player2.money + 50]
    chances2= [chance2, chance4]
    randomchance2 = random.choice(chances2)
    result2 = int(randomchance2[0])
    player2.money = result2
    print(f"{player2.name} now has {player2.money} dollars because they landed on a chance spot. ")
#If the player lands on Go To LOP, they go to LOP
  elif board[player2.location].owner == 'GoToLOP':
    player2.location = board.index(LOP)
    print(f"Oh no, you are at {board[player2.location].name} because you landed on Go To LOP!")
#If the player lands on a station and it's owner is still no one, they can buy the station at a certain price. If they do buy it, you change their money total based on how much it cost, and make them the owner 
  elif board[player2.location].owner == 'station':
    answerS2= input(f"Would you like to buy this property for {board[player2.location].purchase_price}? ").lower()
    if answerS2 == 'yes':
      player2.money= player2.money - board[player2.location].purchase_price
      print(f"{player2.name} now has {player2.money} dollars. ")
      board[player2.location].owner = player2.name
      print(f"The owner of {board[player2.location].name} is {board[player2.location].owner}")
#You add 1 to the player's station count, because if they get more stations, the other player has to pay more when they land on one of their stations, so we need to keep track of how many stations each player owns
      player2.station= player2.station + 1  
      board[player2.location].stationcount2= board[player2.location].stationcount2 +1
#If the player lands on a station the other player owns and they own 1 station, you pay them the rent price for owning 1 station ($25), and they get $25
  elif board[player2.location].owner == player1.name and player1.station == 1 and board[player2.location].stationcount1 == 1:
    player2.money= player2.money - 25
    player1.money= player1.money + 25
    print(f"{player2.name} has to pay 25 dollars and now has {player2.money} dollars because they landed on a station owned by player 1.")
    print(f"{player1.name} now has {player1.money} dollars after collecting it from Player 2.")
#if the player lands on a station the other player owns and they own 2 stations, you pay them the rent price for owning 2 stations ($50), and they get $50
  elif board[player2.location].owner == player1.name and player1.station == 2 and board[player2.location].stationcount1 == 1:
    player2.money= player2.money - 50
    player1.money= player1.money + 50
    print(f"{player2.name} has to pay 50 dollars and now has {player2.money} dollars because they landed on a station owned by player 1 (who owns two stations).")
    print(f"{player1.name} now has {player1.money} dollars after collecting it from Player 2.")
#if the player lands on a station the other player owns and they own 3 stations, you pay them the rent price for owning 3 stations ($75), and they get $75
  elif board[player2.location].owner == player1.name and player1.station == 3 and board[player2.location].stationcount1 == 1:
    player2.money= player2.money - 75
    player1.money= player1.money + 75
    print(f"{player2.name} has to pay 75 dollars and now has {player2.money} dollars because they landed on a station owned by player 1 (who owns three stations).")
    print(f"{player1.name} now has {player1.money} dollars after collecting it from Player 2.")
 #if the player lands on a station the other player owns and they own 4 stations, you pay them the rent price for owning 4 stations ($100), and they get $100
  elif board[player2.location].owner == player1.name and player1.station == 4 and board[player1.location].stationcount1 == 1:
    player2.money= player2.money - 100
    player1.money= player1.money + 100
    print(f"{player2.name} has to pay 100 dollars and now has {player2.money} dollars because they landed on a station owned by player 2 (who owns four stations).")
    print(f"{player1.name} now has {player1.money} dollars after collecting it from Player 2.")
#If the player lands on tax, subtract 50 dollars from their total
  elif board[player2.location].owner == 'Tax':
    player2.money= player2.money - 50
    print(f"{player2.name} has to pay 50 dollars and now has {player2.money} dollars.")
#If the player lands on an unowned property, ask them if they want to buy it. If they say yes, you subtract the price to buy it from them, and make them the owner of the property
  elif board[player2.location].owner == 'none':
    answer2= input(f"Would {player2.name} like to buy this property for {board[player2.location].purchase_price}? ")
    if answer2 == 'yes':
      player2.money= player2.money - board[player2.location].purchase_price
      print(f"{player2.name} now has {player2.money} dollars. ")
      board[player2.location].owner = player2.name
      print(f"The owner of {board[player2.location].name} is {board[player2.location].owner}")
#Add the location of the space the player owns to the list that tracks if they own all the spaces of a certain color, to see if they can buy houses or hotels later
      color2.append(board[player2.location].color)
#If the player lands on a the other player's space and they have a hotel there, the player pays the hotel price to the other player  
  elif board[player2.location].hotel_owner == player1.name:
    player2.money= player2.money - board[player2.location].hotel_price
    player1.money= player1.money + board[player2.location].hotel_price
    print(f"{player2.name} now has {player2.money} dollars because they landed on Player One's Property that has a hotel on it. ")
    print(f"{player1.name} now has {player1.money} dollars after collecting it from Player 2.")
#If the player lands on a the other player's space and they have 1 house there, the player pays the price of that space when it has 1 house to the other player
  elif board[player2.location].house_owner == player1.name and board[player2.location].house_count == 1:
    player2.money= player2.money- board[player2.location].house_1price
    player1.money= player1.money + board[player2.location].house_1price
    print(f"You landed on {player1.name}'s propery with one house, so {player2.name} now has {player2.money} dollars. ")
    print(f"{player1.name} now has {player1.money} dollars after collecting it from Player 2.")
#If the player lands on a the other player's space and they have 2 houses there, the player pays the price of that space when it has 2 houses to the other player  
  elif board[player2.location].house_owner == player1.name and board[player2.location].house_count == 2:
    player2.money= player2.money- board[player2.location].house_2price
    player1.money= player1.money + board[player2.location].house_2price
    print(f"You landed on {player1.name}'s propery with two houses, so {player2.name} now has {player2.money} dollars. ")
    print(f"{player1.name} now has {player1.money} dollars after collecting it from Player 2.")
#If the player lands on a the other player's space and they have 3 houses there, the player pays the price of that space when it has 3 houses to the other player
  elif board[player2.location].house_owner == player1.name and board[player2.location].house_count == 3:
    player2.money= player2.money- board[player2.location].house3_price
    player1.money= player1.money + board[player2.location].house_3price
    print(f"You landed on {player1.name}'s propery with three houses, so {player2.name} now has {player2.money} dollars. ")
    print(f"{player1.name} now has {player1.money} dollars after collecting it from Player 2.")
#If the player lands on a the other player's space and they have 4 houses there, the player pays the price of that space when it has 4 houses to the other player 
  elif board[player2.location].house_owner == player1.name and board[player2.location].house_count == 4:
    player2.money= player2.money- board[player2.location].house4_price
    player1.money= player1.money + board[player2.location].house_4price
    print(f"You landed on {player1.name}'s propery with four houses, so {player2.name} now has {player2.money} dollars. ")
    print(f"{player1.name} now has {player1.money} dollars after collecting it from Player 2.")
#If the player lands on a the other player's space and they have 0 houses there, the player pays the rent price of that space to the other player
  elif board[player2.location].owner == player1.name:
    player2.money= player2.money - board[player2.location].rent_price
    player1.money= player1.money + board[player2.location].rent_price
    print(f"You landed on {player1.name}'s propery at {board[player2.location].name}, so {player2.name} now has {player2.money} dollars. ")
    print(f"{player1.name} now has {player1.money} dollars after collecting it from Player 2.")
#If the player lands on their property, nothing happens
  elif board[player2.location].owner == player2.name:
    print("This location is your property, so you don't have to pay money!")
#If the player has all the purple spaces and they are on one of those spaces, they can buy a house for that space. If they say yes, you subtract the price to buy a house, and add a house to that location
  elif color2.count('purple')== 2 and board[player2.location].color=='purple':
    P2_house_answer= input(f'Congrats, you have all of the purple properties, would you like to buy a house for {board[player2.location].house_price}? Type yes if you want to!').lower()
    if P2_house_answer == 'yes':
      player2.money= player2.money- board[player2.location].house_price
      print(f'You now have {player2.money} dollars and a house at {board[player2.location].name}.')
      board[player2.location].house_owner = player2.name
      board[player2.location].house_2count +=1
#If the player has all the light blue spaces and they are on one of those spaces, they can buy a house for that space. If they say yes, you subtract the price to buy a house, and add a house to that location
  elif color2.count('light blue') == 3 and board[player2.location].color == 'light blue':
    LB2_house_answer= input(f'Congrats, you have all of the light blue properties, would you like to buy a house for {board[player2.location].house_price}? Type yes if you want to!').lower()
    if LB2_house_answer == 'yes' and board[player2.location].color == 'light blue':
      player2.money= player2.money- board[player2.location].house_price
      print(f'You now have {player2.money} dollars and a house at {board[player2.location].name}.')
      board[player2.location].house_owner = player2.name
      board[player2.location].house_2count +=1
#If the player has all the pink spaces and they are on one of those spaces, they can buy a house for that space. If they say yes, you subtract the price to buy a house, and add a house to that location
  elif color2.count('pink') == 3 and board[player2.location].color == 'pink':
    P2_house_answer= input(f'Congrats, you have all of the pink properties, would you like to buy a house for {board[player2.location].house_price}? Type yes if you want to!').lower()
    if P2_house_answer == 'yes' :
      player2.money= player2.money- board[player2.location].house_price
      print(f'You now have {player2.money} dollars and a house at {board[player2.location].name}.')
      board[player2.location].house_owner = player2.name
      board[player2.location].house_2count +=1
#If the player has all the orange spaces and they are on one of those spaces, they can buy a house for that space. If they say yes, you subtract the price to buy a house, and add a house to that location
  elif color2.count('orange') == 3 and board[player2.location].color == 'orange':
    O2_house_answer= input(f'Congrats, you have all of the pink properties, would you like to buy a house for {board[player2.location].house_price}? Type yes if you want to!').lower()
    if O2_house_answer == 'yes':
      player2.money= player2.money- board[player2.location].house_price
      print(f'You now have {player2.money} dollars and a house at {board[player2.location].name}.')
      board[player2.location].house_owner = player2.name
      board[player2.location].house_2count +=1
#If the player has all the red spaces and they are on one of those spaces, they can buy a house for that space. If they say yes, you subtract the price to buy a house, and add a house to that location
  elif color2.count('red') == 3 and board[player2.location].color == 'red':
    R2_house_answer= input(f'Congrats, you have all of the pink properties, would you like to buy a house for {board[player2.location].house_price}? Type yes if you want to!').lower()
    if R2_house_answer == 'yes':
      player2.money= player2.money- board[player2.location].house_price
      print(f'You now have {player2.money} dollars and a house at {board[player2.location].name}.')
      board[player2.location].house_owner = player2.name
      board[player2.location].house_2count +=1
#If the player has all the yellow spaces and they are on one of those spaces, they can buy a house for that space. If they say yes, you subtract the price to buy a house, and add a house to that location
  elif color2.count('yellow') == 3 and board[player2.location].color == 'yellow':
    Y2_house_answer= input(f'Congrats, you have all of the pink properties, would you like to buy a house for {board[player2.location].house_price}? Type yes if you want to!').lower()
    if Y2_house_answer == 'yes':
      player2.money= player2.money- board[player2.location].house_price
      print(f'You now have {player2.money} dollars and a house at {board[player2.location].name}.')
      board[player2.location].house_owner = player2.name
      board[player2.location].house_2count +=1
#If the player has all the green spaces and they are on one of those spaces, they can buy a house for that space. If they say yes, you subtract the price to buy a house, and add a house to that location
  elif color2.count('green') == 3 and board[player2.location].color == 'green':
    G2_house_answer= input(f'Congrats, you have all of the pink properties, would you like to buy a house for {board[player2.location].house_price}? Type yes if you want to!').lower()
    if G2_house_answer == 'yes':
      player2.money= player2.money- board[player2.location].house_price
      print(f'You now have {player2.money} dollars and a house at {board[player2.location].name}.')
      board[player2.location].house_owner = player2.name
      board[player2.location].house_2count +=1
#If the player has all the dark blue spaces and they are on one of those spaces, they can buy a house for that space. If they say yes, you subtract the price to buy a house, and add a house to that location
  elif color2.count('dark blue') == 2 and board[player2.location].color == 'dark blue':
    DB2_house_answer= input(f'Congrats, you have all of the pink properties, would you like to buy a house for {board[player2.location].house_price}? Type yes if you want to!').lower()
    if DB2_house_answer == 'yes':
      player2.money= player2.money- board[player2.location].house_price
      print(f'You now have {player2.money} dollars and a house at {board[player2.location].name}.')
      board[player2.location].house_owner = player2.name
      board[player2.location].house_2count +=1
#If the player lands on a space of a place they already have 4 houses on, they can buy a hotel. If they say yes, subtract the hotel price and add a hotel to their location
  elif board[player2.location].house_2count == 4:
    hotel2_answer= input("You have four houses at this location, would you like to buy a hotel here?").lower()
    if hotel2_answer == 'yes':
      board[player2.location].house_count +=1
      player2.money= player2.money- board[player2.location].house_price
      board[player2.location].hotel_owner == player2.name
      print(f"Congrats, you now own a hotel at {board[player2.location].name} and you have {player2.money} dollars.")
#Make all the images actually appear
  pygame.display.flip()
#If Player 1 still has money, they win
if player1.money > 0:
  print(f"{player2name} ran out of money, so {player1name} won! Congratulations on winning MAGNET MONOPOLY! ")
#If Player 2 still has money, they win
elif player2.money > 0 :
  print(f"{player1name} ran out of money, so {player2name} won! Congratulations on winning MAGNET MONOPOLY! ")