"""
this program will take an email denoted as a .eml file and remind the user to take back the book when it is due.
the program will read the email and find the "Due Date" string, following the string there will be a date, this is the due date.
The program will print the due date on a GUI and offer three reminder options:
Set reminder: day of, day before, custom
the final GUI screen will display a box with the user's decision
By: Mitch Baumgartner
"""
# import CSV to read and write files
import csv 

# import GUI feature
from tkinter import Tk, Button, Frame, Entry, Label, LEFT, RIGHT, BOTTOM, S, NE, W, SW, E, SE, TOP
from tkinter.messagebox import showinfo


# open the email file 
email_file = open("library checkout receipt.eml")

#read the contents of the email 
email_file_content = email_file.read()

# split email into list to find index value of date (Day, Month, Year)
email_split = email_file_content.split(" ")


# find the due date in the email 
due_date_string_in_email = "Date:"

# if there is a due date, print the due date
if due_date_string_in_email in email_split:
    due_date_index = email_split.index(due_date_string_in_email)

    due_date_with_comma = email_split[due_date_index + 1]

    #seperate the date by the comma to get date and time seperate
    due_date = due_date_with_comma.replace(",", " " )


#get due date into list
due_date_list = due_date.split(" ")

# change the date to month, day, year
due_date_split = due_date.split(" ")
date = due_date_split[0]
date_split = date.split("/")
#add a coma after the day of the month
for i in date_split[0]:
    date_split[1] += ','
#remove the first element at index 0 to align with the month associated with that number
if date_split[0] == "1":
    date_split[0]="January"
elif date_split[0] == "2":
    date_split[0] = "February"
elif date_split[0] == "3":
    date_split[0] = "March"
elif date_split[0] == "4":
    date_split[0]="April"
elif date_split[0] == "5":
    date_split[0]="May"
elif date_split[0] == "6":
    date_split[0]="June"
elif date_split[0] == "7":
    date_split[0]="July"    
elif date_split[0] == "8":
    date_split[0]="August"
elif date_split[0] == "9":
    date_split[0]="September"
elif date_split[0] == "10":
    date_split[0]="October"
elif date_split[0] == "11":
    date_split[0]="November"
else:
    date_split[0]="December"


# put due date list back into a string so it prints properly 
empty_string = " "
due_date_final_string = empty_string.join(date_split)

#print("Your book is due on " + due_date_final_string +" at " + due_date_list[1] + ".")

#close the file
email_file.close()

"""
This part of the program will build a GUI that gives the user button options to set a reminder to be reminded to return then book
"""

# define the reminder button for day of, when clicked the user will see a box displaying the reminder for day of. The time is automatically defined as 08:00
def day_of_clicked(): 
    showinfo(message= "- Reminder set! -\n\n"+ str(due_date_final_string) + "\n08:00 \n\nNote: RETURN YOUR LIBRARY BOOK TODAY")

#define the reminder buttton for custom, user will enter integers corresponding to the entry firelds (month, day, hour, minute) year is automatically assigned based on the book's due date
def custom_reminder_clicked():
    # confirm that the day is within 31 days and the month is within 12 months
    if int(entry_month.get()) in range(1,13) and int(entry_day.get()) in range(1, 32):
        # confirm that the hours is between 0-23 and minutes is between 0-59
        if int(entry_hours.get()) in range(0,24) and int(entry_minutes.get()) in range(0, 60):
            # when user enters integer for month, GUI changes the integer to a string with the corresponding month
            if int(entry_month.get()) == 1:
                showinfo(message= "- Reminder set! -\n\n" + "January " + str(entry_day.get()) + ", " + str(date_split[2]) + "\n" + str(entry_hours.get()) + ":" + str(entry_minutes.get()) +"\n\nNote: RETURN YOUR LIBRARY BOOK ON " + due_date_final_string )
            elif int(entry_month.get()) == 2:
                showinfo(message= "- Reminder set! -\n\n" + "February " + str(entry_day.get()) + ", " + str(date_split[2]) + "\n" + str(entry_hours.get()) + ":" + str(entry_minutes.get()) +"\n\nNote: RETURN YOUR LIBRARY BOOK ON " + due_date_final_string) 
            elif int(entry_month.get()) == 3:
                showinfo(message= "- Reminder set! -\n\n" + "March " + str(entry_day.get()) + ", " + str(date_split[2]) + "\n" + str(entry_hours.get()) + ":" + str(entry_minutes.get()) +"\n\nNote: RETURN YOUR LIBRARY BOOK ON " + due_date_final_string)
            elif int(entry_month.get()) == 4:
                showinfo(message= "- Reminder set! -\n\n" + "April " + str(entry_day.get()) + ", " + str(date_split[2]) + "\n" + str(entry_hours.get()) + ":" + str(entry_minutes.get()) +"\n\nNote: RETURN YOUR LIBRARY BOOK ON " + due_date_final_string)
            elif int(entry_month.get()) == 5:
                showinfo(message= "- Reminder set! -\n\n" + "May " + str(entry_day.get()) + ", " + str(date_split[2]) + "\n" + str(entry_hours.get()) + ":" + str(entry_minutes.get()) +"\n\nNote: RETURN YOUR LIBRARY BOOK ON " + due_date_final_string)
            elif int(entry_month.get()) == 6:
                showinfo(message= "- Reminder set! -\n\n" + "June " + str(entry_day.get()) + ", " + str(date_split[2]) + "\n" + str(entry_hours.get()) + ":" + str(entry_minutes.get()) +"\n\nNote: RETURN YOUR LIBRARY BOOK ON " + due_date_final_string)
            elif int(entry_month.get()) == 7:
                showinfo(message= "- Reminder set! -\n\n" + "July " + str(entry_day.get()) + ", " + str(date_split[2]) + "\n" + str(entry_hours.get()) + ":" + str(entry_minutes.get()) +"\n\nNote: RETURN YOUR LIBRARY BOOK ON " + due_date_final_string)  
            elif int(entry_month.get()) == 8:
                showinfo(message= "- Reminder set! -\n\n" + "August " + str(entry_day.get()) + ", " + str(date_split[2]) + "\n" + str(entry_hours.get()) + ":" + str(entry_minutes.get()) +"\n\nNote: RETURN YOUR LIBRARY BOOK ON " + due_date_final_string)   
            elif int(entry_month.get()) == 9:
                showinfo(message= "- Reminder set! -\n\n" + "September " + str(entry_day.get()) + ", " + str(date_split[2]) + "\n" + str(entry_hours.get()) + ":" + str(entry_minutes.get()) +"\n\nNote: RETURN YOUR LIBRARY BOOK ON " + due_date_final_string) 
            elif int(entry_month.get()) == 10:
                showinfo(message= "- Reminder set! -\n\n" + "October " + str(entry_day.get()) + ", " + str(date_split[2]) + "\n" + str(entry_hours.get()) + ":" + str(entry_minutes.get()) +"\n\nNote: RETURN YOUR LIBRARY BOOK ON " + due_date_final_string)
            elif int(entry_month.get()) == 11:
                showinfo(message= "- Reminder set! -\n\n" + "November " + str(entry_day.get()) + ", " + str(date_split[2]) + "\n" + str(entry_hours.get()) + ":" + str(entry_minutes.get()) +"\n\nNote: RETURN YOUR LIBRARY BOOK ON " + due_date_final_string)
            elif int(entry_month.get()) == 12:
                showinfo(message= "- Reminder set! -\n\n" + "December " + str(entry_day.get()) + ", " + str(date_split[2]) + "\n" + str(entry_hours.get()) + ":" + str(entry_minutes.get()) + "\n\nNote: RETURN YOUR LIBRARY BOOK ON " + due_date_final_string)
        # if user enters integer outside of range, error message
        else: 
            showinfo(message= "Please enter a valid time.")
    # if user enters integer outside of range, error message
    else:
        showinfo(message= "Please enter a valid month and day.")


root = Tk()

#set up window frame for GUI interface

frame0 = Frame(master = root, width = 476, height = 10, bg = "white")
frame0.pack()

frame1 = Frame(master = root, width = 476, height = 10, bg = "white")
frame1.pack()

frame2 = Frame(master = root, width = 476, height = 10, bg = "white")
frame2.pack()

frame6 = Frame(master = root, width = 476, height = 10, bg = "white")
frame6.pack()

frame3 = Frame(master = root, width = 476, height = 10, bg = "white")
frame3.pack()

frame4 = Frame(master = root, width = 476, height = 10, bg = "white")
frame4.pack()

frame5 = Frame(master = root, width = 476, height = 10, bg = "white")
frame5.pack()

frame = Frame(master=root, width=500, height = 5, padx =5, pady = 5, bg = 'white')
frame.pack()



#give display for user that shows when book is due on
display_label = Label(master=frame0, font="Helvetica 16 bold", text="Your book is due on:")
due_date_label = Label(master=frame0, foreground="red", font="Helvetica 20 bold italic", text=due_date_final_string + " at " + due_date_list[1] + "\n")
final_display_label = Label(master=frame0, font="Helvetica 16 bold", text="Set a reminder:")
custom_reminder_label = Label(master=frame2, text="Custom: (Numeric values)")
#show display in GUI
display_label.pack()
due_date_label.pack()
final_display_label.pack()
custom_reminder_label.pack()

# add button that sets reminder for day of
day_of_button = Button(master= frame1, 
                text = "Morning of Due Date",
                padx = 15,
                pady = 10,
                anchor = NE,
                activeforeground = "red",
                fg = "blue",
                command= day_of_clicked)

#add button to confirm custom date reminder
custom_reminder_button = Button(master= frame5, 
                text = "Confirm Custom Reminder",
                padx = 10,
                pady = 8,
                anchor = NE,
                activeforeground = "red",
                fg = "blue",
                command= custom_reminder_clicked)


#add button to GUI
day_of_button.pack()
custom_reminder_button.pack()





#Custom grid that displays the entry fields for month, day, hours, minutes

month = Label(master=frame3,
              padx = 2,
              pady = 3,
              text = "Month:")
day = Label(master=frame3, 
                 padx = 2, 
                 pady = 3, 
                 text="Day:")
hours = Label(master=frame3,
             padx = 2,
             pady = 3,
             text = "Time:")
minutes = Label(master=frame3,
                   padx = 2,
                   pady = 3,
                   text = ":")



#show labeled custom reminder feature in GUI (includes month, day, time (hour, minute) entry fields)
# assign the grid positions
#month label 
month.grid(row = 0, column = 0)
#day label
day.grid(row = 0, column = 2)
#time label
hours.grid(row = 0, column = 4)
#semi-colon label
minutes.grid(row = 0, column = 6)


# entry fields are defined below
#month entry
entry_month = Entry(master=frame3, width = 4)
#day entry
entry_day = Entry(master=frame3, width = 4)
#time entry (Hours)
entry_hours = Entry(master=frame3, width = 2)
#time entry (Minutes)
entry_minutes = Entry(master=frame3, width = 2)

#show entry for month, day, hours, minutes in GUI
entry_month.grid(row = 0, column = 1)
entry_day.grid(row = 0, column = 3)
entry_hours.grid(row = 0, column = 5)
entry_minutes.grid(row = 0, column = 7)

root.mainloop()