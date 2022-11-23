import rtde_control
# import rtde_receive
import time
import rtde_io

from rtde_control import RTDEControlInterface
import time

rtde_c = rtde_control.RTDEControlInterface("192.168.20.35")
rtde_io_ = rtde_io.RTDEIOInterface("192.168.20.35")

home = [4.71, -1.57, -1.57, -1.57, 1.57, 1]
pick = [4.71, -1.529, -1.816, -1.364, 1.57, 1]

#p
# pos00 = [5.303,-2.315,-0.699,-1.685,1.57,1.587]
# pos000 = [5.303,-2.307,-0.773,-1.614,1.57,1.587]

# pos01 = [5.085,-2.1858, -0.922,-1.59,1.57,1.37]
# pos001 = [5.085,-2.2, -0.978,-1.57,1.57,1.37]

# pos02 = [4.865,-2.2,-0.899,-1.6,1.57,1.15]
# pos002 = [4.865,-2.2,-0.934,-1.57,1.57,1.15]

# pos05 = [4.933,-1.8149,-1.48, -1.414,1.57,1.219]
# pos005 = [4.933,-1.828,-1.545,-1.336,1.57,1.219]

# pos04 = [5.195,-1.7968, -1.492,-1.41,1.57,1.482]
# pos004 = [5.195,-1.811,-1.563,-1.324,1.57,1.482]

# pos03 = [5.43,-1.913,-1.3379,-1.45,1.57,1.629]
# pos003 = [5.43,-1.913,-1.417,-1.357,1.57,1.629]

# pos08 = [5.004,-1.429,-1.888, -1.39,1.57,1.29]
# pos008 = [5.004,-1.436,-1.925,-1.3449,1.57,1.219]

# pos07 = [5.328,-1.425,-1.892, -1.39,1.57,1.61]
# pos007 = [5.328,-1.434,-1.9348,-1.3379,1.57,1.61]

# pos06 = [5.6,-1.58,-1.747, -1.379,1.57,1.89]
# pos006 = [5.6,-1.59,-1.79,-1.327,1.57,1.89]

#omz
pos00 = [4.865,-2.2,-0.899,-1.6,1.57,1.15]
pos000 = [4.865,-2.2,-0.934,-1.57,1.57,1.15]

pos01 = [4.933,-1.8149,-1.48, -1.414,1.57,1.219]
pos001 = [4.933,-1.828,-1.545,-1.336,1.57,1.219]

pos02 = [5.004,-1.429,-1.888, -1.39,1.57,1.29]
pos002 = [5.004,-1.436,-1.925,-1.3449,1.57,1.219]

pos03 = [5.085,-2.1858, -0.922,-1.59,1.57,1.37]
pos003 = [5.085,-2.2, -0.978,-1.57,1.57,1.37]

pos04 = [5.195,-1.7968, -1.492,-1.41,1.57,1.482]
pos004 = [5.195,-1.811,-1.563,-1.324,1.57,1.482]

pos05 = [5.328,-1.425,-1.892, -1.39,1.57,1.61]
pos005 = [5.328,-1.434,-1.9348,-1.3379,1.57,1.61]

pos06 = [5.303,-2.315,-0.699,-1.685,1.57,1.587]
pos006 = [5.303,-2.307,-0.773,-1.614,1.57,1.587]

pos07 = [5.43,-1.913,-1.3379,-1.45,1.57,1.629]
pos007 = [5.43,-1.913,-1.417,-1.357,1.57,1.629]

pos08 = [5.6,-1.58,-1.747, -1.379,1.57,1.89]
pos008 = [5.6,-1.59,-1.79,-1.327,1.57,1.89]

metrix = []
with open('E:/ur/omz/Ai.txt', 'w') as r:
    r.write('')
while True:
    with open('E:/ur/omz/Ai.txt', 'r') as r:
        dataText = r.read()
        if dataText == 'clear':
            metrix = []
            #pick o setting
            rtde_io_.setStandardDigitalOut(0,False)
            rtde_io_.setStandardDigitalOut(1,True)
            time.sleep(1)
            rtde_c.moveJ(home,0.5,1,asynchronous=False)
            print(metrix)

        if(dataText == "Robot00"):
            if 0 in metrix:
                pass
            else:
                #pick o setting
                rtde_io_.setStandardDigitalOut(0,False)
                rtde_io_.setStandardDigitalOut(1,True)
                time.sleep(1)
                rtde_c.moveJ(home,0.5,1,asynchronous=False)
                rtde_c.moveJ(pick,0.5,1,asynchronous=False)
                rtde_io_.setStandardDigitalOut(0,True)
                rtde_io_.setStandardDigitalOut(1,False)
                time.sleep(1)
                rtde_c.moveJ(home,0.5,1,asynchronous=False)
                #pick 0 setting
                time.sleep(1)
                rtde_c.moveJ(pos00,0.5,1,asynchronous=False)
                rtde_c.moveJ(pos000,0.5,1,asynchronous=False)
                rtde_io_.setStandardDigitalOut(0,False)
                rtde_io_.setStandardDigitalOut(1,True)
                time.sleep(1)
                rtde_c.moveJ(pos00,0.5,1,asynchronous=False)
                rtde_c.moveJ(home,0.5,1,asynchronous=False)
                metrix.append(0)
                print(metrix)
        elif(dataText == "Robot01"):
            if 1 in metrix:
                pass
            else:
                #pick o setting
                rtde_io_.setStandardDigitalOut(0,False)
                rtde_io_.setStandardDigitalOut(1,True)
                time.sleep(1)
                rtde_c.moveJ(home,0.5,1,asynchronous=False)
                rtde_c.moveJ(pick,0.5,1,asynchronous=False)
                rtde_io_.setStandardDigitalOut(0,True)
                rtde_io_.setStandardDigitalOut(1,False)
                time.sleep(1)
                rtde_c.moveJ(home,0.5,1,asynchronous=False)
                #pick 1 setting
                rtde_c.moveJ(pos01,0.5,1,asynchronous=False)
                rtde_c.moveJ(pos001,0.5,1,asynchronous=False)
                rtde_io_.setStandardDigitalOut(0,False)
                rtde_io_.setStandardDigitalOut(1,True)
                time.sleep(1)
                rtde_c.moveJ(pos01,0.5,1,asynchronous=False)
                rtde_c.moveJ(home,0.5,1,asynchronous=False)
                metrix.append(1)
                print(metrix)
        elif(dataText == "Robot02"):
            if 2 in metrix:
                pass
            else:
                #pick o setting
                rtde_io_.setStandardDigitalOut(0,False)
                rtde_io_.setStandardDigitalOut(1,True)
                time.sleep(1)
                rtde_c.moveJ(home,0.5,1,asynchronous=False)
                rtde_c.moveJ(pick,0.5,1,asynchronous=False)
                rtde_io_.setStandardDigitalOut(0,True)
                rtde_io_.setStandardDigitalOut(1,False)
                time.sleep(1)
                rtde_c.moveJ(home,0.5,1,asynchronous=False)
                #pick 1 setting
                rtde_c.moveJ(pos02,0.5,1,asynchronous=False)
                rtde_c.moveJ(pos002,0.5,1,asynchronous=False)
                rtde_io_.setStandardDigitalOut(0,False)
                rtde_io_.setStandardDigitalOut(1,True)
                time.sleep(1)
                rtde_c.moveJ(pos02,0.5,1,asynchronous=False)
                rtde_c.moveJ(home,0.5,1,asynchronous=False)
                metrix.append(2)
                print(metrix)
        elif(dataText == "Robot10"):
            if 3 in metrix:
                pass
            else:
                #pick o setting
                rtde_io_.setStandardDigitalOut(0,False)
                rtde_io_.setStandardDigitalOut(1,True)
                time.sleep(1)
                rtde_c.moveJ(home,0.5,1,asynchronous=False)
                rtde_c.moveJ(pick,0.5,1,asynchronous=False)
                rtde_io_.setStandardDigitalOut(0,True)
                rtde_io_.setStandardDigitalOut(1,False)
                time.sleep(1)
                rtde_c.moveJ(home,0.5,1,asynchronous=False)
                #pick 1 setting
                rtde_c.moveJ(pos03,0.5,1,asynchronous=False)
                rtde_c.moveJ(pos003,0.5,1,asynchronous=False)
                rtde_io_.setStandardDigitalOut(0,False)
                rtde_io_.setStandardDigitalOut(1,True)
                time.sleep(1)
                rtde_c.moveJ(pos03,0.5,1,asynchronous=False)
                rtde_c.moveJ(home,0.5,1,asynchronous=False)
                metrix.append(3)
                print(metrix)
        elif(dataText == "Robot11"):
            if 4 in metrix:
                pass
            else:
                #pick o setting
                rtde_io_.setStandardDigitalOut(0,False)
                rtde_io_.setStandardDigitalOut(1,True)
                time.sleep(1)
                rtde_c.moveJ(home,0.5,1,asynchronous=False)
                rtde_c.moveJ(pick,0.5,1,asynchronous=False)
                rtde_io_.setStandardDigitalOut(0,True)
                rtde_io_.setStandardDigitalOut(1,False)
                time.sleep(1)
                rtde_c.moveJ(home,0.5,1,asynchronous=False)
                #pick 1 setting
                rtde_c.moveJ(pos04,0.5,1,asynchronous=False)
                rtde_c.moveJ(pos004,0.5,1,asynchronous=False)
                rtde_io_.setStandardDigitalOut(0,False)
                rtde_io_.setStandardDigitalOut(1,True)
                time.sleep(1)
                rtde_c.moveJ(pos04,0.5,1,asynchronous=False)
                rtde_c.moveJ(home,0.5,1,asynchronous=False)
                metrix.append(4)
                print(metrix)
        elif(dataText == "Robot12"):
            if 5 in metrix:
                pass
            else:
                #pick o setting
                rtde_io_.setStandardDigitalOut(0,False)
                rtde_io_.setStandardDigitalOut(1,True)
                time.sleep(1)
                rtde_c.moveJ(home,0.5,1,asynchronous=False)
                rtde_c.moveJ(pick,0.5,1,asynchronous=False)
                rtde_io_.setStandardDigitalOut(0,True)
                rtde_io_.setStandardDigitalOut(1,False)
                time.sleep(1)
                rtde_c.moveJ(home,0.5,1,asynchronous=False)
                #pick 1 setting
                rtde_c.moveJ(pos05,0.5,1,asynchronous=False)
                rtde_c.moveJ(pos005,0.5,1,asynchronous=False)
                rtde_io_.setStandardDigitalOut(0,False)
                rtde_io_.setStandardDigitalOut(1,True)
                time.sleep(1)
                rtde_c.moveJ(pos05,0.5,1,asynchronous=False)
                rtde_c.moveJ(home,0.5,1,asynchronous=False)
                metrix.append(5)
                print(metrix)
        elif(dataText == "Robot20"):
            if 6 in metrix:
                pass
            else:
                #pick o setting
                rtde_io_.setStandardDigitalOut(0,False)
                rtde_io_.setStandardDigitalOut(1,True)
                time.sleep(1)
                rtde_c.moveJ(home,0.5,1,asynchronous=False)
                rtde_c.moveJ(pick,0.5,1,asynchronous=False)
                rtde_io_.setStandardDigitalOut(0,True)
                rtde_io_.setStandardDigitalOut(1,False)
                time.sleep(1)
                rtde_c.moveJ(home,0.5,1,asynchronous=False)
                #pick 1 setting
                rtde_c.moveJ(pos06,0.5,1,asynchronous=False)
                rtde_c.moveJ(pos006,0.5,1,asynchronous=False)
                rtde_io_.setStandardDigitalOut(0,False)
                rtde_io_.setStandardDigitalOut(1,True)
                time.sleep(1)
                rtde_c.moveJ(pos06,0.5,1,asynchronous=False)
                rtde_c.moveJ(home,0.5,1,asynchronous=False)
                metrix.append(6)
                print(metrix)
        elif(dataText == "Robot21"):
            if 7 in metrix:
                pass
            else:
                #pick o setting
                rtde_io_.setStandardDigitalOut(0,False)
                rtde_io_.setStandardDigitalOut(1,True)
                time.sleep(1)
                rtde_c.moveJ(home,0.5,1,asynchronous=False)
                rtde_c.moveJ(pick,0.5,1,asynchronous=False)
                rtde_io_.setStandardDigitalOut(0,True)
                rtde_io_.setStandardDigitalOut(1,False)
                time.sleep(1)
                rtde_c.moveJ(home,0.5,1,asynchronous=False)
                #pick 1 setting
                rtde_c.moveJ(pos07,0.5,1,asynchronous=False)
                rtde_c.moveJ(pos007,0.5,1,asynchronous=False)
                rtde_io_.setStandardDigitalOut(0,False)
                rtde_io_.setStandardDigitalOut(1,True)
                time.sleep(1)
                rtde_c.moveJ(pos07,0.5,1,asynchronous=False)
                rtde_c.moveJ(home,0.5,1,asynchronous=False)
                metrix.append(7)
                print(metrix)
        elif(dataText == "Robot22"):
            if 8 in metrix:
                pass
            else:
                #pick o setting
                rtde_io_.setStandardDigitalOut(0,False)
                rtde_io_.setStandardDigitalOut(1,True)
                time.sleep(1)
                rtde_c.moveJ(home,0.5,1,asynchronous=False)
                rtde_c.moveJ(pick,0.5,1,asynchronous=False)
                rtde_io_.setStandardDigitalOut(0,True)
                rtde_io_.setStandardDigitalOut(1,False)
                time.sleep(1)
                rtde_c.moveJ(home,0.5,1,asynchronous=False)
                #pick 1 setting
                rtde_c.moveJ(pos08,0.5,1,asynchronous=False)
                rtde_c.moveJ(pos008,0.5,1,asynchronous=False)
                rtde_io_.setStandardDigitalOut(0,False)
                rtde_io_.setStandardDigitalOut(1,True)
                time.sleep(1)
                rtde_c.moveJ(pos08,0.5,1,asynchronous=False)
                rtde_c.moveJ(home,0.5,1,asynchronous=False)
                metrix.append(8)
                print(metrix)              
