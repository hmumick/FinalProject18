import pygame

pygame.init()

display_width= 880
display_height= 600

black= (0,0,0)
white= (255,255,255)
red= (255,0,0)
yellow= (255,209,0)
green= (0,255,0)
darkblue= (0,0,255)
lightblue= (0,255,255)
purple= (189,0,255)
lightgreen= (0,255,158)
orange= (255,162,0)
brown= (129,90,6)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Magnet Monopoly')

BackgroundIMG = pygame.image.load("FinalProject18-master\monopolyboard.png").convert()
gameDisplay.blit(BackgroundIMG, [0,0])

hatIMG = pygame.image.load("FinalProject18-master\hat.png")
carIMG = pygame.image.load("FinalProject18-master\car.png")

Start = (750, 510)
gameDisplay.blit(hatIMG, (Start))
gameDisplay.blit(carIMG, (Start))

PintoCar = (650, 510)
#gameDisplay.blit(carIMG, (PintoCar))

Chance1Car = (580, 510)
#gameDisplay.blit(carIMG, (Chance1Car))

ArnoldCar = (510, 510)
#gameDisplay.blit(carIMG, (ArnoldCar))

Tax1Car = (440, 510)
#gameDisplay.blit(carIMG, (Tax1Car))

MakerStationCar = (370, 510)
#gameDisplay.blit(carIMG, (MakerStationCar))

RaiteCar = (300, 510)
#gameDisplay.blit(carIMG, (RaiteCar))

Chance2Car = (230, 510)
#gameDisplay.blit(carIMG, (Chance2Car))

GuptaCar = (160, 510)
#gameDisplay.blit(carIMG, (GuptaCar))

WickCar = (90, 510)
#gameDisplay.blit(carIMG, (WickCar))

LOPCar = (0, 510)
#gameDisplay.blit(carIMG, (LOPCar))

TenanbaumCar = (0, 440)
#gameDisplay.blit(carIMG, (TenanbaumCar))

Chance3Car = (0, 380)
#gameDisplay.blit(carIMG, (Chance3Car))

#Side 2 = [TenebaumCar, Chance3Car, NowakoskiCar, McMenaminCar, GymStationCar, MansfieldCar]
for

clock= pygame.time.Clock
crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)
    
    pygame.display.update()
    #clock.tick(60)
pygame.quit()

