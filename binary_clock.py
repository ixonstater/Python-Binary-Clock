
from graphics import *
import time
import sys
from datetime import datetime
from threading import Timer
class Clock:
    win = ""
    circles = []
    currentHour = 0
    currentMin = 0
    def makeClock():
        win=GraphWin('Binary Clock', 240, 160)
        win.setBackground('white')
        for i in range(0,32):
            if i < 2:
                Clock.circles.append(Circle(Point(20,140-i*40),20))
                Clock.circles[i].draw(win)
            elif i >=2 and i < 6:
                Clock.circles.append(Circle(Point(60,140-(i-2)*40),20))
                Clock.circles[i].draw(win)
            elif i >=6 and i < 9:
                Clock.circles.append(Circle(Point(100,140-(i-6)*40),20))
                Clock.circles[i].draw(win)
            elif i >= 9 and i < 13:
                Clock.circles.append(Circle(Point(140,140-(i-9)*40),20))
                Clock.circles[i].draw(win)
            elif i >= 13 and i < 16:
                Clock.circles.append(Circle(Point(180,140-(i-13)*40),20))
                Clock.circles[i].draw(win)
            elif i >= 16 and i < 20:
                Clock.circles.append(Circle(Point(220,140-(i-16)*40),20))
                Clock.circles[i].draw(win)
            
    def getTime():
        currentTime = str(datetime.now().time())
        currentTime = currentTime.split(':')
        currentTime[2] = int(float(currentTime[2]))
        currentTime[1] = int(currentTime[1])
        currentTime[0] = int (currentTime[0])
        return(currentTime)
        
    def makeTimer(args):
        startTime = time.time()
        Clock.makeClock()
        while True:
            Clock.updateClock(Clock.getTime(),Clock.circles)
            time.sleep(1.0)
            
    def updateClock(time,circles):
        #Seconds
        secTens = time[2]//10
        secOnes = time[2]%10
        if secOnes == 0:
            circles[19].setFill('white')
            circles[18].setFill('white')
            circles[17].setFill('white')
            circles[16].setFill('white')
        elif secOnes == 1 or secOnes == 3 or secOnes == 5 or secOnes == 7 or secOnes == 9:
            circles[19].setFill('blue')
        elif secOnes == 2:
            circles[19].setFill('white')
            circles[18].setFill('blue')
        elif secOnes == 4:
            circles[19].setFill('white')
            circles[18].setFill('white')
            circles[17].setFill('blue')
        elif secOnes == 6:
            circles[19].setFill('white')
            circles[18].setFill('blue')
        elif secOnes == 8:
            circles[19].setFill('white')
            circles[18].setFill('white')
            circles[17].setFill('white')
            circles[16].setFill('blue')
        if secTens == 0:
            circles[15].setFill('white')
            circles[14].setFill('white')
            circles[13].setFill('white')
        elif secTens == 1 or secTens == 3 or secTens == 5:
            circles[15].setFill('blue')
        elif secTens == 2:
            circles[15].setFill('white')
            circles[14].setFill('blue')
        elif secTens == 4:
            circles[15].setFill('white')
            circles[14].setFill('white')
            circles[13].setFill('blue')
        #Minutes
        if time[1] != Clock.currentMin:
            Clock.currentMin = time[1]
            minTens = time[1]//10
            minOnes = time[1]%10
            if minOnes == 0:
                circles[12].setFill('white')
                circles[11].setFill('white')
                circles[10].setFill('white')
                circles[9].setFill('white')
            elif minOnes == 1:
                circles[12].setFill('blue')
            elif minOnes == 2:
                circles[12].setFill('white')
                circles[11].setFill('blue')
            elif minOnes == 3:
                circles[12].setFill('blue')
                circles[11].setFill('blue')
            elif minOnes == 4:
                circles[12].setFill('white')
                circles[11].setFill('white')
                circles[10].setFill('blue')
            elif minOnes == 5:
                circles[12].setFill('blue')
                circles[10].setFill('blue')
            elif minOnes == 6:
                circles[12].setFill('white')
                circles[11].setFill('blue')
                circles[10].setFill('blue')
            elif minOnes == 7:
                circles[12].setFill('blue')
                circles[11].setFill('blue')
                circles[10].setFill('blue')
            elif minOnes == 8:
                circles[12].setFill('white')
                circles[11].setFill('white')
                circles[10].setFill('white')
                circles[9].setFill('blue')
            elif minOnes == 9:
                circles[12].setFill('blue')
                circles[9].setFill('blue')
            if minTens == 0:
                circles[8].setFill('white')
                circles[7].setFill('white')
                circles[6].setFill('white')
            elif minTens == 1:
                circles[8].setFill('blue')
            elif minTens == 2:
                circles[8].setFill('white')
                circles[7].setFill('blue')
            elif minTens == 3:
                circles[8].setFill('blue')
                circles[6].setFill('blue')
            elif minTens == 4:
                circles[8].setFill('white')
                circles[7].setFill('white')
                circles[6].setFill('blue')
            elif minTens == 5:
                circles[8].setFill('blue')
                circles[7].setFill('white')
                circles[6].setFill('blue')
        #Hours
        if time[0] != Clock.currentHour:
            Clock.currentHour = time[0]
            hourTens = time[0]//10
            hourOnes = time[0]%10
            if hourOnes == 0:
                circles[5].setFill('white')
                circles[4].setFill('white')
                circles[3].setFill('white')
                circles[2].setFill('white')
            elif hourOnes == 1:
                circles[5].setFill('blue')
            elif hourOnes == 2:
                circles[5].setFill('white')
                circles[4].setFill('blue')
            elif hourOnes == 3:
                circles[5].setFill('blue')
                circles[4].setFill('blue')
            elif hourOnes == 4:
                circles[5].setFill('white')
                circles[4].setFill('white')
                circles[3].setFill('blue')
            elif hourOnes == 5:
                circles[5].setFill('blue')
                circles[3].setFill('blue')
            elif hourOnes == 6:
                circles[5].setFill('white')
                circles[4].setFill('blue')
                circles[3].setFill('blue')
            elif hourOnes == 7:
                circles[5].setFill('blue')
                circles[4].setFill('blue')
                circles[3].setFill('blue')
            elif hourOnes == 8:
                circles[5].setFill('white')
                circles[4].setFill('white')
                circles[3].setFill('white')
                circles[2].setFill('blue')
            elif hourOnes == 9:
                circles[5].setFill('blue')
                circles[2].setFill('blue')
            if hourTens == 0:
                circles[1].setFill('white')
                circles[0].setFill('white')
            elif hourTens == 1:
                circles[1].setFill('blue')
            elif hourTens == 2:
                circles[1].setFill('white')
                circles[0].setFill('blue')
    
def main():
    myClock = Clock()
    myClock.makeTimer()
main()
