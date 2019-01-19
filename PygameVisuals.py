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

Start = (750, 520)
gameDisplay.blit(hatIMG, (Start))
gameDisplay.blit(carIMG, (Start))

PintoCar = (650, 520)
#gameDisplay.blit(carIMG, (PintoCar))

Chance1Car = (580, 520)
#gameDisplay.blit(carIMG, (Chance1Car))

ArnoldCar = (510, 520)
#gameDisplay.blit(carIMG, (ArnoldCar))

Tax1Car = (440, 520)
#gameDisplay.blit(carIMG, (Tax1Car))

MakerStationCar = (370, 520)
#gameDisplay.blit(carIMG, (MakerStationCar))

RaiteCar = (300, 520)
#gameDisplay.blit(carIMG, (RaiteCar))

Chance2Car = (230, 520)
#gameDisplay.blit(carIMG, (Chance2Car))

GuptaCar = (160, 520)
#gameDisplay.blit(carIMG, (GuptaCar))

WickCar = (90, 520)
#gameDisplay.blit(carIMG, (WickCar))

LOPCar = (0, 520)
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
#gameDisplay.blit(carIMG, (RafalowskiCar))

PintoHat = (670, 520)
#gameDisplay.blit(hatIMG, (PintoHat))

Chance1Hat = (600, 520)
#gameDisplay.blit(hatIMG, (Chance1Hat))

ArnoldHat = (530, 520)
#gameDisplay.blit(hatIMG, (ArnoldHat))

Tax1Hat = (460, 520)
#gameDisplay.blit(hatIMG, (Tax1Hat))

MakerStationHat = (390, 520)
#gameDisplay.blit(hatIMG, (MakerStationHat))

RaiteHat = (320, 520)
#gameDisplay.blit(hatIMG, (Chance1Hat))

Chance2Hat = (250, 520)
#gameDisplay.blit(hatIMG, (Chance2Hat))

GuptaHat = (180, 520)
#gameDisplay.blit(hatIMG, (GuptaHat))

WickHat = (110, 520)
#gameDisplay.blit(hatIMG, (WickHat))

LOPHat = (0, 520)
#gameDisplay.blit(hatIMG, (LOPHat))

TenanbaumHat = (0, 455)
gameDisplay.blit(hatIMG, (TenanbaumHat))

Chance3Hat = (0, 410)
#gameDisplay.blit(hatIMG, (Chance3Hat))

NowakoskiHat = (0, 365)
#gameDisplay.blit(hatIMG, (NowakoskiHat))

McMenaminHat = (0, 320)
#gameDisplay.blit(hatIMG, (McMenaminHat))

GymStationHat = (0,275)
#gameDisplay.blit(hatIMG, (GymStationHat))

MansfieldHat = (0, 225)
#gameDisplay.blit(hatIMG, (MansfieldHat))

Chance4Hat = (0, 180)
#gameDisplay.blit(hatIMG, (Chance4Hat))

ValverdeHat = (0,135)
#gameDisplay.blit(hatIMG, (ValverdeHat))

MejiaHat = (0, 90)
#gameDisplay.blit(hatIMG, (MejiaHat))

FreeParkingHat = (0, 0)
#gameDisplay.blit(hatIMG, (FreeParkingHat))

SansiHat = (110, 0)
#gameDisplay.blit(hatIMG, (SansiHat))

ValleyHat = (180, 0)
#gameDisplay.blit(hatIMG, (ValleyHat))

Chance5Hat = (250, 0)
#gameDisplay.blit(hatIMG, (Chance5Hat))

DraeselHat = (320, 0)
#gameDisplay.blit(hatIMG, (DraeselHat))

LabHat = (390, 0)
#gameDisplay.blit(hatIMG, (LabHat))

WeisserHat = (460, 0)
#gameDisplay.blit(hatIMG, (WeisserHat))

FangHat = (530, 0)
#gameDisplay.blit(hatIMG, (FangHat))

Chance6Hat = (600,0)
#gameDisplay.blit(hatIMG, (Chance6Hat))

GersteinHat = (670, 0)
#gameDisplay.blit(hatIMG, (GersteinHat))

GoToLOPHat = (750, 0)
#gameDisplay.blit(hatIMG, (GoToLOPHat))

OConnorHat = (750, 90)
#gameDisplay.blit(hatIMG, (OConnorHat))

LiuHat = (750, 135)
#gameDisplay.blit(hatIMG, (LiuHat))

Chance7Hat = (750, 180)
#gameDisplay.blit(hatIMG, (Chance7Hat))

MoskowitzHat = (750, 225)
#gameDisplay.blit(hatIMG, (MoskowitzHat))

AuditStationHat = (750, 275)
#gameDisplay.blit(hatIMG, (AuditStationHat))

Chance8Hat = (750, 320)
#gameDisplay.blit(hatIMG, (Chance8Hat))

GuidanceHat = (750, 365)
#gameDisplay.blit(hatIMG, (Chance3Hat))

Tax2Hat = (750, 410)
#gameDisplay.blit(hatIMG, (Tax2Hat))

RafalowskiHat = (750, 455)
#gameDisplay.blit(hatIMG, (RafalowskiHat))


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

