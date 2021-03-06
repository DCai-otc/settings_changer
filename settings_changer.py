from tkinter import * # Basic Setup
UniFont = "Arial"

# actual program functions
import os, fileinput, time


#defines function which finds the file
def FoldersIn(Path):

    Folders = []

    for r, d, f in os.walk(Path):
        for folder in d:
            if "Documents\My Games\Rainbow Six - Siege" in str(os.path.join(r, folder)):
                for r, d, f in os.walk(str(os.path.join(r, folder))):
                    for folder in d:
                        if "Benchmark" not in (str(os.path.join(r, folder))):
                            Folders.append(str(os.path.join(r, folder)) + "/GameSettings.ini")
                break
    return Folders

# function which saves the FPS limit
def SaveFPS(MaxFPS): # save fps

    Folders = FoldersIn("C:/Users/")
    print (Folders)

    for i in range(len(Folders)):

        with open(Folders[i], 'r') as file:
            data = file.readlines()

        try:
            data[127] = 'FPSLimit={}\n'.format(MaxFPS)

        except:
            pass

        with open(Folders[i], 'w') as file:
            file.writelines(data)

# Function which saves the Data Center
def DataCenter(DataCenter):

    Folders = FoldersIn("C:/Users/")

    for i in range(len(Folders)):

        with open(Folders[i], 'r') as file:
            data = file.readlines()

        try:
            data[171] = 'DataCenterHint=' + str(DataCenter) + "\n"
        except:
            pass

        with open(Folders[i], 'w') as file:
            file.writelines(data)

# Function which saves the Mouse Sensitivity
def MouseSens(MouseSens):

    Folders = FoldersIn("C:/Users/")

    for i in range(len(Folders)):

        with open(Folders[i], 'r') as file:
            data = file.readlines()

        try:
            data[119] = 'MouseSensitivityMultiplierUnit=' + str(MouseSens) + "\n"
        except:
            pass

        with open(Folders[i], 'w') as file:
            file.writelines(data)





# Creating and setting up a window
Window = Tk()
Window.state("zoomed")
Window.title("Modifi Settings Changer")
Window.config(bg="gray13")

# button 1: FPS
LabelWidget = Label(Window, text="FPS Limit", font = (UniFont, 60), bg="gray13", fg="gray87")
LabelWidget.place(relx=0.15, rely=0.5, anchor = CENTER)

FPSWidget = Entry(Window, font = (UniFont, 20), bg="gray19", fg="gray80")
FPSWidget.place(relx=0.15, rely = 0.6, anchor = CENTER)

SaveButton = Button(Window, font = (UniFont, 20), bg="gray19", fg="gray87", command = lambda: SaveFPS(FPSWidget.get()), text="Save", relief = 'flat', bd=0)
SaveButton.place(relx=0.257, rely = 0.6, anchor = CENTER)

#button 2: Server
LabelWidget = Label(Window, text="Server ", font = (UniFont, 60), bg="gray13", fg="gray87")
LabelWidget.place(relx=0.4, rely=0.5, anchor = CENTER)

ServerWidget = Entry(Window, font = (UniFont, 20), bg="gray19", fg="gray80")
ServerWidget.place(relx=0.4, rely = 0.6, anchor = CENTER)

SaveServer = Button(Window, font = (UniFont, 20), bg="gray19", fg="gray87", command = lambda: DataCenter(ServerWidget.get()), text="Save", relief = 'flat', bd=0)
SaveServer.place(relx=0.515   , rely = 0.6, anchor = CENTER)

#button 3: Sensitivity Multiplier
LabelWidget = Label(Window, text="Multiplier", font = (UniFont, 60), bg="gray13", fg="gray87")
LabelWidget.place(relx=0.7, rely=0.5, anchor = CENTER)

MouseWidget = Entry(Window, font = (UniFont, 20), bg="gray19", fg="gray80")
MouseWidget.place(relx=0.7, rely = 0.6, anchor = CENTER)

SaveSens = Button(Window, font = (UniFont, 20), bg="gray19", fg="gray87", command = lambda: MouseSens(MouseWidget.get()), text="Save", relief = 'flat', bd=0)
SaveSens.place(relx=0.815   , rely = 0.6, anchor = CENTER)

Window.mainloop()
