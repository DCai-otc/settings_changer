from tkinter import * # Basic Setup
UniFont = "Arial"


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


def SaveFPS(MaxFPS): # save fps

    Folders = FoldersIn("C:/Users/")
    print (Folders)

    for i in range(len(Folders)):

        with open(Folders[i], 'r') as file:
            data = file.readlines()

        try:
            data[104] = 'FPSLimit={}\n'.format(MaxFPS)

        except:
            pass

        with open(Folders[i], 'w') as file:
            file.writelines(data)

def DataCenter(DataCenter): #save data center

    Folders = FoldersIn("C:/Users/")

    for i in range(len(Folders)):

        with open(Folders[i], 'r') as file:
            data = file.readlines()

        try:
            data[148] = 'DataCenterHint=' + str(DataCenter) + "\n"
        except:
            pass

        with open(Folders[i], 'w') as file:
            file.writelines(data)

def MouseSens(MouseSens):#saves mouse sensitivity

    Folders = FoldersIn("C:/Users/")

    for i in range(len(Folders)):

        with open(Folders[i], 'r') as file:
            data = file.readlines()

        try:
            data[84] = 'MouseSensitivityMultiplierUnit=' + str(SensitivityMultiplier) + "\n"
        except:
            pass

        with open(Folders[i], 'w') as file:
            file.writelines(data)





# Creating and setting up a window
Window = Tk()
Window.state("zoomed")
Window.title("Testing")
Window.config(bg="gray13")

# Creating a widget 1
LabelWidget = Label(Window, text="FPS Limit", font = (UniFont, 60), bg="gray13", fg="gray87")
LabelWidget.place(relx=0.15, rely=0.5, anchor = CENTER)

FPSWidget = Entry(Window, font = (UniFont, 20), bg="gray19", fg="gray80")
FPSWidget.place(relx=0.15, rely = 0.6, anchor = CENTER)

SaveButton = Button(Window, font = (UniFont, 20), bg="gray19", fg="gray87", command = lambda: SaveFPS(FPSWidget.get()), text="Save", relief = 'flat', bd=0)
SaveButton.place(relx=0.257, rely = 0.6, anchor = CENTER)

#button 2: server
LabelWidget = Label(Window, text="Server ", font = (UniFont, 60), bg="gray13", fg="gray87")
LabelWidget.place(relx=0.4, rely=0.5, anchor = CENTER)

ServerWidget = Entry(Window, font = (UniFont, 20), bg="gray19", fg="gray80")
ServerWidget.place(relx=0.4, rely = 0.6, anchor = CENTER)

SaveServer = Button(Window, font = (UniFont, 20), bg="gray19", fg="gray87", command = lambda: DataCenter(ServerWidget.get()), text="Save", relief = 'flat', bd=0)
SaveServer.place(relx=0.515   , rely = 0.6, anchor = CENTER)

#button 3
LabelWidget = Label(Window, text="Multiplier", font = (UniFont, 60), bg="gray13", fg="gray87")
LabelWidget.place(relx=0.7, rely=0.5, anchor = CENTER)

MouseWidget = Entry(Window, font = (UniFont, 20), bg="gray19", fg="gray80")
MouseWidget.place(relx=0.7, rely = 0.6, anchor = CENTER)

SaveSens = Button(Window, font = (UniFont, 20), bg="gray19", fg="gray87", command = lambda: MouseSens(MouseWidget.get()), text="Save", relief = 'flat', bd=0)
SaveSens.place(relx=0.815   , rely = 0.6, anchor = CENTER)








#testing, ignore
mainframe = Frame(Window)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

tkvar = StringVar(Window)
choices = { 'Pizza','Lasagne','Fries','Fish','Potatoe'}
tkvar.set('Pizza') # set the default option

popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="Choose a dish").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )

# link function to change dropdown
tkvar.trace('w', change_dropdown)

Window.mainloop()
