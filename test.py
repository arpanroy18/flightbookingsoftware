import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import re
import os

try:
    os.remove("Receipt.txt")
except FileNotFoundError:
    pass
#removes all previous passenger tickets from users before
for i in range(9):
    try:
        os.remove("Passenger "+str(i)+".txt")
    except FileNotFoundError:
        pass

#initalizes root frame
root = tk.Tk()
#sets dimensions of program
root.geometry('700x500')
root.title('SkyToronto Flight Booking System')

#initalizes main frame to use for screens later on. Main frame is placed on top of root frame
mainFrame = tk.Frame(root, bg="#ffffff")
mainFrame.pack(side=tk.LEFT)
#pack_propagate helps formatting of frame and prevents further errors.
mainFrame.pack_propagate(False)
screenHeight = root.winfo_height()
#places main frame on screen underneath menu banner
mainFrame.place(x=0, y=50, height=500, width=700)

def mainFrameLayout():
    #setting layout of landing page of program. tk.Label function is used to place text labels the user can read
    lb = tk.Label(mainFrame, text='Home Page', font=('Rage Italic', 16), bg="#ffffff")
    lb.place(x=0, y=0)
    titleLable = tk.Label(mainFrame, text='Welcome to SkyToronto, the most convenient way to escape the cold!', font=('Trebuchet MS', 16), wraplength=600, bg="#ffffff")
    titleLable.place(x=50, y=50)
    titleDesc = tk.Label(mainFrame, text='We have helped over 25,000 travellers visit their dream destinations in just a few steps', font=('Trebuchet MS', 13), wraplength=600, bg="#ffffff")
    titleDesc.place(x=50, y=110)
    #button to direct user to the booking page of the program
    bookButton = tk.Button(mainFrame, text='Book Now!', font=('Bold', 20), fg='black', activebackground='#4BA8A4', activeforeground='black', bd=2, command=lambda: switchPage(bookPage))
    bookButton.place(x=260, y=180)



#calls main function layout so that the contents of main frame is displayed on screen. Layout is in function to help with page switching in the future
mainFrameLayout()
#function to help switch pages in the program. Re-iterates through each frame in frame and deletes the frame.
def deletePages():
    for frame in mainFrame.winfo_children(): #checks for each frame on the screen and destroys them. Removes them off of the screen
        frame.destroy()



#home page function which contains all the contents of the home frame. It is in function so that this page can be called for later use
def homePage():
    homeFrame = tk.Frame(mainFrame)
    #places title lable
    lb = tk.Label(mainFrame, text='Home Page', font=('Trebuchet MS', 16)) #places label on main frame for user to view
    lb.place(x=0, y=0)
    mainFrameLayout()
    #pack frame so that it is displayed on the screen. Pady function used to add 20 pixels y seperation
    homeFrame.pack(pady=20)


def bookPage(): #function to call the next page. The booking page

    global paxGlobal
    bookFrame = tk.Frame(mainFrame)
    lb = tk.Label(mainFrame, text='Booking Page', font=('Trebuchet MS', 16), bg="#ffffff", bd='2') #lable for title
    lb.place(x=0, y=0)

    #check if you are going to or leaving from a city
    tripDetail = tk.StringVar() #initalives variable that the user's direction of travel will be stored into. Use of stringVar function to enable use inside tkinter functions later on
    tripDetail.set("Direction") # Set the default value of the variable. This is a temporary value
    # Create a dropdown menu with the two options
    dropdown = tk.OptionMenu(mainFrame, tripDetail, "Going To", "Leaving From") #creates a dropdown menu where the user can select if they are leaving from a location or going to a location
    dropdown.config(width=10) #sets width of the button to help organize page layout
    dropdown.place(x=50, y=40)

    # Create a function to handle the selection
    def selectDirection(event): #function to store value in variable every single time a new option is selected
        selectedValue = tripDetail.get() #stores any value selected from the dropdown menu into variable
        tripDetail.set(selectedValue) #sets the name of the dropdown menu. For example, if you select Going To, it will display "Going To"
    # Assign the function to the dropdown menu
    dropdown.bind("<ButtonRelease-1>", selectDirection) #whenever the user clicks on the option menu, it will call the function so that the variable is updated
    # This will update the variable immediately when user click on option
    tripDetail.trace("w", lambda *args: selectDirection(None)) #callback function for updating direction when trip detail changes


    #allow user to type in where they are travelling
    destinationInput = tk.StringVar() #initalizes variable that destination will be put into
    # Create a textbox for the user to enter a string and sets visual properties
    textboxLocation = tk.Entry(mainFrame, textvariable=destinationInput, highlightbackground='black', highlightthickness=2)
    textboxLocation.place(x=180, y=40)
    # Function to print the input to the console and update the destinationInput variable
    def updateDestination():
        destinationInput.set(textboxLocation.get()) #stores variable in destination input by getting text inside the textbox
    # Bind the <KeyRelease> event to the textbox
    textboxLocation.bind("<KeyRelease>", lambda event: updateDestination()) #whenver the user releases a key, it will store any data into the textbox into destinationInput variable


    #check what month you are leaving
    tripDate = tk.StringVar() #initalizes variable that month of trip will be put into
    tripDate.set("Month") # Set the default value of variable so that user knows this dropdown menu is to select month
    # Create a dropdown menu with the two options
    dropdownMonth = tk.OptionMenu(mainFrame, tripDate, "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December") #sets the options of the dropdown menu the user can select
    dropdownMonth.config(width=10)
    dropdownMonth.pack()
    dropdownMonth.place(x=350 , y=40)
    # Create a function to handle the selection
    def selectMonth(event):
        selectedValue = tripDate.get() #updates value of selected value by getting option selected from dropdown menu
        tripDate.set(selectedValue)
    # Assign the function to the dropdown menu
    dropdownMonth.bind("<ButtonRelease-1>", selectMonth)
    # This will update the variable immediately when user click on option
    tripDate.trace("w", lambda *args: selectMonth(None)) #whenever value of tripDate changes, it will call the function to update the variable

    #check how many passengers are travelling
    tripPax = tk.StringVar() #initalizes variable that number of passengers will be stored in
    tripPax.set("Pax") # Set the default value so the user knows that the dropdown menu is to select number of passengers
    # Create a dropdown menu with the two options
    dropdownPax = tk.OptionMenu(mainFrame, tripPax, "1", "2", "3", "4", "5", "6", "7", "8", "9") #allows users to select upto 9 passengers
    dropdownPax.place(x=490 , y=40)

    # Create a function to handle the selection
    def updatePax(event):
        global paxGlobal
        selectedValue = tripPax.get()
        tripPax.set(selectedValue)
        paxGlobal = selectedValue #assigns number of pax to global values. Stores both in local and global variable so that value can easily be accessed and prevent errors.
    # Assign the function to the dropdown menu
    dropdownPax.bind("<ButtonRelease-1>", updatePax)
    # This will update the variable immediately when user click on option
    tripPax.trace("w", lambda *args: updatePax(None)) #whenever value of tripPax changes (or is written over), it will call the function to update variable

    #create search button. Search button is used to filter flights. It calls the searchFilter function and passes the parameters of the trip details to only display flights that meet the criteria
    searchButton = tk.Button(mainFrame, text='Search Flights', font=('Bold', 10), fg='black', activebackground='#4BA8A4', activeforeground='black', bd=2, command=lambda: searchFilter(tripDetail.get(), destinationInput.get(), tripDate.get(), tripPax.get()))
    searchButton.place(x=220, y=80)


codeGlobal = 0 #assigns temp value to global variable so that it can used later in several functions
def orderPage(flightChoice, pax): #function is called and receives two arguements. These arguements are used to display order details
    global codeGlobal #allows global variable to be used within the function
    orderFrame = tk.Frame(mainFrame) #initalizes order frame. This frame loads the order screen where user can input passenger details

    lb = tk.Label(mainFrame, text='Order page', font=('Trebuchet MS', 16), bg="#ffffff", bd='2')
    lb.place(x=0, y=0)
    #following 6 lines orf code manipulates text from flight database to find the flight code and assigns it to both a local and global variable
    flightDisplay = list(re.split(r' \| |Departure', listFlights[int(flightChoice)-1])) #listFlights is a list that stores contents of all flights that meets search criteria
    sentence = listFlights[int(flightChoice)-1]
    startCode = sentence.find("(")
    endCode = sentence.find(")")
    flightCode = sentence[startCode+1:endCode] #uses index slices to extract flight code
    codeGlobal = flightCode #assigns local variable to global variable

    flightTitleFinal = str(flightDisplay[0] + " | "+ flightDisplay[3] + " | "+ flightDisplay[4] + " per ticket") #stores order details as a string to be displayed later
    priceInt = flightDisplay[4].replace("Price: $", "") #replaces an unneccessary string in the list with nothing. Manipulates the string

    flightTitle = tk.Label(mainFrame, text=flightTitleFinal, font=('Trebuchet MS', 10), bg="#ffffff", bd='2') #sets title of the page to order details of variable assigned to previously
    flightTitle.place(x=root.winfo_width()/2, y=85, anchor='center') #places title in the centre
    pageTitle = tk.Label(mainFrame, text="Order Page", font=('Trebuchet MS', 16), bg="#ffffff", bd='2')
    pageTitle.place(x=root.winfo_width()/2, y=50, anchor='center')

    if pax == "1": #checks for number of tickets to display grammatically correct title
        ticketPurchaseMsg = "Order for "+pax+" ticket"
    else:
        ticketPurchaseMsg = "Order for "+pax+" tickets"

    #following set of code initalizes and displays all the text on the page. This is done using the tk.Label function.
    ticketsPurchase = tk.Label(mainFrame, text=ticketPurchaseMsg, font=('Trebuchet MS', 15), bg="#ffffff", bd='2')
    ticketsPurchase.place(x=root.winfo_width()/2, y=110, anchor='center')
    orderTitle = tk.Label(mainFrame, text="Enter order details: ", font=('Trebuchet MS', 10), bg="#ffffff", bd='2')
    orderTitle.place(x=50, y=130)
    passengerTitle = tk.Label(mainFrame, text="Enter passenger information for "+ pax + " passengers: ", font=('Trebuchet MS', 10), bg="#ffffff", bd='2')
    passengerTitle.place(x=225, y=130)
    warningTitle = tk.Label(mainFrame, text="Please ensure that the names of the passengers match the names on their government issued documents\n Passengers with incorrect names will not be allowed to board the plane\n In the case of flight cancellations, the airline is responsible for arranging a rescheduled flight", font=('Trebuchet MS', 8), bg="#cccccc", bd='2', wraplength=170)
    warningTitle.place(x=500, y=130)

    #displays total cost of flight ticket to user.
    tripDetail = tk.Label(mainFrame, text="Trip Fare", font=('Trebuchet MS', 8), bg="#ffffff", bd='2', wraplength=170)
    tripDetail.place(x=500, y=315)
    tripDetailTicket = tk.Label(mainFrame, text="Ticket x "+pax+"   $"+str(int(priceInt)*int(pax)), font=('Trebuchet MS', 8), bg="#ffffff", bd='2', wraplength=170)
    tripDetailTicket.place(x=500, y=335)
    feeCost = tk.Label(mainFrame, text="HST  $"+str((int(priceInt)*int(pax)*0.13)), font=('Trebuchet MS', 8), bg="#ffffff", bd='2', wraplength=170)
    feeCost.place(x=500, y=355)
    tripTotal = tk.Label(mainFrame, text="Total Cost $"+str(round((int(priceInt)*int(pax)*1.13), 2)), font=('Trebuchet MS', 8), bg="#ffffff", bd='2', wraplength=170)
    tripTotal.place(x=500, y=375)

    textboxes = []
    for i in range(int(pax)): #creates a textboxt to enter full name for each passenger
        textboxes.append(tk.Entry(mainFrame, width=25, highlightbackground='black', highlightcolor='black', bd='2'))
        textboxes[i].insert(0, 'Passenger ' + str(i+1)+ ' Full Name')
        textboxes[i].place(x=220, y= 180 + i * 30)
        textboxes[-1].bind("<FocusIn>", lambda event, i=i: onFocus(event, i)) #deletes placeholder text in texboxes

    def onFocus(event, i):
        textboxes[i].delete(0, tk.END) #deletes placeholder text by deleting last value in list of textboxes

    textboxes2 = []
    for i in range(int(pax)):
        textboxes2.append(tk.Entry(mainFrame, width=20, highlightbackground='black', highlightcolor='black', bd='2'))
        textboxes2[i].insert(0, "Age")
        textboxes2[i].place(x=345, y= 180 + i * 30)
        textboxes2[-1].bind("<FocusIn>", lambda event, i=i: onFocus1(event, i))

    def onFocus1(event, i):
        textboxes2[i].delete(0, tk.END)

    #creates order form where user is able to input basic information need for flight booking process
    nameEntry = tk.Label(mainFrame, text="Name: ", font=('Trebuchet MS', 10), bg="#ffffff", bd='2')
    nameEntry.place(x=50, y=160)
    singleTextbox = tk.Entry(mainFrame, width=20, highlightbackground='black', highlightcolor='black')
    singleTextbox.place(x=50, y=190)
    emailEntry = tk.Label(mainFrame, text="Email: ", font=('Trebuchet MS', 10), bg="#ffffff", bd='2')
    emailEntry.place(x=50, y=210)
    nameBox = tk.Entry(mainFrame, width=20, highlightbackground='black', highlightcolor='black')
    nameBox.place(x=50, y=240)
    addressEntry = tk.Label(mainFrame, text="Address: ", font=('Trebuchet MS', 10), bg="#ffffff", bd='2')
    addressEntry.place(x=50, y=270)
    addressBox = tk.Entry(mainFrame, width=20, highlightbackground='black', highlightcolor='black')
    addressBox.place(x=50, y=300)
    phoneEntry = tk.Label(mainFrame, text="Phone Number: ", font=('Trebuchet MS', 10), bg="#ffffff", bd='2')
    phoneEntry.place(x=50, y=330)
    phoneBox = tk.Entry(mainFrame, width=20, highlightbackground='black', highlightcolor='black')
    phoneBox.place(x=50, y=360)

    def submit(): #submit function will store all inputted values in a list which is pased onto another function
        inputList = []
        for i in range(int(pax)): #get information for each variable and store it in a single list
            inputList.append(textboxes[i].get())
            inputList.append(textboxes2[i].get())
        inputList.append(singleTextbox.get())
        inputList.append(nameBox.get())
        inputList.append(addressBox.get())
        inputList.append(phoneBox.get())

        switchPage(paymentPage, inputList, flightChoice) #switches page to payment page and passes on two additional parameters

    submitButton = tk.Button(mainFrame, text="Proceed to Payment", command=submit) #when button is clicked, it wil call submit function
    submitButton.place(x=500, y=395)

paxGlobal = 0 #assigns temp value to global which will be used in multiple functions

def paymentPage(inputList, pax, flightNumber, flightCode): #initalizes the payment page where user enters payment information
    paymentFrame = tk.Frame(mainFrame)
    pageTitle = tk.Label(mainFrame, text='Payment Page', font=('Trebuchet MS', 16), bg='#ffffff') #sets title of page
    pageTitle.place(x=root.winfo_width()/2, y=50, anchor='center')
    def checkPayment(): #function to check payment details for validity. Will not allow user to proceed if payment details are invalid. 
        #follwowing three codes stores all payment details entered into 3 variables
        cardNumber = cardNumberEntry.get() #gets all payment information and stores it in variables
        cvv = cvvEntry.get()
        date = dateEntry.get()
        cardNumber = cardNumber.replace(" ", "") #in case of different card formats, it wil replace any spaces to prevent errors

        # check if inputs are valid
        if not cardNumber.isdigit() or len(cardNumber) != 16: #checks if card digits are not 16 in length and gives error message
            messagebox.showerror("Invalid Input", "Invalid card number")
        elif not cvv.isdigit() or len(cvv) != 3: #checks if cvv is not three digits and throws errors message if true
            messagebox.showerror("Invalid Input", "Invalid CVV")
        elif len(date)!=7 or "/" not in date: #check if date is in propr format by checks length of input and if a slash is in the string
            messagebox.showerror("Invalid Input", "Invalid date")
        else:
            messagebox.showinfo("Payment Successful", "Payment has been processed successfully") #shows success message if all details are valid and switches page to the confirmation page
            switchPage(confirmationPage, inputList, pax, flightNumber, flightCode) #switches page by calling switchPage function

    paymentYPos = 90 #variable assigned value so that all positioning is correlated to one widget or button. Helps organization
    
    #following code initalizes payment form where user can input card, cvv, and expiration date. Three labels and three entry forms are used for this
    cardNumberLabel = tk.Label(mainFrame, text="Card Number:", font=('Trebuchet MS', 13), bg='#ffffff')
    cardNumberLabel.place(x=350, y=paymentYPos, anchor='center')  
    cardNumberEntry = tk.Entry(mainFrame)
    cardNumberEntry.config(justify='center', font=("Courier", 10))
    cardNumberEntry.place(x=350, y=paymentYPos+30, anchor='center', width=300)
    cvvLabel = tk.Label(mainFrame, text="CVV:", font=('Trebuchet MS', 13), bg='#ffffff')
    cvvLabel.place(x=350, y=paymentYPos+70, anchor='center')
    cvvEntry = tk.Entry(mainFrame)
    cvvEntry.config(justify='center', font=("Courier", 10))
    cvvEntry.place(x=350, y=paymentYPos+100, anchor='center', width=300)
    dateLabel = tk.Label(mainFrame, text="Date: (MM/YYYY)", font=('Trebuchet MS', 13), bg='#ffffff')
    dateLabel.place(x=350, y=paymentYPos+140, anchor='center')
    dateEntry = tk.Entry(mainFrame)
    dateEntry.config(justify='center', font=("Courier", 10))
    dateEntry.place(x=350, y=paymentYPos+170, anchor='center', width=300)
    
    
    submitButton = tk.Button(mainFrame, text="Submit", command=checkPayment) #when user hits submit, it will call checkPayment function which then directs to confirmation page
    submitButton.place(x=350, y=paymentYPos+200, anchor='center') #switches page to confirmation page and checks payment validity

    paymentFrame.pack(pady=20)


def confirmationPage(inputList, pax, flightNumber, flightCode):

    stringFile = listFlights[int(pax)-1] #stores the selected flight by the user in a variable so that full details of the file can be easily accessed
    #following code manipulates string in the stringFile variable to extract required information to deliver ticket to customer
    route = stringFile.split("|")[0].strip()
    airlineFlight = stringFile.split("|")[1].strip()
    airline = airlineFlight.split("(")[0].strip()
    flightCode = airlineFlight.split("(")[1].replace(")","").strip()
    departureDate = stringFile.split("Depature: ")[1].split("|")[0].strip()

    listYPos = 90

    #the following code shows text to the user that their order has been successful and informs them of their email delivery.
    pageTitle = tk.Label(mainFrame, text="Thank You!", font=('Trebuchet MS', 25), bg="#ffffff", bd='2') 
    pageTitle.place(x=root.winfo_width()/2, y=listYPos, anchor='center')
    pageTitle2 = tk.Label(mainFrame, text="Your Order Was Completed Successfully.", font=('Trebuchet MS', 20), bg="#ffffff", bd='2')
    pageTitle2.place(x=root.winfo_width()/2, y=listYPos+45, anchor='center')
    pageTitle3 = tk.Label(mainFrame, text="An email containing the details of your order and ticket will be sent to the email address provided shortly", font=('Trebuchet MS', 15), bg="#ffffff", bd='2', wraplength=400)
    pageTitle3.place(x=root.winfo_width()/2, y=listYPos+110, anchor='center')
    passengerNum = 1 #sets default value of passengerNum to 1

    for i in range(0, len(inputList)-4, 2): #checks how many passengers there are by checking the list of the inputList
        orderNumber = str(random.randint(10000000000,19999999999)) #creates random order number using randint function
        name = inputList[i] #collects values in the inputList form to extract passenger name and age
        age = inputList[i+1] #colelcts age of passenger
        with open("Passenger "+str(passengerNum)+".txt", "w") as file: #creats digital tickets for passengers by creating file with number of passenger
            file.write("Passenger "+str(passengerNum)+" Ticket\n") #writes the passenger number
            file.write("Passenger Name: "+name+"\n") # writes passenger names
            file.write("Passenger Age: "+age+"\n") #writes passenger age
            file.write("Route: "+route+"\n") #writes route of flight
            file.write("Departure Date: "+departureDate+"\n") #writes departure date
            file.write("Airline: "+airline+"\n") #writes airline name
            file.write("Flight Code: "+flightCode+"\n") #writes flight code
            file.write("Ticket Number: "+orderNumber) #writes ticket number

        passengerNum += 1 #adds one to passenger so that next file will display the next passenger number and not repeat previous number

    with open("Receipt.txt", "w") as file: #create electronic receipt that displays order total and billig information
        file.write("Electronic Receipt\n") #title of receipt
        file.write("------------------\n")
        file.write("Bill To:\n") #displays billing address
        file.write(inputList[-4]+"\n")
        file.write(inputList[-2])
        file.write("\n")
        file.write("\n")

        file.write("Total: $"+str(125*int(paxGlobal))) #following lines of code displays order total to user
        file.write("\n")
        file.write("HST: $"+str((125*int(paxGlobal)*0.13)))
        file.write("\n")
        file.write("Total Cost: $"+str(round((125*int(paxGlobal)*1.13), 2)))
        file.write("\n")
        file.write("Thank you for using SkyToronto!")

    with open("Flights.txt", "r") as file:
        # Read each line
        lines = file.readlines()

    # Go through each line
    for i, line in enumerate(lines): #for loop to re-iterate through each line in the flight database
        # Check if the flight code is in the line
        if codeGlobal in line: #if the flight code the user booked is in the line
            # Get the current number of seats
            match = re.search(r'seats="(\d+),', line) #uses re library to search for seats pattern using regula expression in the line of the selected flight
            seats = int(match.group(1)) #extracts the matched string to determine the number of seats and converts to integer
            # Subtract the number of pax
            seats -= int(paxGlobal) #subtracts the number of tickets booked to the seats available amount. 8 seats available and 5 booked will update 3 as seats available
            # Replace the number of seats in the line
            lines[i] = line.replace(match.group(), 'seats="'+str(seats)+",") #replaces old seats available with current seats available. This replaces the string not file

    # Open the file again to write the new lines
    with open("flights.txt", "w") as file:
        file.writelines(lines) #opens file to rewrite updated flight database


def toggleMenu():
    global collapseMenu #globalizes function
    def collapseMenu(): #collapseMenu function destroys all frames in the menu. This function is only called when user selects a page.
        toggleMenuFrame.destroy() #destroys all menu frames when menu is closed
        toggleBtn.config(text='☰') #sets menu icon
        toggleBtn.config(command=toggleMenu) #associates comamnd to togglemenu

    toggleMenuFrame = tk.Frame(root, bg='#4BA8A4')

    homeButton = tk.Button(toggleMenuFrame, text='Home', font=('Bold', 20), borderwidth=0, bg='#4BA8A4', fg='white', activebackground='#4BA8A4', activeforeground='white', highlightthickness=0, command=lambda: switchPage(homePage))
    homeButton.place(x=5, y=20)

    homeIndicate = tk.Label(toggleMenuFrame, text='', bg='#4BA8A4')
    homeIndicate.place(x=3, y=25, width=5, height=30)

    bookButton = tk.Button(toggleMenuFrame, text='Book', font=('Bold', 20), bd=0, bg='#4BA8A4', fg='white', activebackground='#4BA8A4', activeforeground='white', highlightthickness=0, command=lambda: switchPage(bookPage))
    bookButton.place(x=5, y=80)



    windowHeight = root.winfo_height()
    toggleMenuFrame.place(x=0, y=50, height=windowHeight, width=150)
    toggleBtn.config(text='X') #sets menu symbol to x when menu is open to show user how to close menu
    toggleBtn.config(command=collapseMenu)

def switchPage(page, flightChoice=None, pax=None, flightNumber=None, flightCode=None):
    #switch page function switches between pages and also acts as a hub where functions call pass arguements to one another. Essentially the hub of the code

    #if statement checks for what page is being switched to so that it can pass certain arguements to each page
    if page == orderPage:
        deletePages()
        page(flightChoice, pax)
    elif page == paymentPage:
        deletePages()
        page(flightChoice, pax, flightNumber, flightCode)
    elif page == confirmationPage:
        deletePages()
        page(flightChoice, pax, flightNumber, flightCode)
    else:
        deletePages()
        page()

#create banner at top of screen and set background colour to blue. Also set white border to frame
headFrame = tk.Frame(root, bg='#4BA8A4', highlightbackground='white', highlightthickness=1)

#create menu button for application. Set visual characteristics of button such as background colour
toggleBtn = tk.Button(headFrame, text='☰', bg='#4BA8A4', fg='white', font=('Bold', 20), bd=0, activebackground='#4BA8A4', activeforeground='white', highlightthickness=0, command=toggleMenu)
toggleBtn.pack(side=tk.LEFT)

#create title of application and set characterstics like font and size
titleLable = tk.Label(headFrame, text='SkyToronto ✈', bg='#4BA8A4', fg='white', font=('Bold', 20))
titleLable.pack(side=tk.LEFT)


#fill the frame of the banner and position it at the top of the screen
headFrame.pack(side=tk.TOP, fill=tk.X)
headFrame.pack_propagate(False)
#set size of banner to 50 pixels
headFrame.configure(height=50)
flightNumberFinal = 0
listFlights =[] #initalizes list to store filtered flights in
listFlightsCount = [] #initalizes list to count number of flights and stores as seperate items
def searchFilter(direction, destination, month, pax): #search filter to search for flights
    global listFlights
    global flightNumberFinal
    listFlights.clear() #clears listFlights list from previous searches to provide accurate searches
    flightsFound = 0 #sets flightsFound value to 0 before searching

    file = open("Flights.txt", "r") #opens text file to access database
    lines = file.readlines() #stores all lines in file to list called lines
    file.close() #closes file after storing all values

    for line in lines: #goes through each line in file to check if they meet the conditions of the if statement
        global flightNumberFinal
        seats = re.split(r'seats="|,', line)
        seatsAvailable = int(seats[-3])
        try:
            if direction=="Leaving From" and "origin=\""+destination.lower()+"\"" in line and month in line and seatsAvailable >= int(pax):
                global flightNumberFinal

                #following line of code splits the content of filtered flights into more manageable and readable values
                nextDestination = re.split(r'destination="|", duration=', line)
                flightsFound = flightsFound+1
                originDestination = re.split(r'"origin="|", destination=', line)
                flightNumber = re.split(r'flight="|", airline="', line)
                flightNumberFinal = flightNumber
                departureDate = re.split(r'departureTime="|", seats="', line)
                airline = re.split(r'airline="|", departureTime="', line)
                seatsLeft = re.split(r'seats="|,', line)
                priceTicket = re.split(r'price="|,', line)
                priceTicketNew = priceTicket[-2].replace("price=$", "")
                flightInfo=(originDestination[1].capitalize()+" To "+nextDestination[1].capitalize()+ " | "+airline[1]+" ("+flightNumber[1]+")"+ " | Seats Available: "+seatsLeft[-3]+" | Depature: "+departureDate[-2]+" | Price: "+priceTicketNew)
                listFlights.append(flightInfo)
                inputSpreadsheet(pax) #calls input spreadsheet function to input data of filtered flights into spreadsheet for user to see
            elif direction=="Going To" and "destination=\""+destination.capitalize()+"\"" in line and month in line and seatsAvailable >= int(pax):

                #following line of code splits the content of filtered flights into more manageable and readable values
                nextDestination = re.split(r'destination="|", duration=', line)
                originDestination = re.split(r'"origin="|", destination=', line)
                flightNumber = re.split(r'flight="|", airline="', line)
                flightNumberFinal = flightNumber
                departureDate = re.split(r'departureTime="|", seats="', line)
                airline = re.split(r'airline="|", departureTime="', line)
                seatsLeft = re.split(r'seats="|,', line)
                priceTicket = re.split(r'price="|,', line)
                priceTicketNew = priceTicket[-2].replace("price=$", "")
                flightInfo=(originDestination[1].capitalize()+" To "+nextDestination[1].capitalize()+ " | "+airline[1]+" ("+flightNumber[1]+")"+ " | Seats Available: "+seatsLeft[-3]+" | Depature: "+departureDate[-2]+" | Price: "+priceTicketNew)
                listFlights.append(flightInfo)
                inputSpreadsheet(pax) #calls input spreadsheet function to input data of filtered flights into spreadsheet for user to see
        except TypeError:
            break #prevent errors occuring if no search criteria is met


tree = None #assigns temp value for tree. Intitalizes variable so code knows that tree exists
flightSelected = 0 #assigns temp value for the user choice

def inputSpreadsheet(pax=None): #function to display all filtered flights to user
    global listFlightsCount
    global tree
    listFlightsCount.clear()
    for i in range(len(listFlights)): #checks for how many filtered flights there are by checking length
        listFlightsCount.append(i+1) #appens one to each listFlightsCount which counts amount of flights

    flightSelection = tk.StringVar()
    flightSelection.set("Flight Number") #sets default name of dropdown menu so user knows purpose of menu
    dropdownFlights = tk.OptionMenu(mainFrame, flightSelection, *listFlightsCount) #creates a dropdown menu where user can select the flight number they want to book. Uses values in listFlightCount to show how many flights they can book
    dropdownFlights.place(x=330, y=79)
    dropdownFlights.config(width=11)
    bookButton = tk.Button(mainFrame, text='Book Flight', font=('Bold', 10), fg='black', activebackground='#4BA8A4', activeforeground='black', bd=2, command=lambda: switchPage(orderPage, flightSelected, pax)) #switches page to orderPage when user clicks the book flight button
    bookButton.config(width=10)
    bookButton.place(x=450, y=80)
    def selectFlightMenu(event):
        global flightSelected
        selectedValue = flightSelection.get()
        flightSelection.set(selectedValue)
        flightSelected = selectedValue #stores selected flight number user wants to book into flightSelected value
    dropdownFlights.bind("<ButtonRelease-1>", selectFlightMenu) #whenever button is released, it calls function to update value of variable live
    flightSelection.trace("w", lambda *args: selectFlightMenu(None))

    if tree is None: #checks if there is already a spreadsheet in the frame. If there isn't it creates a spreadsheet and displays all data
        tree = ttk.Treeview(mainFrame, columns="col1")
        tree.column("col1", minwidth=100, width=620)
        tree.configure(height=15)
        tree.heading("#0", text="Flights")
        tree.column("#0", minwidth=25, width=75)
        tree.heading("col1", text="Details")
        vbar = ttk.Scrollbar(mainFrame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=vbar.set)
        vbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.place(x=0, y=110)
    else: #if there is, it deletes all rows (children) of the spreadsheet
        tree.delete(*tree.get_children())
    for i, item in enumerate(listFlights): #checks for item in listFlights, and puts each item in the list as a seperate row in the spreadsheet
        tree.insert("", "end", text="Flight "+str(i+1), values=(item,)) #inserts rows into spreadsheet displaying file



root.mainloop()
