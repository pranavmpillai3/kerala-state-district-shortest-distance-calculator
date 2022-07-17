from DistanceCalc import distance
from KeralaMap import map_display, line_display
from tkinter import *
from tkinter import messagebox

# ********** COLOURS USED **********
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"


# **********************************

# ********** METHOD USED TO READ DATA FROM CSV**********

def readfromcsv():
    origin = originco = (0, 0)
    destination = destinationco = (0, 0)
    dist = (str(dist1_textbox.get()).upper(), str(dist2_textbox.get()).upper())
    with open('KeralaDistricts.csv') as file:
        content = file.readlines()
    rows = content[1:]
    d1, d2 = dist[0], dist[1]
    districts = []

    for i in range(0, len(rows)):
        districts.append(rows[i].split(','))

    flag0 = 0
    flag1 = 0

    # loop to find wheather entered district is available in the list
    for district in districts:
        if district[0] == d1:
            origin = (float(district[3]), float(district[4]))
            originco = (int(district[1]), int(district[2]))
            flag0 = 1

        if district[0] == d2:
            destination = (float(district[3]), float(district[4]))
            destinationco = (int(district[1]), int(district[2]))
            flag1 = 1

    # print the message if district is not in the list
    if flag0 == 0 and flag1 == 0:
        messagebox.showerror("ERROR", 'You entered a wrong district name')
        exit()
    elif (flag0 == 0 and flag1 == 1) or (flag0 == 1 and flag1 == 0):
        messagebox.showerror("ERROR", "You haven't enter either one of district name")
        exit()
    else:
        #  if district is available in the list displays map and popup the shortest between them
        shortDist = int(distance(origin, destination))
        window.withdraw()
        map_display(districts)
        line_display(originco, destinationco)
        messagebox.showinfo("Distance", f'shortest distance is : {shortDist} km')
        window.destroy()
        exit()


# **********************************


# ********** UI FUNCTION **********

window = Tk()
window.title('Distance Calculator')
window.config(padx=100, pady=100)

# Canvas
canvas = Canvas(window, height=200, width=200)
logo_img = PhotoImage(file="KeralaIcon.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
dist1_label = Label(window, text="Enter the first District :")
dist1_label.grid(row=1, column=0)

dist2_label = Label(window, text="Enter the second District :")
dist2_label.grid(row=2, column=0)

# Textbox
dist1_textbox = Entry(window, width=35)
dist1_textbox.insert(0, "ERNAKULAM")
dist1_textbox.grid(row=1, column=1, columnspan=2)
dist1_textbox.focus()

dist2_textbox = Entry(window, width=35)
dist2_textbox.insert(0, "KOTTAYAM")
dist2_textbox.grid(row=2, column=1, columnspan=2)

# Buttons
button = Button(window, text="Check", command=readfromcsv)
button.grid(row=3, column=1)

window.mainloop()
# **********************************
