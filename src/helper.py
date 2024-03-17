import os

def getSRCDir(): #dapatkan directory ke folder src di repository ini
    currDir = os.getcwd()
    parentDir = os.path.dirname(currDir)
    while "src" not in os.listdir(parentDir):
        parentDir = os.path.dirname(parentDir)

    return parentDir+"\src"