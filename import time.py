import time

class Clock:
    def __init__(self, Hours, Minutes, Seconds, ClockType):
        self.Hours = int(Hours)
        self.Minutes = int(Minutes)
        self.Seconds = int(Seconds)
        self.ClockType = int(ClockType)

    def __str__(self):
        if(self.ClockType == 0):
            return("{:02}:{:02}:{:02}".format(self.Hours,self.Minutes,self.Seconds))
        if(self.ClockType == 1):
            if(self.Hours > 12):
                return("{:02}:{:02}:{:02} pm".format(self.Hours-12,self.Minutes,self.Seconds))
            else:
                return("{:02}:{:02}:{:02} am".format(self.Hours,self.Minutes,self.Seconds))
                

    def tick(self):
        self.Seconds += 1
        if(self.Seconds > 59):
            self.Seconds = 0
            self.Minutes += 1
        if(self.Minutes > 59):
            self.Minutes = 0
            self.Hours += 1
        if(self.Hours > 23):
            self.Hours = 0

clockInstance = Clock(2,16,15,0)
print(clockInstance)
clockInstance.tick()
print(clockInstance)

def ClockProgram():
    Hours = input("What is the current hour ==> ")
    Minutes = input("What is the current minute ==> ")
    Seconds = input("What is the current second ==> ")
    ClockType = input("What is the clock type ==> ")
    myClock = Clock(Hours, Minutes, Seconds, ClockType)
    while True:
        print(myClock)
        myClock.tick()
        time.sleep(1)

ClockProgram()
