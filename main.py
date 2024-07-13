
import matplotlib.pyplot as plt
import numpy as np
xpointList =[]
yPointList =[]

try:
    coordTime = input("Enter coordination point :")
    coordLineColor = input("Chose coordination line color 'Red = r / Green = g / Blue = b / Cyan = c / Yellow = y' ")
    x = 1
    while x<=int(coordTime) :
        xp = input("Enter x coordination :")
        xpointList.append(int(xp))
        x+=1
    x = 1
    while x<=int(coordTime) :
        yp = input("Enter y coordination :")
        yPointList.append(int(yp))
        x+=1
    xPoint = np.array(xpointList)
    yPoint = np.array(yPointList)

    plt.plot(xPoint,yPoint,color = f'{coordLineColor}')
    plt.show()
except :
    print("Beware! Entered type is incorrect.")