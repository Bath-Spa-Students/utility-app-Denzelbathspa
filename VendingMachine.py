# Vending Machine
# Version 1.3
# Python 3.11.6

import random
import time
import os

# ANSI escape codes for text formatting and colors
# WARNING: Might not work on other editors!!
RED_TEXT = "\033[31m"
GREEN_TEXT = "\033[32m"
YELLOW_TEXT = "\033[33m"
BLUE_TEXT = "\033[34m"
MAGENTA_TEXT = "\033[35m"
CYAN_TEXT = "\033[36m"
WHITE_TEXT = "\033[37m"
DARK_RED_TEXT = "\033[31;2m"   
DARK_GREEN_TEXT = "\033[32;2m"   
DARK_YELLOW_TEXT = "\033[33;2m"  
DARK_BLUE_TEXT = "\033[34;2m"    
DARK_MAGENTA_TEXT = "\033[35;2m" 
DARK_CYAN_TEXT = "\033[36;2m"    
DARK_WHITE_TEXT = "\033[37;2m" 
RESET_TEXT = "\033[0m"  

# Using a dict to store rows of products
row1 = {"A1":"Orange Juice","A2":"Apple Juice","A3":"Mango Juice","A4": "Grape Juice","A5":"Ginger Ale","A6":"Lemonade"}
row2 = {"B1":"Pepsi","B2":"Coca-Cola","B3":"Sprite","B4":"Dr. Pepper","B5":"Fanta","B6":"Mountain Dew"}
row3 = {"C1":"Cappaccino","C2":"Americano","C3":"Espresso","C4":"Latte","C5":"Mocha","C6":"Macchiato"}
row4 = {"D1": "Potato Chips","D2": "Chocolate Bars","D3": "Popcorn","D4": "Pretzels","D5": "Candy","D6": "Trail Mix"}

# Using a dict to store random price numbers as keys and storage as values.
pRow1 ={}
pRow2 = {}
pRow3 = {}
def priceStock(row,column):
    count = len(column)
    while True:
        pR = random.randint(1,9)
        stock = random.randint(10,20)
        if str(pR) not in row:
            row[str(pR)] = stock
            count-=1
        if count <= 0:
            break

# This checks all the dicts to see if the user input is a valid key or not and returns the value
def rowChecker(uInput):
    if row1.get(uInput) != None:
        return row1.get(uInput)
    elif row2.get(uInput) != None:
        return row2.get(uInput)
    elif row3.get(uInput) != None:
        return row3.get(uInput)
    else:
        return False

# User balance
userBalance = 0
# Stores user choices in a variable
paidItems = "Default"

# Returns recomended items
def recomended(uInput):
    if uInput in row1.values():
        joined = ', '.join(map(str,list(row1.values())))
        return joined
    if uInput in row2.values():
        joined = ', '.join(map(str,list(row2.values())))
        return joined
    if uInput in row3.values():
        joined = ', '.join(map(str,list(row3.values())))
        return joined

# This combines the price, Stocks to the user choice and displays the bill
def userInputChoice(row,price_stock,userChoice):
    global userBalance
    global paidItems
    userChoiceValues = list(row.values())
    priceKeys = list(price_stock.keys())
    stockValues = list(price_stock.values())
    pK = userChoiceValues.index(userChoice) # gets number index as int
    sV = userChoiceValues.index(userChoice) # gets number index as int
    if userBalance < 0: # Sets user balance to 0 if it goes to the negative integer
        userBalance = 0
    print(f"\n{WHITE_TEXT}{userChoice} costs {priceKeys[pK]}$. There are {stockValues[sV]} {userChoice} left")
    print(f"Total Balance Left: {YELLOW_TEXT}{userBalance}${WHITE_TEXT}\n")
    buyOrNot = input(f"{MAGENTA_TEXT}Would you like to purchase?\n{WHITE_TEXT}Type {GREEN_TEXT}Yes{WHITE_TEXT} or {RED_TEXT}No:{CYAN_TEXT} ")

    while True:
        if buyOrNot.upper() == "YES" and userBalance >= int(priceKeys[pK]):
            if price_stock[priceKeys[pK]] > 0: # checks if product is still in stock and deducts 1 if it is in stock.
                userBalance -= int(priceKeys[pK])
                price_stock[priceKeys[pK]] -= 1
                print(f"\n{GREEN_TEXT}You have purchased {userChoice} for {priceKeys[pK]}$.\nTotal Balance Left: {YELLOW_TEXT}{userBalance}${WHITE_TEXT}\n")
                paidItems = userChoice
                loading()
                break
            else:
                print(f"\n{RED_TEXT}{userChoice} is unavailable, please pick another product.{WHITE_TEXT}\n")
                loading()
                break
        elif buyOrNot.upper() == "NO":
            loading()
            break
        elif userBalance < int(priceKeys[pK]):
            print(f"{RED_TEXT}Not enough money to buy! Pick another product!{WHITE_TEXT}")
            loading()
            break
        else:
            print(f"{RED_TEXT}Type only Yes or No!!{WHITE_TEXT}")
            loading()
            break

def priceDisplay(priceRow,whatRow):
    priceList = list(priceRow.keys())# Puts all the keys in pRow in to a list
    return "$"+str(priceList[whatRow])

def labelDisplay(Row,whatRow):
    label = list(Row.keys())# Puts all the keys in pRow in to a list
    return label[whatRow]

def stockDisplay(price_stock,Row):
    stockValues = list(price_stock.values())
    if stockValues[Row] == 0:
        return RED_TEXT
    else:
        return MAGENTA_TEXT 
        
# Vending Machine Visuals
def vendingMachine():
    print(f"{WHITE_TEXT}===============================================================\n",f"{YELLOW_TEXT}"
          f"|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n",
          f"||                                                       ||\n",
          f"||\t{stockDisplay(pRow1,0)}- {row1['A1']} \t- {row1['A2']} \t- {row1['A3']} \t {YELLOW_TEXT} ||\n",
          f"||\t{WHITE_TEXT}- {labelDisplay(row1,0)} - {GREEN_TEXT}{priceDisplay(pRow1,0)}{WHITE_TEXT} \t- {labelDisplay(row1,1)} - {GREEN_TEXT}{priceDisplay(pRow1,1)}{WHITE_TEXT} \t- {labelDisplay(row1,2)} - {GREEN_TEXT}{priceDisplay(pRow1,2)}{YELLOW_TEXT} \t  ||\n",
          f"||                                                       ||\n",
          f"||\t{WHITE_TEXT}- {row1['A4']} \t- {row1['A5']} \t- {row1['A6']} \t {YELLOW_TEXT} ||\n",
          f"||\t{WHITE_TEXT}- {labelDisplay(row1,3)} - {GREEN_TEXT}{priceDisplay(pRow1,3)}{WHITE_TEXT} \t- {labelDisplay(row1,4)} - {GREEN_TEXT}{priceDisplay(pRow1,4)}{WHITE_TEXT} \t- {labelDisplay(row1,5)} - {GREEN_TEXT}{priceDisplay(pRow1,5)}{YELLOW_TEXT} \t  ||\n",
          f"||                                                       ||\n",
          f"||\t{WHITE_TEXT}- {row2['B1']} \t- {row2['B2']} \t- {row2['B3']} \t {YELLOW_TEXT} ||\n",
          f"||\t{WHITE_TEXT}- {labelDisplay(row2,0)} - {GREEN_TEXT}{priceDisplay(pRow2,0)}{WHITE_TEXT} \t- {labelDisplay(row2,1)} - {GREEN_TEXT}{priceDisplay(pRow2,1)}{WHITE_TEXT} \t- {labelDisplay(row2,2)} - {GREEN_TEXT}{priceDisplay(pRow2,2)}{YELLOW_TEXT} \t  ||\n",
          f"||                                                       ||\n",
          f"||\t{WHITE_TEXT}- {row2['B4']} \t- {row2['B5']} \t- {row2['B6']} \t {YELLOW_TEXT} ||\n",
          f"||\t{WHITE_TEXT}- {labelDisplay(row2,3)} - {GREEN_TEXT}{priceDisplay(pRow2,3)}{WHITE_TEXT} \t- {labelDisplay(row2,4)} - {GREEN_TEXT}{priceDisplay(pRow2,4)}{WHITE_TEXT} \t- {labelDisplay(row2,5)} - {GREEN_TEXT}{priceDisplay(pRow2,5)}{YELLOW_TEXT} \t  ||\n",
          f"||                                                       ||\n",
          f"||\t{WHITE_TEXT}- {row3['C1']} \t- {row3['C2']} \t- {row3['C3']} \t {YELLOW_TEXT} ||\n",
          f"||\t{WHITE_TEXT}- {labelDisplay(row3,0)} - {GREEN_TEXT}{priceDisplay(pRow3,0)}{WHITE_TEXT} \t- {labelDisplay(row3,1)} - {GREEN_TEXT}{priceDisplay(pRow3,1)}{WHITE_TEXT} \t- {labelDisplay(row3,2)} - {GREEN_TEXT}{priceDisplay(pRow3,2)}{YELLOW_TEXT} \t  ||\n",
          f"||                                                       ||\n",
          f"||\t{WHITE_TEXT}- {row3['C4']} \t- {row3['C5']} \t- {row3['C6']} \t {YELLOW_TEXT} ||\n",
          f"||\t{WHITE_TEXT}- {labelDisplay(row3,3)} - {GREEN_TEXT}{priceDisplay(pRow3,3)}{WHITE_TEXT} \t- {labelDisplay(row3,4)} - {GREEN_TEXT}{priceDisplay(pRow3,4)}{WHITE_TEXT} \t- {labelDisplay(row3,5)} - {GREEN_TEXT}{priceDisplay(pRow3,5)}{YELLOW_TEXT} \t  ||\n",
          f"||                                                       ||\n",
          f"|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n",
          f"|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n",
          f"|||||||||||||||||||||||||||||||||||||||||||{DARK_BLUE_TEXT}||{WHITE_TEXT}00{DARK_BLUE_TEXT}||{WHITE_TEXT}00{DARK_BLUE_TEXT}||{WHITE_TEXT}00{DARK_BLUE_TEXT}||{RESET_TEXT}{YELLOW_TEXT}||\n",
          f"|||||||||||||||||||||||||||||||||||||||||||{DARK_BLUE_TEXT}||{WHITE_TEXT}00{DARK_BLUE_TEXT}||{WHITE_TEXT}00{DARK_BLUE_TEXT}||{WHITE_TEXT}00{DARK_BLUE_TEXT}||{RESET_TEXT}{YELLOW_TEXT}||\n",
          f"||||{DARK_CYAN_TEXT}|||||||||||||||||||||||||||||||||||{RESET_TEXT}{YELLOW_TEXT}||||{DARK_BLUE_TEXT}||{WHITE_TEXT}00{DARK_BLUE_TEXT}||{WHITE_TEXT}00{DARK_BLUE_TEXT}||{WHITE_TEXT}00{DARK_BLUE_TEXT}||{RESET_TEXT}{YELLOW_TEXT}||\n",
          f"||||{DARK_CYAN_TEXT}|||||||||||||||||||||||||||||||||||{RESET_TEXT}{YELLOW_TEXT}||||||||||||||||||||\n",
          f"||||{DARK_WHITE_TEXT}|||||||||||||||||||||||||||||||||||{RESET_TEXT}{YELLOW_TEXT}||||||||||||||||||||\n",
          f"|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n",
          f"|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n",
          f"|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||{RESET_TEXT}\n")

# Text Art
def loading():
    sleeptime = 0.2
    print(f"Returning to menu {YELLOW_TEXT}▒▒▒▒▒▒▒▒▒▒ 0%...{RESET_TEXT}", end = "\r")
    time.sleep(sleeptime)
    print(f"Returning to menu {YELLOW_TEXT}█▒▒▒▒▒▒▒▒▒ 10%...{RESET_TEXT}", end = "\r")
    time.sleep(sleeptime)
    print(f"Returning to menu {YELLOW_TEXT}██▒▒▒▒▒▒▒▒ 20%...{RESET_TEXT}", end = "\r")
    time.sleep(sleeptime)
    print(f"Returning to menu {YELLOW_TEXT}███▒▒▒▒▒▒▒ 30%...{RESET_TEXT}", end = "\r")
    time.sleep(sleeptime)
    print(f"Returning to menu {YELLOW_TEXT}████▒▒▒▒▒▒ 40%...{RESET_TEXT}", end = "\r")
    time.sleep(sleeptime)
    print(f"Returning to menu {YELLOW_TEXT}█████▒▒▒▒▒ 50%...{RESET_TEXT}", end = "\r")
    time.sleep(sleeptime)
    print(f"Returning to menu {YELLOW_TEXT}██████▒▒▒▒ 60%...{RESET_TEXT}", end = "\r")
    time.sleep(sleeptime)
    print(f"Returning to menu {YELLOW_TEXT}███████▒▒▒ 70%...{RESET_TEXT}", end = "\r")
    time.sleep(sleeptime)
    print(f"Returning to menu {YELLOW_TEXT}████████▒▒ 80%...{RESET_TEXT}", end = "\r")
    time.sleep(sleeptime)
    print(f"Returning to menu {YELLOW_TEXT}█████████▒ 90%...{RESET_TEXT}", end = "\r")
    time.sleep(sleeptime)
    print(f"Returning to menu {YELLOW_TEXT}██████████ 100%...{RESET_TEXT}", end = "\r")
    time.sleep(1)

def startup():
    sleeptime = 0.2
    os.system('cls')
    loading2(RED_TEXT,WHITE_TEXT,0.01)
    time.sleep(sleeptime)
    os.system('cls')
    for x in range(3):
        loadingHearts(sleeptime)
    time.sleep(1)

def loadingHearts(sleeptime):
    loading2(WHITE_TEXT,RED_TEXT,0)
    time.sleep(sleeptime)
    os.system('cls')
    loading2(RED_TEXT,WHITE_TEXT,0)
    time.sleep(sleeptime)
    os.system('cls')
    loading2(WHITE_TEXT,RED_TEXT,0)
    time.sleep(sleeptime)
    os.system('cls')
    loading2(RED_TEXT,WHITE_TEXT,0)
    time.sleep(sleeptime)
    os.system('cls')

def loading2(color1,color2,timetick):
    print(f"{color2}___________________________________________________")
    print(f"{color2}________00000000000___________000000000000_________",end = '\r')
    time.sleep(timetick)
    print(f"{color2}________{color1}00000000000{color2}___________{color1}000000000000{color2}_________")
    time.sleep(timetick)
    print(f"____0000000_____________000______________00000_____",end = '\r')
    time.sleep(timetick)
    print(f"______{color1}00000000{color2}_____{color1}00000{color2}___{color1}000000{color2}_____{color1}0000000{color2}______")
    time.sleep(timetick)
    print(f"___0000000_______________0_________________0000____",end = '\r')
    time.sleep(timetick)
    print(f"____{color1}0000000{color2}_____________{color1}000{color2}______________{color1}00000{color2}_____")
    time.sleep(timetick)
    print(f"__000000____________________________________0000___",end = '\r')
    time.sleep(timetick)
    print(f"___{color1}0000000{color2}_______________{color1}0{color2}_________________{color1}0000{color2}____")
    time.sleep(timetick)
    print(f"__00000_____________________________________ 0000__",end = '\r')
    time.sleep(timetick)
    print(f"__{color1}000000{color2}____________________________________{color1}0000{color2}___")
    time.sleep(timetick)
    print(f"_00000______________________________________00000__",end = '\r')
    time.sleep(timetick)
    print(f"__{color1}00000{color2}_____________________________________ {color1}0000{color2}__")
    time.sleep(timetick)
    print(f"_00000_____________________________________000000__",end = '\r')
    time.sleep(timetick)
    print(f"_{color1}00000{color2}______ {color1}Denzel's Vending Machine{color2} ______{color1}00000{color2}__")
    time.sleep(timetick)
    print(f"__000000_________________________________0000000___",end = '\r')
    time.sleep(timetick)
    print(f"_{color1}00000{color2}_____________________________________{color1}000000{color2}__")
    time.sleep(timetick)
    print(f"___0000000______________________________0000000____",end = '\r')
    time.sleep(timetick)
    print(f"__{color1}000000{color2}_________________________________{color1}0000000{color2}___")
    time.sleep(timetick)
    print(f"_____000000____________________________000000______",end = '\r')
    time.sleep(timetick)
    print(f"___{color1}0000000{color2}______________________________{color1}0000000{color2}____")
    time.sleep(timetick)
    print(f"_______000000________________________000000________",end = '\r')
    time.sleep(timetick)
    print(f"_____{color1}000000{color2}____________________________{color1}000000{color2}______")
    time.sleep(timetick)
    print(f"__________00000_____________________0000___________",end = '\r')
    time.sleep(timetick)
    print(f"_______{color1}000000{color2}________________________{color1}000000{color2}________")
    time.sleep(timetick)
    print(f"_____________0000_________________0000_____________",end = '\r')
    time.sleep(timetick)
    print(f"__________{color1}00000{color2}_____________________{color1}0000{color2}___________")
    time.sleep(timetick)
    print(f"_______________0000_____________000________________",end = '\r')
    time.sleep(timetick)
    print(f"_____________{color1}0000{color2}_________________{color1}0000{color2}_____________")
    time.sleep(timetick)
    print(f"_________________000_________000___________________",end = '\r')
    time.sleep(timetick)
    print(f"_______________{color1}0000{color2}_____________{color1}000{color2}_______________")
    time.sleep(timetick)
    print(f"___________________000_____000_____________________",end = '\r')
    time.sleep(timetick)
    print(f"_________________{color1}000{color2}__________{color1}000{color2}__________________")
    time.sleep(timetick)
    print(f"______________________00__00_______________________",end = '\r')
    time.sleep(timetick)
    print(f"___________________{color1}000{color2}______{color1}000{color2}____________________")
    time.sleep(timetick)
    print(f"________________________00_________________________",end = '\r')
    time.sleep(timetick)
    print(f"______________________{color1}00{color2}__{color1}00{color2}_______________________")  
    time.sleep(timetick)  
    print(f"________________________{color1}00{color2}_________________________")
    print(f"___________________________________________________")


# Set Price Values and Stock numbers
priceStock(pRow1,row1)
priceStock(pRow2,row2)
priceStock(pRow3,row3)

# Collect User Input
os.system('cls')
startup()
while True:
    os.system('cls')
    print(f"{WHITE_TEXT}Version 1.3{RESET_TEXT}")
    vendingMachine()
    print(f"{WHITE_TEXT}{GREEN_TEXT}Insert/Add money{WHITE_TEXT} or {WHITE_TEXT}enter any {YELLOW_TEXT}NON-INTEGER{WHITE_TEXT} key to {RED_TEXT}quit{WHITE_TEXT}")
    while True:
        try:
            print(f"{WHITE_TEXT}Total Balance Left: {YELLOW_TEXT}{userBalance}${WHITE_TEXT}\n")
            checkIfDeposit = input(f"{MAGENTA_TEXT}Would you like to deposit? Click {GREEN_TEXT}ENTER{MAGENTA_TEXT} to continue or type {YELLOW_TEXT}YES{MAGENTA_TEXT} to add Balance or {RED_TEXT}NO{MAGENTA_TEXT} to quit : {CYAN_TEXT}")
            if checkIfDeposit.upper() == "YES":
                while True:
                    userBalanceInput = int(input(f"{WHITE_TEXT}Insert Money: {CYAN_TEXT}"))
                    if userBalanceInput <= 0:
                        print(f"{RED_TEXT}INVALID NUMBER!!{WHITE_TEXT}")
                        continue
                    else:
                        userBalance += userBalanceInput
                    break
                break
            if checkIfDeposit.upper() == "NO":
                print(f"{YELLOW_TEXT}Thank you for ordering!{WHITE_TEXT}")
                time.sleep(5)
                exit()
            if userBalance == 0:
                while True:
                    userBalanceInput = int(input(f"{RED_TEXT}Program will EXIT if no BALANCE is added!! : {CYAN_TEXT}"))
                    if userBalanceInput <= 0:
                        print(f"{YELLOW_TEXT}Thank you for ordering!{WHITE_TEXT}")
                        time.sleep(5)
                        exit()
                    else:
                        userBalance += userBalanceInput
                    if userBalance > 0:
                        break
                break
            if checkIfDeposit == "":
                break
            else:
                print(f"{WHITE_TEXT}{checkIfDeposit}{RED_TEXT} is an invalid input!!\n")
                continue
        except:
            print(f"{YELLOW_TEXT}Thank you for ordering!{WHITE_TEXT}")
            time.sleep(5)
            exit()
    if paidItems != "Default":
        print(f"{YELLOW_TEXT}Recomended items to buy from your previous purchase: {WHITE_TEXT}{recomended(paidItems)}.{RESET_TEXT}")
    userChoice = input(f"{WHITE_TEXT}What is your order?: {CYAN_TEXT}").upper()
    if rowChecker(userChoice) in row1.values():
        userInputChoice(row1,pRow1,rowChecker(userChoice))
    elif rowChecker(userChoice) in row2.values():
        userInputChoice(row2,pRow2,rowChecker(userChoice))
    elif rowChecker(userChoice) in row3.values():
        userInputChoice(row3,pRow3,rowChecker(userChoice))
    else:
        print(f"{WHITE_TEXT}{userChoice}{RED_TEXT} is an invalid input!!\n")
        while True:
            continueOrNot = input(f"{MAGENTA_TEXT}Would you like to continue?\n{WHITE_TEXT}Type {GREEN_TEXT}Yes{WHITE_TEXT} or {RED_TEXT}No:{CYAN_TEXT} ")
            if continueOrNot.upper() == "NO":
                print(f"{YELLOW_TEXT}Thank you for ordering!{WHITE_TEXT}")
                time.sleep(5)
                exit()
            elif continueOrNot.upper() == "YES":
                break
            else:
                print(f"{RED_TEXT}Type only Yes or No!!{WHITE_TEXT}")
                continue
