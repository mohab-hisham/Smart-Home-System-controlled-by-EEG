import pyautogui as pg
import time
# print(pg.size())
# pg.moveTo(100, 100, duration = 1)
# time.sleep(10)
# pg.typewrite(["left","left","left", "space"],interval=5)


def navigate(gotoPos):
    global numOfMoves
    global currentPos

    if gotoPos > currentPos:
        numOfMoves = gotoPos - currentPos 
    elif currentPos > gotoPos:
        numOfMoves = (5-currentPos) + gotoPos +1
    else:
        numOfMoves = 0
    
    for i in range(numOfMoves):
        pg.typewrite(["right"],interval=0.5)
    # pg.typewrite(["space"])
    # pg.typewrite(["space"])
    # pg.typewrite(["right","right","right","right", "space"],interval=0.5)# to return to main menu

    currentPos = gotoPos


if __name__ == "__main__":

    
    homePosArr = ["LR","R1","R2","K","C","BR"]

    currentPos = 0
    currentTab = 0

    targetPos = 0

    numOfMoves = 0

    time.sleep(10)

    navigate(5)# bathroom
    # navigate(4,5)

    time.sleep(5)

    navigate(0) # living room
    # navigate(4,5)

    time.sleep(5)

    navigate(3) # kitchen
    # navigate(4,5)

    time.sleep(5)

    navigate(2) # Room2
     # navigate(4,5)