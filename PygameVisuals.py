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

BackgroundIMG = pygame.image.load("monopolyboard.png")
gameDisplay.blit(BackgroundIMG, [0,0])

hatIMG = pygame.image.load("hat.png")
carIMG = pygame.image.load("car.png")

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

Chance3Car = (0, 390)
#gameDisplay.blit(carIMG, (Chance3Car))

NowakoskiCar = (0, 340)
#gameDisplay.blit(carIMG, (NowakoskiCar))

McMenaminCar = (0, 290)
#gameDisplay.blit(carIMG, (McMenaminCar))

GymCar = (0, 240)
#gameDisplay.blit(carIMG, (GymCar))

MansfieldCar = (0,190)
#gameDisplay.blit(carIMG, (MansfieldCar))

Chance4Car = (0,140)
#gameDisplay.blit(carIMG, (Chance4Car))

ValverdeCar = (0,90)
#gameDisplay.blit(carIMG, (ValverdeCar))

MejiaCar = (0,40)
#gameDisplay.blit(carIMG, (MejiaCar))

FreeParkingCar = (0,0)
#gameDisplay.blit(carIMG, (FreeParkingCar))

SansiCar = (90,0)
#gameDisplay.blit(carIMG, (SansiCar))

ValleyCar = (160,0)
#gameDisplay.blit(carIMG, (ValleyCar))

Chance5Car = (230, 0)
#gameDisplay.blit(carIMG, (Chance5Car))

DraeselCar = (300,0)
#gameDisplay.blit(carIMG, (DraeselCar))

LabCar = (370,0)
#gameDisplay.blit(carIMG, (LabCar))

WeisserCar = (440, 0)
#gameDisplay.blit(carIMG, (WeisserCar))

FangCar = (510,0)
#gameDisplay.blit(carIMG, (FangCar))

Chance6Car = (580,0)
#gameDisplay.blit(carIMG, (Chance6Car))

GersteinCar = (650,0)
#gameDisplay.blit(carIMG, (GersteinCar))

GoToLopCar = (750, 0)
#gameDisplay.blit(carIMG, (GoToLOPCar))

OConnorCar = (750, 40)
#gameDisplay.blit(carIMG, (OConnorCar))

LiuCar = (750, 90)
#gameDisplay.blit(carIMG, (LiuCar))

Chance7Car = (750, 140)
#gameDisplay.blit(carIMG, (Chance7Car))

MoskowitzCar = (750, 190)
#gameDisplay.blit(carIMG, (MoskowitzCar))

AuditStationCar = (750, 240)
#gameDisplay.blit(carIMG,(AuditStationCar))

Chance8Car = (750, 290)
#gameDisplay.blit(carIMG, (Chance8Car))

GuidanceCar = (750, 340)
#gameDisplay.blit(carIMG, (GuidanceCar))

Tax2Car = (750, 390)
#gameDisplay.blit(carIMG, (Tax2Car))

RafalowskiCar = (750, 440)
gameDisplay.blit(carIMG, (RafalowskiCar))




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

