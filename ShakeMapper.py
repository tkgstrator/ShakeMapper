# -*- coding: utf-8 -*-

import xml.etree.ElementTree as et
import matplotlib.pyplot as plt
import os
import sys
import math
import matplotlib
# matplotlib.use('Agg')

def loadPos(xml, xpath, id):
    x = [[[], [], []], [[], [], []], [[], [], []]]
    y = [[[], [], []], [[], [], []], [[], [], []]]
    z = [[[], [], []], [[], [], []], [[], [], []]]
    b = [[0] * 3, [0] * 3]
    d = [[[], [], []], [[], [], []], [[], [], []]]
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
        plt.scatter(mX, mY, c="black", marker="s")
    for tree in xml.findall("./C1/C0/C1/A0/[@StringValue='%s']/.." % xpath):
        pos = tree.findall("./C1/[@Name='Translate']/")
        layer = tree.find("./A0/[@Name='LayerConfigName']")
        mX = float(pos[0].attrib["StringValue"])
        mY = float(pos[2].attrib["StringValue"])
        mZ = float(pos[1].attrib["StringValue"])

        # Drizzler
        if xpath == "Obj_CoopJumpPointEnemyRocket":
            # if tree.find("./D0/[@Name='IsLinkDest']").attrib["StringValue"] == "False":
            #     continue
            if layer.attrib["StringValue"][:9] != "CoopWater":
                print(layer.attrib["StringValue"][:9])
                continue
            i = int(layer.attrib["StringValue"][-1])
            x[i][0].append(mX)
            y[i][0].append(mY)
            z[i][0].append(mZ)
            continue
        # Tower Flyfish Salmonids
        if (xpath[-2:] == "_1") or (xpath[-2:] == "_2") or (xpath[-2:] == "_3"):
            i = int(layer.attrib["StringValue"][-1])
            j = int(xpath[-1]) - 1
            x[i][j].append(mX)
            y[i][j].append(mY)
            z[i][j].append(mY)
            continue
        # Otherwise
        # print(xpath, layer.attrib["StringValue"])

        # if layer.attrib["StringValue"] != "CoopWater":
        #     continue
        #     i = int(layer.attrib["StringValue"][-1])
        #     x[i][0].append(mX)
        #     y[i][0].append(mY)
        #     z[i][0].append(mZ)
        
    if (xpath[-2:] == "_1") or (xpath[-2:] == "_2") or (xpath[-2:] == "_3"):
        i = int(xpath[-1]) - 1
        j = int(layer.attrib["StringValue"][-1])
    # print(xpath, "Size", len(x[0][0]), len(x[1][0]), len(x[2][0]))
    plt.xlim([700, -960])
    plt.ylim([-600, 500])


    if "Point" in xpath:
        for i in range (0, len(x[0])):
            for j in range (0, len(x[0][i])):
                dist = math.sqrt(math.pow((b[0][0] - x[0][i][j]), 2) +  math.pow((b[0][1] - y[0][i][j]), 2) + math.pow((b[0][2] - z[0][i][j]), 2))
                plt.annotate(round(dist), (x[0][i][j], y[0][i][j]), color="black")
        for i in range (0, len(x[1])):
            for j in range (0, len(x[1][i])):
                dist = math.sqrt(math.pow((b[1][0] - x[1][i][j]), 2) +  math.pow((b[1][1] - y[1][i][j]), 2) + math.pow((b[1][2] - z[1][i][j]), 2))
                plt.annotate(round(dist), (x[1][i][j], y[1][i][j]), color="black")
        for i in range (0, len(x[2])):
            for j in range (0, len(x[2][i])):
                dist = math.sqrt(math.pow((b[1][0] - x[2][i][j]), 2) +  math.pow((b[1][1] - y[2][i][j]), 2) + math.pow((b[1][2] - z[2][i][j]), 2))
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
        plt.savefig(str(id) + "_" + xpath +".png", dpi=300)
        plt.close()

if __name__ == "__main__":
    print("0: Spawning Grounds(Shakeup)\n1: Marooner's Bay(Shakeship)\n2: Lost Outpost(Shakehouse)\n3: Salmonid Smokeyard(Shakelift)\n4: Ruins of Ark Polaris(Shakeride)\n5: All\nInput the key :")
    id = input()
    if id == "5":
        for id in range(0, 5):
            xmlp = et.XMLParser(encoding="utf-8")
            xml = et.parse("./xml/" + str(id) + ".xml", parser=xmlp)
            if id == 3:
                config = []
                sum = 0
                for obj in xml.findall("./C1/C0/C1/A0/[@Name='UnitConfigName']"):
                    config.append(obj.attrib["StringValue"])
                config = sorted(list(set(config)))
                for xpath in config:
                    param = xml.findall("./C1/C0/C1/A0/[@StringValue='%s']/.." % xpath)
                    sum += len(param)
                    # print(xpath, len(param))
                    loadPos(xml, xpath, id)
                print("UnitConfigName", sum)
        exit(0)
    print("0: Zako SpawnPoint\n1: Boss SpawnPoint\n2: Tower ArrivalPoint\n3: Drizzler JumpPoint\n4: Flyfish ArrivalPoint\n5: All\nInput tht key :")
    type = input()
    print("0: Transparent\n1: None\nInput tht key :")
    alpha = input()
    xmlp = et.XMLParser(encoding="utf-8")
    xml = et.parse("./xml/" + str(id) + ".xml", parser=xmlp)
    loadPos(xml, type, id, alpha)
    # plt.tick_params(labelbottom=False,
    #                 labelleft=False,
    #                 labelright=False,
    #                 labeltop=False)