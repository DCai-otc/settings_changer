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


#finds the different lines storing different settings with a function, then change it.
def UpdateGameFiles(MaxFPS, DataCenter, SensitivityMultiplier):

    global Folders

    for i in range(len(Folders)):

        with open(Folders[i], 'r') as file:
            data = file.readlines()

        try:
            data[104] = 'FPSLimit=' + str(MaxFPS) + "\n"
        except:
            pass


        try:
            data[148] = 'DataCenterHint=' + str(DataCenter) + "\n"
        except:
            pass


        try:
            data[84] = 'MouseSensitivityMultiplierUnit=' + str(SensitivityMultiplier) + "\n"
        except:
            pass


        with open(Folders[i], 'w') as file:
            file.writelines(data)

def SaveSettings(MaxFPS, DataCenter, SensitivityMultiplier):    # defines the function for saving user input.

    global Folders

    Folders = FoldersIn("C:/Users/")

    UpdateGameFiles(MaxFPS, DataCenter, SensitivityMultiplier)

MaxFPS = str(input("What would you like to change the FPS limit to? Anything below 30 will disable the FPS limit."))
DataCenter = (input("What would you like to change the Data Center to?"))
SensitivityMultiplier = str(input("What would you like to change the Sensitivity Multiplier to?"))

SaveSettings(MaxFPS, DataCenter, SensitivityMultiplier)
