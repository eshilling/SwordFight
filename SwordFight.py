import time, random, sys
P1Health = 50
P2Health = 50
GameRun = P2Health * P1Health
SlashDamage = -2
StabDamage = -5
BleedingDamage = -1
Rd = 1
P1Blood = 0
P2Blood = 0

print("""How to play:
Please put player inputs as 1, 2, or 3 then press enter. 
Slashing is more likely to hit but does less damage. 
Stabbing does more damage but is harder to land a hit.
After each hit there is a chance bleeding damage will occure.
Bleeding causes damage over time. The more you are bleeding the more damage you take each turn. 
On each hit there is a chance of a critical hit. Crits cause double damage.
If you wish to play agianst the computer enter Player 2 name as "computer"
""")
time.sleep(2)
P1Name = str(input("Player 1, what is your name?\n"))
P2Name = str(input("Player 2, what is your name?\n"))
print("This is a battle to the DEATH. May the best sword fighter win!")
time.sleep(1)
while GameRun != 0:
  if P2Name != "computer":
    IsBlood = random.randint(1, 20)
    P1Tripp = random.randint(1, 100)
    P2Tripp = random.randint(1, 100)
    print("Round " + str(Rd))
    print(P1Name + ", what is your action?")
    Action1 = input("1 - SLASH\n2 - STAB\n3 - DODGE\n")
    print(P2Name + ", what is your action?")
    Action2 = input("1 - SLASH\n2 - STAB\n3 - DODGE\n")
    time.sleep(1)
    if P1Tripp != 100 and P2Tripp != 100:
        if Action1 == "1":
            p1 = random.randint(5, 10)
            damage1 = SlashDamage
            if p1 == 10:
                damage1 = SlashDamage * 2
        elif Action1 == "2":
            p1 = random.randint(1, 10)
            damage1 = StabDamage
            if p1 == 10:
                damage1 = StabDamage * 2
        elif Action1 == "3":
            p1 = random.randint(9, 10)
        if Action2 == "1":
            p2 = random.randint(5, 10)
            damage2 = SlashDamage
            if p2 == 10:
                damage2 = SlashDamage * 2
        elif Action2 == "2":
            p2 = random.randint(1, 10)
            damage2 = StabDamage
            if p2 == 10:
                damage2 = StabDamage * 2
        elif Action2 == "3":
            p2 = random.randint(9, 10)
        if Action1 == "3" and Action2 == "3":
            time.sleep(1)
            print("Both warriors step aback.")
        elif Action1 != "3" or Action2 != "3":
            time.sleep(1)
            print("THWANG!")
            time.sleep(.5)
            print("KLANK!")
            time.sleep(.5)
            print("TINK!")
            time.sleep(1)
            if p1 >= p2 and Action1 == "3":
                print(P1Name + " dodges the blow!")
            elif p2 >= p1 and Action2 == "3":
                print(P2Name + " dodges the blow!")
            elif p1 > p2:
                P2Health += damage1
                print(P2Name + " takes a hit!")
                if IsBlood >= 15:
                    P2Health += BleedingDamage
                    print("That wound is SPEWING!")
                    P2Blood += 1
            elif p2 > p1:
                P1Health += damage2
                print(P1Name + " takes a hit!")
                if IsBlood >= 15:
                    P1Health += BleedingDamage
                    print("That wound is SPEWING!")
                    P1Blood += 1
            elif p1 == p2:
                print("The blades glent off each other with a thwang")
        P1Health += P1Blood * BleedingDamage
        P2Health += P2Blood * BleedingDamage
        if P1Blood >= 1:
            print(P1Name + " is still bleeding!")
        if P2Blood >= 1:
            print(P2Name + " is still bleeding!")
        if P1Health <= 0:
            print(P1Name + " is dead.")
            time.sleep(3)
            print("Do you feel good about this?")
            time.sleep(2)
            print("Do you feel good about killing them?")
            time.sleep(2)
            bean = input("Y/N")
            sys.exit()
        elif P2Health <= 0:
            print(P2Name + " is dead.")
            time.sleep(3)
            print("Do you feel good about this?")
            time.sleep(2)
            print("Do you feel good about killing them?")
            time.sleep(2)
            bean = input("Y/N")
            sys.exit()
    elif P1Tripp == 100:
        print(P1Name + " TRIPPED! What an IDIOT!")
    elif P2Tripp == 100:
        print(P2Name + " TRIPPED! What an IDIOT!")
    elif P1Tripp == 100 and P2Tripp == 100:
        print("You both tripped. You're just lying on the ground now...")
        sys.exit()
    Rd += 1
    print("Health:")
    print(P1Name + " - " + str(P1Health))
    print(P2Name + " - " + str(P2Health))
    time.sleep(1)
  elif P2Name == "computer":
    CName = "Blathgar"
    IsBlood = random.randint(1, 20)
    P1Tripp = random.randint(1, 100)
    P2Tripp = random.randint(1, 100)
    print("Round " + str(Rd))
    print("What is your action?")
    Action1 = input("1 - SLASH\n2 - STAB\n3 - DODGE\n")
    Action2 = str(random.randint(1, 3))
    time.sleep(1)
    if P1Tripp != 100 and P2Tripp != 100:
      if Action1 == "1":
        p1 = random.randint(5, 10)
        damage1 = SlashDamage
        if p1 == 10:
          damage1 = SlashDamage * 2
      elif Action1 == "2":
        p1 = random.randint(1, 10)
        damage1 = StabDamage
        if p1 == 10:
          damage1 = StabDamage * 2
      elif Action1 == "3":
        p1 = random.randint(9, 10)
      if Action2 == "1":
        p2 = random.randint(5, 10)
        damage2 = SlashDamage
        if p2 == 10:
          damage2 = SlashDamage * 2
      elif Action2 == "2":
        p2 = random.randint(1, 10)
        damage2 = StabDamage
        if p2 == 10:
          damage2 = StabDamage * 2
      elif Action2 == "3":
        p2 = random.randint(9, 10)
      if Action1 == "3" and Action2 == "3":
        time.sleep(1)
        print("Both warriors step aback.")
      elif Action1 != "3" or Action2 != "3":
        time.sleep(1)
        print("THWANG!")
        time.sleep(.5)
        print("KLANK!")
        time.sleep(.5)
        print("TINK!")
        time.sleep(1)
        if p1 >= p2 and Action1 == "3":
          print(P1Name + " dodges the blow!")
        elif p2 >= p1 and Action2 == "3":
          print(CName + " dodges the blow!")
        elif p1 > p2:
          P2Health += damage1
          print(CName + " takes a hit!")
          if IsBlood >= 15:
            P2Health += BleedingDamage
            print("That wound is SPEWING!")
            P2Blood += 1
        elif p2 > p1:
          P1Health += damage2
          print(P1Name + " takes a hit!")
          if IsBlood >= 15:
            P1Health += BleedingDamage
            print("That wound is SPEWING!")
            P1Blood += 1
        elif p1 == p2:
          print("The blades glent off each other with a thwang")
      P1Health += P1Blood * BleedingDamage
      P2Health += P2Blood * BleedingDamage
      if P1Blood >= 1:
        print(P1Name + " is still bleeding!")
      if P2Blood >= 1:
        print(CName + " is still bleeding!")
      if P1Health <= 0:
        print(P1Name + " is dead.")
        time.sleep(3)
        sys.exit()
      elif P2Health <= 0:
        print(CName + " is dead.")
        time.sleep(3)
        print("Do you feel good about this?")
        time.sleep(2)
        print("Do you feel good about killing them?")
        time.sleep(2)
        bean = input("Y/N")
        sys.exit()
    elif P1Tripp == 100:
      print(P1Name + " TRIPPED! What an IDIOT!")
    elif P2Tripp == 100:
      print(CName + " TRIPPED! What an IDIOT!")
    elif P1Tripp == 100 and P2Tripp == 100:
      print("You both tripped. You're just lying on the ground now...")
      sys.exit()
    Rd += 1
    print("Health:")
    print(P1Name + " - " + str(P1Health))
    print(CName + " - " + str(P2Health))
    time.sleep(1)