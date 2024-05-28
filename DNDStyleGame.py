#Imports
import random
import json
import math
import numpy as np
import cv2
import json.decoder
with open('CharacterSheet.json', 'r') as i:
          ChS = json.load(i)

# Title
def TitleScreen():
          print("********************| (o) |************************************************| (o) |********************    D&D    Online    ********************| (o) |************************************************| (o) |******************** ")
          input('')
          print("                                                                                                       ( Not Owned Nor Endoursed By Wizards of the Coast or Hasbro )")
          input('')
# Stats Conversions
"""
"1" Kingsmen Kurrancy = "100" Nobles Currancy
"1" Nobles Currancy = "50" Commonmen Currancy
"1" Commonmens Currancy = "150" Poormens Change
"""
# Money
global PoorMensChange
global CommonMensChange
global NoblesCurrancy
global KingsmenChange
PoorMensChange = 15
CommonMensChange = 5
NoblesCurrancy = 1
KingsmenChange = 0
# Descriptions
Non = False
def OCDescription():
          # Game
          Name = str(input("What is your Characters Name?"))
          Gender = str(input("What is your Characters Gender?"))
          Looks = str(input("What is your Characters Apperance?"))
          Attraction = str(input("[ --- What is your Characters sexaulity?"))
          Background = str(input("What is your Characters background?"))
          Personality = str(input("What is your Characters personality?"))          
          # Finished
          Flaws = str(input("what is your Characters Flaws?"))
          x = {
                    "Name": Name,
                    "Gender": Gender,
                    "Sexuality": Attraction,
                    "Apperance": Looks,
                    "Background": Background,
                    "Personality": Personality,
                    "Flaws": Flaws
          }
          y = json.dumps(x)
          with open("OCSheet.json", "a") as outfile:
                    outfile.write(y)
                    
          
# Equipment
Count = 0
def Equipment():
          Z = True
          while Z == True:
                    global Count
                    Count = Count + 1
                    B = str(input("Does your Item cause any damage or harm? ( Is it a weapon ) ( Y / N )"))
                    if B == "Y":
                              C = str(input("Whats its Name?"))
                              E = str(input("Whats its appearance?"))
                              F = str(input("Whats its background / Description"))
                              G = int(input("What is its Value? ( Poor Mens Change Only )"))
                              D = int(input("How much does it do? ( Max is 10 )"))
                              Equipment.x = {
                                        "DamageWeilder": B,
                                        "Name": C,
                                        "Apperance": E,
                                        "Description": F,
                                        "Damage": D,
                                        "Value": G
                              }
                              y = json.dumps(Equipment.x)
                              with open("Equipment.json", "a") as outfile:
                                        outfile.write(y)
                    else:
                              R = str(input("Whats its Name?"))
                              S = str(input("Whats its appearance?"))
                              T = str(input("Whats its background / Description"))
                              V = str(input("What is its value? ( Poor Mens Change Only )"))
                              Equipment.JsonPython = {
                                        "DamageWeilder": B,
                                        "Name": R,
                                        "Apperance": S,
                                        "Description": T,
                                        "Value": V
                              }
                              JsonExport = json.dumps(Equipment.JsonPython)
                              with open("Equipment.json", "a") as outfile:
                                        outfile.write(JsonExport)
                    Ask = str(input("Is that all? ( Y / N )"))
                    if Ask == "Y":
                              Z = False
def DonaldTrumpAttack():
          # This is a joke Code.  Also, its not mine.
          a = cv2.VideoCapture("TrumpBehindTheSlaughter.mp4")
          if (a.isOpened()==False):
                    print("error")
          song = AudioSegment.from_mp3("Song.mp3")
          print('playing sound using pydub')
          play(song)

          while(a.isOpened()):
                    ret, frame = a.read()
                    if ret == True:
                              cv2.imshow('Frame', frame)
                              if cv2.waitKey(25) & 0xFF == ord('q'):
                                        break
                                        
                    else:
                              break

          a.release()
          # UNNEEDED!
          cv2.destroyAllWindows()
                    
                    

# Variables Abl
Strength = 0
Intelligence = 0
Wisdom = 0
Charisma = 0
Constitution = 0
Dexterity = 0
# Race
def Race():
          global Strength
          global Intelligence
          global Wisdom
          global Charisma
          global Constitution
          global Dexterity
          # Specieis Picker
          while True:
                    print('                                                                                                                        | ******************** Race ******************** |')
                    print('                                                                                                                                               |0x0| : Goblin')
                    print('                                                                                                                                               |0x0| : Orc')
                    print('                                                                                                                                               |0x0| : Elf')
                    print('                                                                                                                                               |0x0| : Human')
                    print('                                                                                                                                               |0x0| : Centaur')
                    print('                                                                                                                                               |0x0| : Angel')
                    print('                                                                                                                                               |0x0| : Vampire')
                    print('                                                                                                                                               |0x0| : Demon')
                    print('                                                                                                                                               |0x0| : Giant')
          
                    Race = str(input('What Race Will you be? ( * for more information )'))

                    if Race == '*':
                              print('')
                              print('')
                              print('')
                              file = open('RaceTwoSV.txt', 'r')
                              New = file.read()
                              print(New)
                              print('')
                              print('')
                              print('')
                    #if Race == 'Custom':
                              #RunningOutOfNames = 
                    if Race == 'Donald Trump':
                              DonaldTrumpAttack()
                    if Race == 'Goblin':
                              print('')
                              # Strength #
                              
                              Strength = Strength + ChS['Characters'][0]['Strength']
                              
                              
                              # Charisma #
                              
                              Charisma = Charisma + ChS['Characters'][0]['Charisma']
                              
                              
                              # Intelligence #
                              
                              Intelligence = Intelligence + ChS['Characters'][0]['Intelligence']
                              
                              
                              # Wisdom #
                              
                              Wisdom = Wisdom + ChS['Characters'][0]['Wisdom']
                              
                              
                              # Constitution #
                              
                              Constitution = Constitution + ChS['Characters'][0]['Consitution']
                              
                              
                              # Dexterity #
                              
                              Dexterity = Dexterity + ChS['Characters'][0]['Dexterity']
                              

                              # Break #
                              
                              break
                    if Race == 'Orc':
                              print('')
                              # Strength #
                              
                              Strength = Strength + ChS['Characters'][1]['Strength']
                              
                              
                              # Charisma #
                              
                              Charisma = Charisma + ChS['Characters'][1]['Charisma']
                              
                              # Intelligence #
                              
                              Intelligence = Intelligence + ChS['Characters'][1]['Intelligence']
                              
                              # Wisdom #
                              
                              Wisdom = Wisdom + ChS['Characters'][1]['Wisdom']
                              
                              # Constitution #
                              
                              Constitution = Constitution + ChS['Characters'][1]['Consitution']
                              
                              # Dexterity #
                              
                              Dexterity = Dexterity + ChS['Characters'][1]['Dexterity']

                              # Break #
                              
                              break
                    if Race == 'Elf':
                              print('')
                              # Strength #
                              
                              Strength = Strength + ChS['Characters'][2]['Strength']
                              
                              # Charisma #
                              
                              Charisma = Charisma + ChS['Characters'][2]['Charisma']
                              
                              # Intelligence #
                              
                              Intelligence = Intelligence + ChS['Characters'][2]['Intelligence']
                              
                              # Wisdom #
                              
                              Wisdom = Wisdom + ChS['Characters'][2]['Wisdom']
                              
                              # Constitution #
                              
                              Constitution = Constitution + ChS['Characters'][2]['Consitution']
                              
                              # Dexterity #
                              
                              Dexterity = Dexterity + ChS['Characters'][2]['Dexterity']

                              # Break #
                              
                              break
                    if Race == 'Human':
                              print('')
                              # Strength #
                              
                              Strength = Strength + ChS['Characters'][3]['Strength']
                              
                              # Charisma #
                              
                              Charisma = Charisma + ChS['Characters'][3]['Charisma']
                              
                              # Intelligence #
                              
                              Intelligence = Intelligence + ChS['Characters'][3]['Intelligence']
                              
                              # Wisdom #
                              
                              Wisdom = Wisdom + ChS['Characters'][3]['Wisdom']
                              
                              # Constitution #
                              
                              Constitution = Constitution + ChS['Characters'][3]['Consitution']
                              
                              # Dexterity #
                              
                              Dexterity = Dexterity + ChS['Characters'][3]['Dexterity']

                              # Break #
                              
                              break
                    if Race == 'Centaur':
                              print('')
                              # Strength #
                              
                              Strength = Strength + ChS['Characters'][4]['Strength']
                              
                              # Charisma #
                              
                              Charisma = Charisma + ChS['Characters'][4]['Charisma']
                              
                              # Intelligence #
                              
                              Intelligence = Intelligence + ChS['Characters'][4]['Intelligence']
                              
                              # Wisdom #
                              
                              Wisdom = Wisdom + ChS['Characters'][4]['Wisdom']
                              
                              # Constitution #
                              
                              Constitution = Constitution + ChS['Characters'][4]['Consitution']
                              
                              # Dexterity #
                              
                              Dexterity = Dexterity + ChS['Characters'][4]['Dexterity']

                              # Break #
                              
                              break
                    if Race == 'Angel':
                              print(ChS['Characters'][5])
                              print('')
                              # Strength #
                              
                              Strength = Strength + ChS['Characters'][5]['Strength']
                              
                              # Charisma #
                              
                              Charisma = Charisma + ChS['Characters'][5]['Charisma']
                              
                              # Intelligence #
                              
                              Intelligence = Intelligence + ChS['Characters'][5]['Intelligence']
                              
                              # Wisdom #
                              
                              Wisdom = Wisdom + ChS['Characters'][5]['Wisdom']
                              
                              # Constitution #
                              
                              Constitution = Constitution + ChS['Characters'][5]['Consitution']
                              
                              # Dexterity #
                              
                              Dexterity = Dexterity + ChS['Characters'][5]['Dexterity']

                              # Break #
                              
                              break
                    if Race == 'Vampire':
                              print('')
                              # Strength #
                              
                              Strength = Strength + ChS['Characters'][6]['Strength']
                              
                              # Charisma #
                              
                              Charisma = Charisma + ChS['Characters'][6]['Charisma']
                              return Charisma
                              
                              # Intelligence #
                              
                              Intelligence = Intelligence + ChS['Characters'][6]['Intelligence']
                              return Intelligence
                              
                              # Wisdom #
                              
                              Wisdom = Wisdom + ChS['Characters'][6]['Wisdom']
                              
                              # Constitution #
                              
                              Constitution = Constitution + ChS['Characters'][6]['Consitution']
                              
                              # Dexterity #
                              
                              Dexterity = Dexterity + ChS['Characters'][6]['Dexterity']

                              # Break #
                              
                              break
                    if Race == 'Demon':
                              print('')
                              # Strength #
                              
                              Strength = Strength + ChS['Characters'][7]['Strength']
                              
                              # Charisma #
                              
                              Charisma = Charisma + ChS['Characters'][7]['Charisma']
                              
                              # Intelligence #
                              
                              Intelligence = Intelligence + ChS['Characters'][7]['Intelligence']
                              
                              # Wisdom #
                              
                              Wisdom = Wisdom + ChS['Characters'][7]['Wisdom']
                              
                              # Constitution #
                              
                              Constitution = Constitution + ChS['Characters'][7]['Consitution']
                              
                              # Dexterity #
                              
                              Dexterity = Dexterity + ChS['Characters'][7]['Dexterity']

                              # Break #
                              
                              break
                    if Race == 'Giant':
                              print(ChS['Characters'][8])
                              print('')
                              # Strength #
                              
                              Strength = Strength + ChS['Characters'][8]['Strength']
                              
                              # Charisma #
                              
                              Charisma = Charisma + ChS['Characters'][8]['Charisma']
                              
                              # Intelligence #
                              
                              Intelligence = Intelligence + ChS['Characters'][8]['Intelligence']
                              
                              # Wisdom #
                              
                              Wisdom = Wisdom + ChS['Characters'][8]['Wisdom']
                              
                              # Constitution #
                              
                              Constitution = Constitution + ChS['Characters'][8]['Consitution']
                              
                              # Dexterity #
                              
                              Dexterity = Dexterity + ChS['Characters'][8]['Dexterity']

                              # Break #
                              
                              break
                    #if Race == 'Custom': ( Maybe Later . . . )
                              
# Abilities
def AbilitiesOne():
          # Global Variables
          global Strength
          global Intelligence
          global Wisdom
          global Charisma
          global Constitution
          global Dexterity
          # Runs the infinite loop
          VTester = True
          # Abiltite Creator Loop
          while VTester == True:
                    AbName = str(input('Whats Your Characters ability?'))
                    AbDescription = str(input('What does your Ability do?'))
                    try:
                              AbDamage = int(input('How much damage does it do? ( Note : 20 is the maxium )'))
                              if AbDamage > 20:
                                        AbDamage = 20
                              print(AbDamage)
                              Energy = AbDamage * 2
                              Energy = Energy / 1.5
                    except ValueError:
                              print('Please use an integer')
                              AbDamage = int(input('How much damage does it do? ( Note : 20 is the maxium )'))
                              if AbDamage > 20:
                                        AbDamage = 20
                              print(AbDamage)
                              Energy = AbDamage * 2
                              Energy = Energy / 1.5
                    AbClass = str(input('Which of the following prompts is the base of your ability? ( Charisma, Strength, Dexterity, Wisdom, Intelligence, or Constitution )'))
                    if AbClass == 'Charisma':
                              AbDamage = AbDamage + Charisma
                              if AbDamage <= 1:
                                        Time = 1
                              elif 1 < AbDamage <= 5:
                                        Time = 2.5
                              elif 5 < AbDamage <= 10:
                                        Time = 5
                              elif 10 < AbDamage <= 15:
                                        Time = 7.5
                              elif 15 < AbDamage <= 20:
                                        Time = 10
                              else:
                                        a = AbDamage - 20
                                        a = a / 5
                                        Time = 10 + (2.5 * a)
                    if AbClass == 'Strength':
                              AbDamage = AbDamage + Strength
                              if AbDamage <= 1:
                                        Time = 1
                              elif 1 < AbDamage <= 5:
                                        Time = 2.5
                              elif 5 < AbDamage <= 10:
                                        Time = 5
                              elif 10 < AbDamage <= 15:
                                        Time = 7.5
                              elif 15 < AbDamage <= 20:
                                        Time = 10
                              else:
                                        a = AbDamage - 20
                                        a = a / 5
                                        Time = 10 + (2.5 * a)
                    if AbClass == 'Dexterity':
                              AbDamage = AbDamage + Dexterity
                              if AbDamage <= 1:
                                        Time = 1
                              elif 1 < AbDamage <= 5:
                                        Time = 2.5
                              elif 5 < AbDamage <= 10:
                                        Time = 5
                              elif 10 < AbDamage <= 15:
                                        Time = 7.5
                              elif 15 < AbDamage <= 20:
                                        Time = 10
                              else:
                                        a = AbDamage - 20
                                        a = a / 5
                                        Time = 10 + (2.5 * a)
                    if AbClass == 'Wisdom':
                              AbDamage = AbDamage + Wisdom
                              if AbDamage <= 1:
                                        Time = 1
                              elif 1 < AbDamage <= 5:
                                        Time = 2.5
                                        Score = 4
                              elif 5 < AbDamage <= 10:
                                        Time = 5
                                        Score = 3
                              elif 10 < AbDamage <= 15:
                                        Time = 7.5
                                        Score = 2
                              elif 15 < AbDamage <= 20:
                                        Time = 10
                                        Score = 1
                              else:
                                        a = AbDamage - 20
                                        a = a / 5
                                        Time = 10 + (2.5 * a)
                    if AbClass == 'Intelligence':
                              AbDamage = AbDamage + Intelligence
                              if AbDamage <= 1:
                                        Time = 1
                              elif 1 < AbDamage <= 5:
                                        Time = 2.5
                                        Score = 4
                              elif 5 < AbDamage <= 10:
                                        Time = 5
                                        Score = 3
                              elif 10 < AbDamage <= 15:
                                        Time = 7.5
                                        Score = 2
                              elif 15 < AbDamage <= 20:
                                        Time = 10
                                        Score = 1
                              else:
                                        a = AbDamage - 20
                                        a = a / 5
                                        Time = 10 + (2.5 * a)
                    if AbClass == 'Constitution':
                              AbDamage = AbDamage + Constitution
                              if AbDamage <= 1:
                                        Time = 1
                              elif 1 < AbDamage <= 5:
                                        Time = 2.5
                              elif 5 < AbDamage <= 10:
                                        Time = 5
                              elif 10 < AbDamage <= 15:
                                        Time = 7.5
                              elif 15 < AbDamage <= 20:
                                        Time = 10
                              else:
                                        a = AbDamage - 20
                                        a = a / 5
                                        Time = 10 + (2.5 * a)

# Scoring System.
                    print(f'Damage : {AbDamage}')
                    print(f'Time To Use / Duration : {Time} Seconds')
                    x = {
                              "Name": AbName,
                              "Descripition": AbDescription,
                              "Damage": AbDamage,
                              "TTU": Time,
                              "Class": AbClass
                    }
                    y = json.dumps(x)
                    with open("Abiltities.json", "a") as outfile:
                              outfile.write(y)
                    ContinueYesNo = str(input("Do you want to add another ability? ( Y / N )"))
                    if ContinueYesNo == "N":
                              VTester = False
                    
# Dice
def DiceTypes():
          AskDi = input('What type of Di do you want?')
          if AskDi == '4':
                    Dice4 = random.randint(1,4)
                    print(f'{AskDi} Sided Di : ', Dice4)
          if AskDi == '6':
                    Dice6 = random.randint(1,6)
                    print(f'{AskDi} Sided Di : ', Dice6)
          if AskDi == '8':
                    Dice8 = random.randint(1,8)
                    print(f'{AskDi} Sided Di : ', Dice8)
          if AskDi == '100':
                    Dice100 = random.randint(1,100)
                    print(f'{AskDi} Sided Di : ', Dice100)
          if AskDi == '10':
                    Dice10 = random.randint(1,10)
                    print(f'{AskDi} Sided Di : ', Dice10)
          if AskDi == '12':
                    Dice12 = random.randint(1,12)
                    print(f'{AskDi} Sided Di : ', Dice12)
          if AskDi == '20':
                    Dice20 = random.randint(1,20)
                    print(f'{AskDi} Sided Di : ', Dice20)
#Launch
input("Please Note : If you run into errors, please check OCSheet.json / Equipment.json / Abilities.json. If there is anything inside, wipe it.")
TitleScreen()
Race()
# Ability Definer
Ask = str(input('Does your character have abilities? ( Y / N )'))
if Ask == 'Y':
          AbilitiesOne()
print('')
AskEqu = str(input('Do you want to add items? ( Y / N )'))
if AskEqu == 'Y':
          Equipment()
print('')
OCDescription()

# After Market imports

with open('OCSheet.json', 'r') as g:
          OCS = json.load(g)
# Congrats
input("Congratulations!  You Have reached the end of Character Creation!")
# Launch Scores
NeetJson = json.dumps(OCS, indent=4)
print(NeetJson)
# JSON DECODER ( Not mine )
if AskEqu == "Y":
          with open("Equipment.json", "r") as r:
                    var = r.read()
                    var = var.replace('\n', '')
                    var = var.replace('}{', '},{')
                    var = "[" + var + "]"
                    json.loads(var)
          print(var)
if Ask == "Y":

          with open("Abiltities.json", "r") as r:
                    response = r.read()
                    response = response.replace('\n', '')
                    response = response.replace('}{', '},{')
                    response = "[" + response + "]"
                    json.loads(response)
          print(response)
# Problems.. All of them.. WHICH ARE NOW GONE BABY!


# Score Stats
print('  ')
print(f'Strength Score : {Strength}')
print(f'Charisma Score : {Charisma}')
print(f'Constitution Score : {Constitution}')
print(f'Wisdom Score : {Wisdom}')
print(f'Intelligence Score : {Intelligence}')
print(f'Dexterity Score : {Dexterity}')
print('  ')
print(f'Poor Mens Change : {PoorMensChange}')
print(f'Common Mens Change : {CommonMensChange}')
print(f'Noble Currancy : {NoblesCurrancy}')
print(f'Kingsmen Wealth : {KingsmenChange}')
# --------------------------------------------------------------- END OF CHARACTER CREATOR --------------------------------------------------------------- #

print("********************| (o) |************************************************| (o) |********************    Game   Maker    ********************| (o) |************************************************| (o) |******************** ")

# --------------------------------------------------------------- END OF CHARACTER CREATOR --------------------------------------------------------------- #
RunGamePweaseTwT = True
with open("Equipment.json", "r") as r:
          var = r.read()
          var = var.replace('\n', '')
          var = var.replace('}{', '},{')
          var = '{"Equip": [' + var + "]}"
          json.loads(var)
with open("Equipment.json", "w") as outfile:
          outfile.write(var)
with open("Abiltities.json", "r") as r:
          vr = r.read()
          vr = vr.replace('\n', '')
          vr = vr.replace('}{', '},{')
          vr = '{"Abs": [' + vr + "]}"
          json.loads(vr)
with open("Abiltities.json", "w") as outsfile:
          outsfile.write(vr)
def Player():
          RepeatLaunch = True
          while RepeatLaunch == True:
                    WDYD = input("What do you do?")
                    impa = "PC : "
                    qwertyuiop = str(impa)
                    with open("Roleplay.txt", "a") as ItsGonnaBeMe:
                              ItsGonnaBeMe.write(qwertyuiop)
                              ItsGonnaBeMe.write(WDYD)
                              ItsGonnaBeMe.write(" | ************ Spacer ************ | ")
                    Ask = str(input("Is that all? ( Y / N )"))
                    if Ask == "Y":
                              RepeatLaunch = False
          RepeatLaunch = True
Health = 50      
def DM():
          global Health
          global PoorMensChange
          global CommonMensChange
          global NoblesCurrancy
          global KingsmenChange
          ExTra = True
          Continue = True
          while ExTra == True:
                    RPorGM = str(input("[ Roleplay ] [ Game Mechanics ]"))
                    if RPorGM == "Roleplay":
                              with open("Roleplay.txt", "a") as ItsGonnaBeMe:
                                        DMing = input("")
                                        SEVENOFOUR = "DM : "
                                        EvilLikeMe = str(DMing)
                                        ItsGonnaBeMe.write(SEVENOFOUR)
                                        ItsGonnaBeMe.write(EvilLikeMe)
                                        ItsGonnaBeMe.write(" | ************ Spacer ************ | ")
                    elif RPorGM == "Game Mechanics":
                              UwU = str(input("[ Money ][ Health ][ Items ][ Abilities ][ OCSheet ][ Race ]"))
                              # FIX THE SYSTEMS! 
                              if UwU == "Money":
                                        while Continue == True:
                                                  A = str(input("What type of currancy do you want? [ PMC , CMC , NC , KK ]"))
                                                  print(f'PMC : {PoorMensChange}')
                                                  print(f'CMC : {CommonMensChange}')
                                                  print(f'NC : {NoblesCurrancy}')
                                                  print(f'KK : {KingsmenChange}')
                                                  B = int(input("how much do you want to add or subtract ( add '-' for negative )?"))                                        
                                                  if A == "PMC":
                                                            print('Works')
                                                            PoorMensChange = PoorMensChange + B
                                                            return PoorMensChange
                                                  elif A == "CMC":
                                                            CommonMensChange = CommonMensChange + B
                                                            return CommonMensChange
                                                  elif A == "NC":
                                                            NoblesCurrancy = NoblesCurrancy + B
                                                            return NoblesCurrancy
                                                  elif A == "KK":
                                                            KingsmenChange = KingsmenChange + B
                                                            return KingsmenChange
                                                  C = str(input("is that the end of it? ( Y / N )"))
                                                  if C == 'Y':
                                                            Continue = False
                              if UwU == "Items":
                                        OwO = True
                                        while OwO == True:
                                                  EquQuestion = str(input("Do you want to add another item? ( Y / N )"))
                                                  if EquQuestion == "Y":
                                                            # Reversal
                                                            with open("Equipment.json", "r") as r:
                                                                      qwerty = r.read()
                                                                      qwerty = qwerty.replace('},{', '}{')
                                                                      qwerty = qwerty.replace('{"Equip": [', '')
                                                                      qwerty = qwerty.replace(']}', '')
                                                                      json.loads(qwerty)
                                                                      with open("Equipment.json", "w") as outfile:
                                                                                outfile.write(qwerty)
                                                            # Reuse Equipment            
                                                            Equipment()
                                                            # Redo of reversal
                                                            with open("Equipment.json", "r") as r:
                                                                      var = r.read()
                                                                      var = var.replace('\n', '')
                                                                      var = var.replace('}{', '},{')
                                                                      var = '{"Equip": [' + var + "]}"
                                                                      json.loads(var)
                                                            with open("Equipment.json", "w") as outfile:
                                                                      outfile.write(var)
                                                  Del = str(input("Do you want to delete an item? ( Y / N )"))
                                                  # Why dont you work.. TwT..
                                                  if Del == "Y":
                                                            with open('Equipment.json', 'r') as ia:
                                                                      Eqp = json.load(ia)                                                                      
                                                            print(Eqp)
                                                            EveryLittleThingIDo = int(input("What is its number? ( Count the Names until you reach your desired item )"))
                                                            EveryLittleThingIDo = EveryLittleThingIDo - 1
                                                            H = Eqp['Equip'][EveryLittleThingIDo]
                                                            StringCheese = str(H)
                                                            with open("BannedItems.txt", "a") as bvc:
                                                                      bvc.write(StringCheese)
                                                                      bvc.write("| **** Spacer ****")
                              if UwU == "Abilities":
                                        asdf = True
                                        while asdf == True:
                                                  poiu = str(input("Do you want to add another Abilities? ( Y / N )"))
                                                  if poiu == "Y":
                                                            # Reversal
                                                            with open("Abiltities.json", "r") as r:
                                                                      qwert = r.read()
                                                                      qwert = qwert.replace('},{', '}{')
                                                                      qwert = qwert.replace('{"Abs": [', '')
                                                                      qwert = qwert.replace(']}', '')
                                                                      json.loads(qwert)
                                                            with open("Abiltities.json", "w") as lkjhgfdsa:
                                                                      lkjhgfdsa.write(qwert)
                                                            # Abs
                                                            AbilitiesOne()
                                                            # Redo of reversal
                                                            with open("Abiltities.json", "r") as r:
                                                                      vr = r.read()
                                                                      vr = vr.replace('\n', '')
                                                                      vr = vr.replace('}{', '},{')
                                                                      vr = '{"Abs": [' + vr + "]}"
                                                                      json.loads(vr)
                                                            with open("Abiltities.json", "w") as outsfile:
                                                                      outsfile.write(vr)
                                                  fgh = str(input("Do you want to Ban an Abilitie? ( Y / N )"))
                                                  # Why dont you work.. TwT..
                                                  if fgh == "Y":
                                                            with open('Abiltities.json', 'r') as isa:
                                                                      Eqap = json.load(isa)                                                                      
                                                            print(Eqap)
                                                            EveryLittleThingIDso = int(input("What is its number? ( Count the Names until you reach your desired item )"))
                                                            EveryLittleThingIDso = EveryLittleThingIDso - 1
                                                            High = Eqap["Abs"][EveryLittleThingIDso]
                                                            Stringgeese = str(High)
                                                            with open("BannedAbs.txt", "a") as bvlc:
                                                                      bvlc.write(Stringgeese)
                                                                      bvlc.write("| ****** Spacer ****** |")
                                                                      
                              if UwU == "OCSheet":
                                        with open("OCSheet.json", "r") as hjk:
                                                  OCCS = json.load(hjk)
                                        print(OCCS)
                              if UwU == "Race":
                                        with open("CharacterSheet.json", "r") as uio:
                                                  CSJ = json.load(uio)
                                        print(CSJ)
                              if UwU == "Health":
                                        HealthStat = int(input("How do you want to change the Health? ( Integers only / add '-' for negative )"))
                                        Health = Health + HealthStat
                                        return Health
                    ImCha = str(input("Is that all? ( Y / N )"))
                    if ImCha == "Y":
                              ExTra = False
while RunGamePweaseTwT == True:
          DM()
          '''print('')
          print(f'PMC : {PoorMensChange}')
          print(f'CMC : {CommonMensChange}')
          print(f'NC : {NoblesCurrancy}')
          print(f'KK : {KingsmenChange}')
          print('')'''
          Player()
