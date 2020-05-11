# -*- coding: utf-8 -*-

import xml.etree.ElementTree as et
import matplotlib.pyplot as plt
import os
import sys
import math
import matplotlib
# matplotlib.use('Agg')

def calcDist(mX, mY, mZ, nX, nY, nZ, value, tide):
    # print("Dist Check", len(mX))
    for i in range (0, len(mX)):
        dist = math.sqrt(math.pow(mX[i] - nX, 2) + math.pow(mY[i] - nY, 2) + math.pow(mZ[i] - nZ, 2))
        # print("Tide", tide, "Dist", round(dist))
        if dist <= value:
            return False
    return True

def loadPos(xml, xpath, id, type):
    x = [[[], [], []], [[], [], []], [[], [], []]]
    y = [[[], [], []], [[], [], []], [[], [], []]]
    z = [[[], [], []], [[], [], []], [[], [], []]]
    b = [[0] * 3, [0] * 3]
    #Ikura Bank
    for tree in xml.findall("./C1/C0/[@Name='Objs']/C1/A0/[@StringValue='Obj_CoopIkuraBank']/.."):
        pos = tree.findall("./C1/[@Name='Translate']/")
        layer = tree.find("./A0/[@Name='LayerConfigName']")
        mX = float(pos[0].attrib["StringValue"])
        mY = float(pos[2].attrib["StringValue"])
        mZ = float(pos[1].attrib["StringValue"])
        if layer.attrib["StringValue"] == "CoopWater_0":
            b[0][0] = mX
            b[0][1] = mY
            b[0][2] = mZ
        if layer.attrib["StringValue"] == "Cmn":
            b[1][0] = mX
            b[1][1] = mY
            b[1][2] = mZ
    for tree in xml.findall("./C1/C0/[@Name='Objs']/C1/A0/[@StringValue='Obj_CoopIkuraBankBase']/.."):
        pos = tree.findall("./C1/[@Name='Translate']/")
        layer = tree.find("./A0/[@Name='LayerConfigName']")
        mX = float(pos[0].attrib["StringValue"])
        mY = float(pos[2].attrib["StringValue"])
        mZ = float(pos[1].attrib["StringValue"])
        plt.scatter(mX, mY, c="black", marker="s")

    # Load XML All Lines
    for tree in xml.findall("./C1/C0/C1/A0/[@StringValue='%s']/.." % xpath):
        pos = tree.findall("./C1/[@Name='Translate']/")
        layer = tree.find("./A0/[@Name='LayerConfigName']")
        mX = float(pos[0].attrib["StringValue"])
        mY = float(pos[2].attrib["StringValue"])
        mZ = float(pos[1].attrib["StringValue"])
        
        # Geyser
        if xpath == "Obj_CoopSpawnGeyser":
            if layer.attrib["StringValue"][:9] != "CoopWater":
                continue
            i = int(layer.attrib["StringValue"][-1])
            dist = math.sqrt(math.pow(b[1][0] - mX, 2) + math.pow(b[1][1] - mY, 2) + math.pow(b[1][2] - mZ, 2))
            if dist <= 450:
                x[i][0].append(mX)
                y[i][0].append(mY)
                z[i][0].append(mZ)
            else:
                print("Geyser Point is too far from IkuraBank.")
                layer.set("StringValue", "Tmp")
            continue
        # Drizzler
        if xpath == "Obj_CoopJumpPointEnemyRocket":
            if layer.attrib["StringValue"][:9] != "CoopWater":
                continue
            i = int(layer.attrib["StringValue"][-1])
            if calcDist(x[i][0], y[i][0], z[i][0], mX, mY, mZ, 200, i):
                x[i][0].append(mX)
                y[i][0].append(mY)
                z[i][0].append(mZ)
            else:
                print("Drizzler Point is too close.")
                layer.set("StringValue", "Tmp")
            continue
        # Tower Flyfish Salmonids
        if (xpath[-2:] == "_1") or (xpath[-2:] == "_2") or (xpath[-2:] == "_3"):
            i = int(layer.attrib["StringValue"][-1])
            j = int(xpath[-1]) - 1
            x[i][j].append(mX)
            y[i][j].append(mY)
            z[i][j].append(mZ)
            continue
        # Otherwise
        if pos == None:
            continue
        # print(xpath, layer.attrib["StringValue"])

        if layer.attrib["StringValue"][:9] == "CoopWater" or layer.attrib["StringValue"] == "Cmn":
            if layer.attrib["StringValue"][:9] == "CoopWater":
                i = int(layer.attrib["StringValue"][-1])
            else:
                i = 0
            x[i][0].append(mX)
            y[i][0].append(mY)
            z[i][0].append(mZ)
    if (xpath[-2:] == "_1") or (xpath[-2:] == "_2") or (xpath[-2:] == "_3"):
        i = int(xpath[-1]) - 1
        j = int(layer.attrib["StringValue"][-1])
    # print(xpath, "Size", len(x[0][0]), len(x[1][0]), len(x[2][0]))
    plt.xlim([700, -960])
    # plt.xlim([-960, 700])
    plt.ylim([-700, 700])

    if "Point" in xpath or "Geyser" in xpath:
        for i in range (0, len(x[0])):
            # print(xpath, b[0], x[0][i], y[0][i], z[0][i])
            for j in range (0, len(x[0][i])): # Low Tide
                dist = math.sqrt(math.pow((b[0][0] - x[0][i][j]), 2) +  math.pow((b[0][1] - y[0][i][j]), 2) + math.pow((b[0][2] - z[0][i][j]), 2))
                plt.annotate(round(dist), (x[0][i][j], y[0][i][j]), color="black")
        for i in range (0, len(x[1])): # Middle Tide
            for j in range (0, len(x[1][i])):
                dist = math.sqrt(math.pow((b[1][0] - x[1][i][j]), 2) +  math.pow((b[1][1] - y[1][i][j]), 2) + math.pow((b[1][2] - z[1][i][j]), 2))
                if xpath != "Obj_CoopJumpPointEnemyRocket":
                    plt.annotate(round(dist), (x[1][i][j], y[1][i][j]), color="black")
        for i in range (0, len(x[2])): # High Tide
            for j in range (0, len(x[2][i])):
                dist = math.sqrt(math.pow((b[1][0] - x[2][i][j]), 2) +  math.pow((b[1][1] - y[2][i][j]), 2) + math.pow((b[1][2] - z[2][i][j]), 2))
                if xpath != "Obj_CoopJumpPointEnemyRocket":
                    plt.annotate(round(dist), (x[2][i][j], y[2][i][j]), color="black")

    # plt.axes().set_aspect('equal', 'datalim')
    plt.scatter(x[0][0], y[0][0], c="red", marker="o")
    plt.scatter(x[0][1], y[0][1], c="red", marker="^")
    plt.scatter(x[0][2], y[0][2], c="red", marker="D")
    plt.scatter(x[1][0], y[1][0], c="blue", marker="o")
    plt.scatter(x[1][1], y[1][1], c="blue", marker="^")
    plt.scatter(x[1][2], y[1][2], c="blue", marker="D")
    plt.scatter(x[2][0], y[2][0], c="yellow", marker="o")
    plt.scatter(x[2][1], y[2][1], c="yellow", marker="^")
    plt.scatter(x[2][2], y[2][2], c="yellow", marker="D")
    if (xpath[-2:] != "_1") and (xpath[-2:] != "_2"):
        # plt.legend()
        plt.tick_params(labelbottom=False,
                    labelleft=False,
                    labelright=False,
                    labeltop=False)
        plt.savefig(str(id) + "_mod_" + xpath +".png", dpi=150, transparent=False, bbox_inches="tight", pad_inches=0.0)
        plt.close()

if __name__ == "__main__":
    print("0: Disable Far Object\n")
    print("Input the number :")
    # id = input()
    for id in range(0, 5):
        xmlp = et.XMLParser(encoding="utf-8")
        xml = et.parse("./xml/" + str(id) + ".xml", parser=xmlp)
        config = []
        sum = 0
        for obj in xml.findall("./C1/C0/C1/A0/[@Name='UnitConfigName']"):
            config.append(obj.attrib["StringValue"])
        config = sorted(list(set(config)))
        for xpath in config:
            print("Object Name:", xpath)
            param = xml.findall("./C1/C0/C1/A0/[@StringValue='%s']/.." % xpath)
            sum += len(param)
            # print(xpath, len(param))
            loadPos(xml, xpath, id, 0)
        if id == 0:
            name = "Fld_Shakeup00_Cop.byaml"
        if id == 1:
            name = "Fld_Shakeship00_Cop.byaml"
        if id == 2:
            name = "Fld_Shakehouse00_Cop.byaml"
        if id == 3:
            name = "Fld_Shakelift00_Cop.byaml"
        if id == 4:
            name = "Fld_Shakeride00_Cop.byaml"

        xml.write("./mod/" + name + ".xml")
        print("UnitConfigName", sum)