# To update prices of ores in the current market check out the 'Prices' folder in the file directory and change the values in each file -- You might have to 'Fork' this program

import random
import time
import os

korreliteCompleted = False
rekniteCompleted = False
gelliumCompleted = False
axnitCompleted = False
blueNarcorCompleted = False
redNarcorCompleted = False
vexniumCompleted = False
creditsCompleted = False


print('''IMPORTANT - Read the top of the code for user notes!
Would you like to continue collecting ores or would you like to start again?''')
startAgain = input("[type 'y' to start again, and 'n' to continue]:")

if startAgain.lower() == "y":
  print("Would you like to use a catalogue item?")
  catalogue = input("[enter 'y' for yes and 'n' for no]: ")
  if catalogue.lower() == "n":
    print("How much korrelite do you need: ")
    file = open("Ore/korrelite", "w")
    file.write(input("[Enter amount here]: "))
    file.close()
    print()

    print("How much reknite do you need: ")
    file = open("Ore/reknite", "w")
    file.write(input("[Enter amount here]: "))
    file.close()
    print()

    print("How much gellium do you need: ")
    file = open("Ore/gellium", "w")
    file.write(input("[Enter amount here]: "))
    file.close()
    print()

    print("How much axnit do you need: ")
    file = open("Ore/axnit", "w")
    file.write(input("[Enter amount here]: "))
    file.close()
    print()

    print("How much blue narcor do you need: ")
    file = open("Ore/bluenarcor", "w")
    file.write(input("[Enter amount here]: "))
    file.close()
    print()

    print("How much red narcor do you need: ")
    file = open("Ore/rednarcor", "w")
    file.write(input("[Enter amount here]: "))
    file.close()
    print()

    print("How much vexnium do you need: ")
    file = open("Ore/vexnium", "w")
    file.write(input("[Enter amount here]: "))
    file.close()
    print()

    print("How many credits do you need: ")
    file = open("Ore/credits", "w")
    file.write(input("[Enter amount here]: "))
    file.close()
    print()

    file = open("Num/korreliteNum", "w")
    file.write("0")
    file.close()

    file = open("Num/rekniteNum", "w")
    file.write("0")
    file.close()

    file = open("Num/gelliumNum", "w")
    file.write("0")
    file.close()

    file = open("Num/axnitNum", "w")
    file.write("0")
    file.close()

    file = open("Num/bluenarcorNum", "w")
    file.write("0")
    file.close()

    file = open("Num/rednarcorNum", "w")
    file.write("0")
    file.close()

    file = open("Num/vexniumNum", "w")
    file.write("0")
    file.close()

    file = open("Num/creditsNum", "w")
    file.write("0")
    file.close()
  elif catalogue.lower() == "y":
    print("Would you like to make a new item or use a saved one?")
    item = input("[enter 'n' for a new one and 's' for a saved one]:")
    if item.lower() == "n":
      print("What is the item's name?")
      name = input("[enter the name here]: ")
      print()
      print("What is the amount of korrelite needed?")
      korrelite = input("[enter number here]: ")
      print()
      print("What is the amount of reknite needed?")
      reknite = input("[enter number here]: ")
      print()
      print("What is the amount of gellium needed?")
      gellium = input("[enter number here]: ")
      print()
      print("What is the amount of axnit needed?")
      axnit = input("[enter number here]: ")
      print()
      print("What is the amount of blue narcor needed?")
      blueNarcor = input("[enter number here]: ")
      print()
      print("What is the amount of red narcor needed?")
      redNarcor = input("[enter number here]: ")
      print()
      print("What is the amount of vexnium needed?")
      vexnium = input("[enter number here]: ")
      print()
      print("What is the amount of credits needed?")
      credits = input("[enter number here]: ")
      print()
      text = (f'''
{korrelite};
{reknite};
{gellium};
{axnit};
{blueNarcor};
{redNarcor};
{vexnium};
{credits}
      ''')
      file = open("Ore/korrelite", "w")
      file.write(str(int(korrelite)))
      file.close()
      file = open("Ore/reknite", "w")
      file.write(reknite)
      file.close()
      file = open("Ore/gellium", "w")
      file.write(gellium)
      file.close()
      file = open("Ore/axnit", "w")
      file.write(axnit)
      file.close()
      file = open("Ore/bluenarcor", "w")
      file.write(blueNarcor)
      file.close()
      file = open("Ore/rednarcor", "w")
      file.write(redNarcor)
      file.close()
      file = open("Ore/vexnium", "w")
      file.write(vexnium)
      file.close()
      file = open("Ore/credits", "w")
      file.write(credits)
      file.close()
      file = open("Num/korreliteNum", "w")
      file.write("0")
      file.close()
      file = open("Num/rekniteNum", "w")
      file.write("0")
      file.close()
      file = open("Num/gelliumNum", "w")
      file.write("0")
      file.close()
      file = open("Num/axnitNum", "w")
      file.write("0")
      file.close()
      file = open("Num/bluenarcorNum", "w")
      file.write("0")
      file.close()
      file = open("Num/rednarcorNum", "w")
      file.write("0")
      file.close()
      file = open("Num/vexniumNum", "w")
      file.write("0")
      file.close()
      file = open("Num/creditsNum", "w")
      file.write("0")
      file.close()
      file = open(f"Catalogue/{name.upper()}", "w")
      file.write(text)
      file.close()

    elif item.lower() == "s":
      print("Enter the name of the item.")
      name = input("[enter name here]: ")
      try:
        file = open(f"Catalogue/{name.upper()}", "r")
      except:
        exit(f"There is not file with the directory: 'Catalogue/{name.upper()}'")
      read = file.read()
      find = read.find(";")
      korrelite = read[0:find]
      read = read[find+1:]
      find = read.find(";")
      reknite = read[0:find]
      read = read[find+1:]
      find = read.find(";")
      gellium = read[0:find]
      read = read[find+1:]
      find = read.find(";")
      axnit = read[0:find]
      read = read[find+1:]
      find = read.find(";")
      blueNarcor = read[0:find]
      read = read[find+1:]
      find = read.find(";")
      redNarcor = read[0:find]
      read = read[find+1:]
      find = read.find(";")
      vexnium = read[0:find]
      read = read[find+1:]
      find = read.find(";")
      credits = read[0:find]
      read = read[find+1:]

      file = open("Ore/korrelite", "w")
      file.write(korrelite)
      file.close()
      file = open("Ore/reknite", "w")
      file.write(reknite)
      file.close()
      file = open("Ore/gellium", "w")
      file.write(gellium)
      file.close()
      file = open("Ore/axnit", "w")
      file.write(axnit)
      file.close()
      file = open("Ore/bluenarcor", "w")
      file.write(blueNarcor)
      file.close()
      file = open("Ore/rednarcor", "w")
      file.write(redNarcor)
      file.close()
      file = open("Ore/vexnium", "w")
      file.write(vexnium)
      file.close()
      file = open("Ore/credits", "w")
      file.write(credits)
      file.close()

      file = open("Num/korreliteNum", "w")
      file.write("0")
      file.close()

      file = open("Num/rekniteNum", "w")
      file.write("0")
      file.close()

      file = open("Num/gelliumNum", "w")
      file.write("0")
      file.close()

      file = open("Num/axnitNum", "w")
      file.write("0")
      file.close()

      file = open("Num/bluenarcorNum", "w")
      file.write("0")
      file.close()

      file = open("Num/rednarcorNum", "w")
      file.write("0")
      file.close()

      file = open("Num/vexniumNum", "w")
      file.write("0")
      file.close()

      file = open("Num/creditsNum", "w")
      file.write("0")
      file.close()

while True:
  print()
  loop = 8
  while loop !=0:
    if loop == 6:
      mat = "korrelite"
    elif loop == 5:
      mat = "reknite"
    elif loop == 4:
      mat = "gellium"
    elif loop == 3:
      mat = "axnit"
    elif loop == 2:
      mat = "bluenarcor"
    elif loop == 1:
      mat = "rednarcor"
    elif loop == 7:
      mat = "vexnium"
    elif loop == 8:
      mat = "credits"

    file = open(f"Num/{mat}Num", "r")
    currentNum = str(int(file.read()))
    file.close()

    file = open(f"Ore/{mat}", "r")
    currentMat = file.read()
    file.close()

    if int(currentNum) >= int(currentMat):
      completed = True
    else:
      completed = False
    if completed == True:
      if loop == 6:
        korreliteCompleted = True
      elif loop == 5:
        rekniteCompleted = True
      elif loop == 4:
        gelliumCompleted = True
      elif loop == 3:
        axnitCompleted = True
      elif loop == 2:
        blueNarcorCompleted = True
      elif loop == 1:
        redNarcorCompleted = True
      elif loop == 7:
        vexniumCompleted = True
      elif loop == 8:
        creditsCompleted = True
    elif completed == False:
      if loop == 6:
        korreliteCompleted = False
      elif loop == 5:
        rekniteCompleted = False
      elif loop == 4:
        gelliumCompleted = False
      elif loop == 3:
        axnitCompleted = False
      elif loop == 2:
        blueNarcorCompleted = False
      elif loop == 1:
        redNarcorCompleted = False
      elif loop == 7:
        vexniumCompleted = False
      elif loop == 8:
        creditsCompleted = False

    loop = loop -1

    


  print("\033[0;37;0mWould you like to add or veiw amounts?")
  addVeiw = input("[type 'a' to add or 'v' to veiw]: ")
  os.system('clear')

  if addVeiw.lower() == "v":
    korrelite = open("Num/korreliteNum", "r")
    reknite = open("Num/rekniteNum", "r")
    gellium = open("Num/gelliumNum", "r")
    axnit = open("Num/axnitNum", "r")
    bluenarcor = open("Num/bluenarcorNum", "r")
    rednarcor = open("Num/rednarcorNum", "r")
    vexnium = open("Num/vexniumNum", "r")
    credits = open("Num/creditsNum", "r")

    korreliteNum = open("Ore/korrelite", "r")
    rekniteNum = open("Ore/reknite", "r")
    gelliumNum = open("Ore/gellium", "r")
    axnitNum = open("Ore/axnit", "r")
    bluenarcorNum = open("Ore/bluenarcor", "r")
    rednarcorNum = open("Ore/rednarcor", "r")
    vexniumNum = open("Ore/vexnium", "r")
    creditsNum = open("Ore/credits", "r")

    korrelitePrice = open("Prices/korrelite", "r")
    reknitePrice = open("Prices/reknite", "r")
    gelliumPrice = open("Prices/gellium", "r")
    axnitPrice = open("Prices/axnit", "r")
    blueNarcorPrice = open("Prices/blueNarcor", "r")
    redNarcorPrice = open("Prices/redNarcor", "r")
    vexniumPrice = open("Prices/vexnium", "r")
    creditsPrice = open("Prices/credits", "r")


    print()
    if korreliteCompleted == True:
      kN = korreliteNum.read()
      k = korrelite.read()
      kP = korrelitePrice.read()
      print("\033[1;32;40mKorrelite:", k, "/", kN, "\033[0;31;40m--", int(k) - int(kN), "extra \033[0;33;40m--", (abs(int(kP) * (int(kN)-int(k)))), "C")
    else:
      kN = korreliteNum.read()
      k = korrelite.read()
      kP = korrelitePrice.read()
      print("\033[0;37;40mKorrelite:",k, "/", kN, "\033[0;31;40m--", int(kN) - int(k), "needed", "\033[0;33;40m--", int(kP) * (int(kN)-int(k)), "C")

    if rekniteCompleted == True:
      rN = rekniteNum.read()
      r = reknite.read()
      rP = reknitePrice.read()
      print("\033[1;32;40mReknite:", r, "/", rN, "\033[0;31;40m--", int(r) - int(rN), "extra \033[0;33;40m--", (abs(int(rP) * (int(rN)-int(r)))), "C")
    else:
      rN = rekniteNum.read()
      r = reknite.read()
      rP = reknitePrice.read()
      print("\033[0;37;40mReknite:", r, "/", rN, "\033[0;31;40m--", int(rN) - int(r), "needed", "\033[0;33;40m--", int(rP) * (int(rN)-int(r)), "C")

    if gelliumCompleted == True:
      gN = gelliumNum.read()
      g = gellium.read()
      gP = gelliumPrice.read()
      print("\033[1;32;40mGellium:", g, "/", gN, "\033[0;31;40m--", int(g) - int(gN), "extra \033[0;33;40m--", (abs(int(gP) * (int(gN)-int(g)))), "C")
    else:
      gN = gelliumNum.read()
      g = gellium.read()
      gP = gelliumPrice.read()
      print("\033[0;37;40mGellium:", g, "/", gN, "\033[0;31;40m--", int(gN) - int(g), "needed", "\033[0;33;40m--", int(gP) * (int(gN)-int(g)), "C")

    if axnitCompleted == True:
      aN = axnitNum.read()
      a = axnit.read()
      aP = axnitPrice.read()
      print("\033[1;32;40mAxnit:", a, "/", aN, "\033[0;31;40m--", int(a) - int(aN), "extra \033[0;33;40m--", (abs(int(aP) * (int(aN)-int(a)))), "C")
    else:
      aN = axnitNum.read()
      a = axnit.read()
      aP = axnitPrice.read()
      print("\033[0;37;40mAxnit:", a, "/", aN, "\033[0;31;40m--", int(aN) - int(a), "needed", "\033[0;33;40m--", int(aP) * (int(aN)-int(a)), "C")

    if blueNarcorCompleted == True:
      bN = bluenarcorNum.read()
      b = bluenarcor.read()
      bP = blueNarcorPrice.read()
      print("\033[1;32;40mBlue Narcor:", b, "/", bN, "\033[0;31;40m--", int(b) - int(bN), "extra \033[0;33;40m--", (abs(int(bP) * (int(bN)-int(b)))), "C")
    else:
      bN = bluenarcorNum.read()
      b = bluenarcor.read()
      bP = blueNarcorPrice.read()
      print("\033[0;37;40mBlue Narcor:", b, "/", bN, "\033[0;31;40m--", int(bN) - int(b), "needed", "\033[0;33;40m--", int(bP) * (int(bN)-int(b)), "C")

    if redNarcorCompleted == True:
      reN = rednarcorNum.read()
      re = rednarcor.read()
      reP = redNarcorPrice.read()
      print("\033[1;32;40mRed Narcor:", re, "/", reN, "\033[0;31;40m--", int(re) - int(reN), "extra \033[0;33;40m--", (abs(int(reP) * (int(reN)-int(re)))), "C")
    else:
      reN = rednarcorNum.read()
      re = rednarcor.read()
      reP = redNarcorPrice.read()
      print("\033[0;37;40mRed Narcor:", re, "/", reN, "\033[0;31;40m--", int(reN) - int(re), "needed", "\033[0;33;40m--", int(reP) * (int(reN)-int(re)), "C")

    if vexniumCompleted == True:
      vN = vexniumNum.read()
      v = vexnium.read()
      vP = vexniumPrice.read()
      print("\033[1;32;40mVexnium:", v, "/", vN, "\033[0;31;40m--", int(v) - int(vN), "extra \033[0;33;40m--", (abs(int(vP) * (int(vN)-int(v)))), "C")
    else:
      vN = vexniumNum.read()
      v = vexnium.read()
      vP = vexniumPrice.read()
      print("\033[0;37;40mVexnium:", v, "/", vN, "\033[0;31;40m--", int(vN) - int(v), "needed", "\033[0;33;40m--", int(vP) * (int(vN)-int(v)), "C")

    if creditsCompleted == True:
      cN = creditsNum.read()
      c = credits.read()
      cP = creditsPrice.read()
      print("\033[1;32;40mCredits:", c, "/", cN, "\033[0;31;40m--", int(c) - int(cN), "extra \033[0;33;40m--", (abs(int(cP) * (int(cN)-int(c)))), "C")
    else:
      cN = creditsNum.read()
      c = credits.read()
      cP = creditsPrice.read()
      print("\033[0;37;40mCredits:", c, "/", cN, "\033[0;31;40m--", int(cN) - int(c), "needed", "\033[0;33;40m--", int(cP) * (int(cN)-int(c)), "C")
    print()

    if korreliteCompleted == False or rekniteCompleted == False or gelliumCompleted == False or axnitCompleted == False or blueNarcorCompleted == False or redNarcorCompleted == False or vexniumCompleted == False or creditsCompleted == False:
      total = str((int(kP) * (int(kN)-int(k))) + (int(rP) * (int(rN)-int(r))) + (int(gP) * (int(gN)-int(g))) + (int(aP) * (int(aN)-int(a))) + (int(bP) * (int(bN)-int(b))) + (int(reP) * (int(reN)-int(re))) + (int(vP) * (int(vN)-int(v)))+(int(cP)* (int(cN)-int(c))))
      print("\033[0;33;40m--Credits needed:" + total)
      print()

    elif korreliteCompleted == True and rekniteCompleted == True and gelliumCompleted == True and axnitCompleted == True and blueNarcorCompleted == True and redNarcorCompleted == True and vexniumCompleted == True and creditsCompleted == True:
      total = str(abs((int(kP) * (int(kN)-int(k))) + (int(rP) * (int(rN)-int(r))) + (int(gP) * (int(gN)-int(g))) + (int(aP) * (int(aN)-int(a))) + (int(bP) * (int(bN)-int(b))) + (int(reP) * (int(reN)-int(re))) + (int(vP) * (int(vN)-int(v)))+(int(cP)* (int(cN)-int(c)))))
      print("\033[0;33;40m--Credits extra:" + total)
      print()
    korrelite.close()
    reknite.close()
    gellium.close()
    axnit.close()
    bluenarcor.close()
    rednarcor.close()
    vexnium.close()
    credits.close()

    korreliteNum.close()
    rekniteNum.close()
    gelliumNum.close()
    axnitNum.close()
    bluenarcorNum.close()
    rednarcorNum.close()
    vexniumNum.close()
    creditsNum.close()

    korrelitePrice.close()
    reknitePrice.close()
    gelliumPrice.close()
    axnitPrice.close()
    blueNarcorPrice.close()
    redNarcorPrice.close()
    vexniumPrice.close()
    creditsPrice.close()
  
  elif addVeiw.lower() == "a":
    try:
      print("What would you like to add?")
      add = input("[type the material here]:").lower()

      print("How much would you like to add?")
      numAdd = input("[enter the number here]:").lower()
      
      file = open(f"Num/{add}Num", "r")
      currentNum = file.read()
      file.close()

      file = open(f"Num/{add}Num", "w")
      write = int(currentNum) + int(numAdd)
      file.write(f"{str(write)}")
      file.close()

      file = open(f"Num/{add}Num", "r")
      currentNum = file.read()
      file.close()

      file = open(f"Ore/{add}", "r")
      currentMat = file.read()
      file.close()
    except:
      print('''That is not an option.
Try any of the following: korrelite, reknite, gellium, axnit, bluenarcor,
rednarcor, vexnium, credits.''')
      print()

  else:
    print("That is not an option!")
    print()
 