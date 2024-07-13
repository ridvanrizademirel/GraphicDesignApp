
import matplotlib.pyplot as plt
import numpy as np
xpointList =[]
yPointList =[]

try:
    coordTime = input("Enter coordination point :")
    coordLineColor = input("Chose coordination line color 'Red = r / Green = g / Blue = b / Cyan = c / Yellow = y' ")
    if coordLineColor == "r" or coordLineColor=="g" or coordLineColor=="b" or coordLineColor=="c" or coordLineColor=="y":
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

        xLabelName = input("Enter x coordination name :")
        yLabelName = input("Enter y coordination name :")
        graphicTitle = input("Enter graphic name :")

        font1 = {'family':'Times New Roman','color':'blue','size':18}
        font2 = {'family': 'Times New Roman', 'color': 'darkred', 'size': 15}

        plt.plot(xPoint,yPoint,color = f'{coordLineColor}')

        plt.title(str(graphicTitle),fontdict=font1)
        plt.xlabel(str(xLabelName),fontdict=font2)
        plt.ylabel(str(yLabelName),fontdict=font2)
        plt.show()
    else :
        print("İncorrect entry ")

except :
    print("Beware! Entered type is incorrect.")