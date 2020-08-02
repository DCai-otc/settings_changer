# actual program, no ui or ways to interact yet

import os, fileinput, time
#defines function which finds the file
def FoldersIn(Path):

    Folders = []

    for r, d, f in os.walk(Path):
        for folder in d:
            if "Pictures\Documents\My Games\Rainbow Six - Siege" in str(os.path.join(r, folder)):
                for r, d, f in os.walk(str(os.path.join(r, folder))):
                    for folder in d:
                        if "Benchmark" not in (str(os.path.join(r, folder))):
                            Folders.append(str(os.path.join(r, folder)) + "/GameSettings.ini")
                break

    return Folders

#finds the different lines storing different settings with a function.

def UpdateGameFiles(MaxFPS, DataCenter, SensitivityMultiplier):

    global Folders

    for i in range(len(Folders)):

        with open(Folders[i], 'r') as file:
            data = file.readlines()

        try:
            data[105] = 'FPSLimit=' + str(MaxFPS) + "\n"
        except:
            pass


        try:
            data[149] = 'DataCenterHint=' + str(DataCenter) + "\n"
        except:
            pass


        try:
            data[85] = 'MouseSensitivityMultiplierUnit=' + str(SensitivityMultiplier) + "\n"
        except:
            pass


        with open(Folders[i], 'w') as file:
            file.writelines(data)


def SaveSettings(MaxFPS, DataCenter, SensitivityMultiplier):

    global Folders

    Folders = FoldersIn("C:/Users/")

    UpdateGameFiles(MaxFPS, DataCenter, SensitivityMultiplier)
