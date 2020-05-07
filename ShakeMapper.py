# -*- coding: utf-8 -*-

import xml.etree.ElementTree as et
import matplotlib.pyplot as plt
import os
import sys
import matplotlib
# matplotlib.use('Agg')

def loadPos(xml, type, id, alpha):
    x = [[], [], []]
    y = [[], [], []]
    if str(type) == "0":
        name = "Salmonids"
        for tree in xml.findall("./C1/C0/[@Name='Objs']/C1/A0/[@StringValue='Obj_CoopSpawnPointZako_1']/.."):
            pos = tree.findall("./C1/[@Name='Translate']/")
            layer = tree.find("./A0/[@Name='LayerConfigName']")
            mX = float(pos[0].attrib["StringValue"])
            mY = float(pos[2].attrib["StringValue"])
            if layer.attrib["StringValue"] == "CoopWater_0":
                x[0].append(mX)
                y[0].append(mY)
            if layer.attrib["StringValue"] == "CoopWater_1":
                x[1].append(mX)
                y[1].append(mY)
            if layer.attrib["StringValue"] == "CoopWater_2":
                x[2].append(mX)
                y[2].append(mY)
        for tree in xml.findall("./C1/C0/[@Name='Objs']/C1/A0/[@StringValue='Obj_CoopSpawnPointZako_2']/.."):
            pos = tree.findall("./C1/[@Name='Translate']/")
            layer = tree.find("./A0/[@Name='LayerConfigName']")
            mX = float(pos[0].attrib["StringValue"])
            mY = float(pos[2].attrib["StringValue"])
            if layer.attrib["StringValue"] == "CoopWater_0":
                x[0].append(mX)
                y[0].append(mY)
            if layer.attrib["StringValue"] == "CoopWater_1":
                x[1].append(mX)
                y[1].append(mY)
            if layer.attrib["StringValue"] == "CoopWater_2":
                x[2].append(mX)
                y[2].append(mY)
        for tree in xml.findall("./C1/C0/[@Name='Objs']/C1/A0/[@StringValue='Obj_CoopSpawnPointZako_3']/.."):
            pos = tree.findall("./C1/[@Name='Translate']/")
            mX = float(pos[0].attrib["StringValue"])
            mY = float(pos[2].attrib["StringValue"])
            if layer.attrib["StringValue"] == "CoopWater_0":
                x[0].append(mX)
                y[0].append(mY)
            if layer.attrib["StringValue"] == "CoopWater_1":
                x[1].append(mX)
                y[1].append(mY)
            if layer.attrib["StringValue"] == "CoopWater_2":
                x[2].append(mX)
                y[2].append(mY)
    if str(type) == "1":
        name = "Boss"
        for tree in xml.findall("./C1/C0/[@Name='Objs']/C1/A0/[@StringValue='Obj_CoopSpawnPointBoss']/.."):
            pos = tree.findall("./C1/[@Name='Translate']/")
            layer = tree.find("./A0/[@Name='LayerConfigName']")
            mX = float(pos[0].attrib["StringValue"])
            mY = float(pos[2].attrib["StringValue"])
            if layer.attrib["StringValue"] == "CoopWater_0":
                x[0].append(mX)
                y[0].append(mY)
            if layer.attrib["StringValue"] == "CoopWater_1":
                x[1].append(mX)
                y[1].append(mY)
            if layer.attrib["StringValue"] == "CoopWater_2":
                x[2].append(mX)
                y[2].append(mY)
    if str(type) == "2":
        name = "Tower"
        for tree in xml.findall("./C1/C0/[@Name='Objs']/C1/A0/[@StringValue='Obj_CoopArrivalPointEnemyTower_1']/.."):
            pos = tree.findall("./C1/[@Name='Translate']/")
            layer = tree.find("./A0/[@Name='LayerConfigName']")
            mX = float(pos[0].attrib["StringValue"])
            mY = float(pos[2].attrib["StringValue"])
            if layer.attrib["StringValue"] == "CoopWater_0":
                x[0].append(mX)
                y[0].append(mY)
            if layer.attrib["StringValue"] == "CoopWater_1":
                x[1].append(mX)
                y[1].append(mY)
            if layer.attrib["StringValue"] == "CoopWater_2":
                x[2].append(mX)
                y[2].append(mY)
        for tree in xml.findall("./C1/C0/[@Name='Objs']/C1/A0/[@StringValue='Obj_CoopArrivalPointEnemyTower_2']/.."):
            pos = tree.findall("./C1/[@Name='Translate']/")
            layer = tree.find("./A0/[@Name='LayerConfigName']")
            mX = float(pos[0].attrib["StringValue"])
            mY = float(pos[2].attrib["StringValue"])
            if layer.attrib["StringValue"] == "CoopWater_0":
                x[0].append(mX)
                y[0].append(mY)
            if layer.attrib["StringValue"] == "CoopWater_1":
                x[1].append(mX)
                y[1].append(mY)
            if layer.attrib["StringValue"] == "CoopWater_2":
                x[2].append(mX)
                y[2].append(mY)
        for tree in xml.findall("./C1/C0/[@Name='Objs']/C1/A0/[@StringValue='Obj_CoopArrivalPointEnemyTower_3']/.."):
            pos = tree.findall("./C1/[@Name='Translate']/")
            layer = tree.find("./A0/[@Name='LayerConfigName']")
            mX = float(pos[0].attrib["StringValue"])
            mY = float(pos[2].attrib["StringValue"])
            if layer.attrib["StringValue"] == "CoopWater_0":
                x[0].append(mX)
                y[0].append(mY)
            if layer.attrib["StringValue"] == "CoopWater_1":
                x[1].append(mX)
                y[1].append(mY)
            if layer.attrib["StringValue"] == "CoopWater_2":
                x[2].append(mX)
                y[2].append(mY)
    if str(type) == "3":
        name = "Drizzler"
        for tree in xml.findall("./C1/C0/[@Name='Objs']/C1/A0/[@StringValue='Obj_CoopJumpPointEnemyRocket']/.."):
            pos = tree.findall("./C1/[@Name='Translate']/")
            layer = tree.find("./A0/[@Name='LayerConfigName']")
            mX = float(pos[0].attrib["StringValue"])
            mY = float(pos[2].attrib["StringValue"])
            if layer.attrib["StringValue"] == "CoopWater_0":
                x[0].append(mX)
                y[0].append(mY)
            if layer.attrib["StringValue"] == "CoopWater_1":
                x[1].append(mX)
                y[1].append(mY)
            if layer.attrib["StringValue"] == "CoopWater_2":
                x[2].append(mX)
                y[2].append(mY)
    if str(type) == "4":
        name = "Flyfish"
        for tree in xml.findall("./C1/C0/[@Name='Objs']/C1/A0/[@StringValue='Obj_CoopArrivalPointEnemyCup_1']/.."):
            pos = tree.findall("./C1/[@Name='Translate']/")
            layer = tree.find("./A0/[@Name='LayerConfigName']")
            mX = float(pos[0].attrib["StringValue"])
            mY = float(pos[2].attrib["StringValue"])
            if layer.attrib["StringValue"] == "CoopWater_0":
                x[0].append(mX)
                y[0].append(mY)
            if layer.attrib["StringValue"] == "CoopWater_1":
                x[1].append(mX)
                y[1].append(mY)
            if layer.attrib["StringValue"] == "CoopWater_2":
                x[2].append(mX)
                y[2].append(mY)
        for tree in xml.findall("./C1/C0/[@Name='Objs']/C1/A0/[@StringValue='Obj_CoopArrivalPointEnemyCup_2']/.."):
            pos = tree.findall("./C1/[@Name='Translate']/")
            layer = tree.find("./A0/[@Name='LayerConfigName']")
            mX = float(pos[0].attrib["StringValue"])
            mY = float(pos[2].attrib["StringValue"])
            if layer.attrib["StringValue"] == "CoopWater_0":
                x[0].append(mX)
                y[0].append(mY)
            if layer.attrib["StringValue"] == "CoopWater_1":
                x[1].append(mX)
                y[1].append(mY)
            if layer.attrib["StringValue"] == "CoopWater_2":
                x[2].append(mX)
                y[2].append(mY)
        for tree in xml.findall("./C1/C0/[@Name='Objs']/C1/A0/[@StringValue='Obj_CoopArrivalPointEnemyCup_3']/.."):
            pos = tree.findall("./C1/[@Name='Translate']/")
            layer = tree.find("./A0/[@Name='LayerConfigName']")
            mX = float(pos[0].attrib["StringValue"])
            mY = float(pos[2].attrib["StringValue"])
            if layer.attrib["StringValue"] == "CoopWater_0":
                x[0].append(mX)
                y[0].append(mY)
            if layer.attrib["StringValue"] == "CoopWater_1":
                x[1].append(mX)
                y[1].append(mY)
            if layer.attrib["StringValue"] == "CoopWater_2":
                x[2].append(mX)
                y[2].append(mY)
    plt.scatter(x[0], y[0], c="red")
    plt.scatter(x[1], y[1], c="blue")
    plt.scatter(x[2], y[2], c="yellow")
    plt.axes().set_aspect('equal', 'datalim')
    if id == 0:
        title = "Spawning Grounds" + "(" + name + ")"
    if id == 1:
        title = "Marooner's Bay" + "(" + name + ")"
    if id == 2:
        title = "Lost Outpost" + "(" + name + ")"
    if id == 3:
        title = "Salmonid Smokeyard" + "(" + name + ")"
    if id == 4:
        title = "Ruins of Ark Polaris" + "(" + name + ")"
    plt.title(title, fontsize=16)
    if alpha == 0:
        plt.savefig(str(name) + "_" + str(id) +".png", transparent=True, dpi=300)
    else:
        plt.savefig(str(name) + "_" + str(id) +".png", transparent=False, dpi=300)
    plt.close()

if __name__ == "__main__":
    print("0: Spawning Grounds(Shakeup)\n1: Marooner's Bay(Shakeship)\n2: Lost Outpost(Shakehouse)\n3: Salmonid Smokeyard(Shakelift)\n4: Ruins of Ark Polaris(Shakeride)\n5: All\nInput tht key :")
    id = input()
    if str(id) == "5":
        for id in range(0, 5):
            xmlp = et.XMLParser(encoding="utf-8")
            xml = et.parse("./xml/" + str(id) + ".xml", parser=xmlp)
            for type in range(0, 5):
                loadPos(xml, type, id, 1)
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