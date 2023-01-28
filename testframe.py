import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#from backend import searchFilter
import re
import os



imagePAth='hiking.jpg'
root = tk.Tk()
root.geometry('700x500')
root.title('SkyToronto Flight Booking System')

mainFrame = tk.Frame(root, bg="#ffffff")
mainFrame.pack(side=tk.LEFT)
mainFrame.pack(side=tk.LEFT)
mainFrame.pack_propagate(False)
screenHeight = root.winfo_height()
mainFrame.place(x=0, y=50, height=500, width=700)
def mainFrameLayout():
    lb = tk.Label(mainFrame, text=' ☰ Home Page', font=('Trebuchet MS', 16), bg="#ffffff")
    lb.place(x=0, y=0)
    titleLable = tk.Label(mainFrame, text='Welcome to SkyToronto, the most convenient way to escape the cold!', font=('Trebuchet MS', 16), wraplength=600, bg="#ffffff")
    titleLable.place(x=50, y=50)
    titleDesc = tk.Label(mainFrame, text='We have helped over 25,000 travellers visit their dream destinations in just a few steps', font=('Trebuchet MS', 13), wraplength=600, bg="#ffffff")
    titleDesc.place(x=50, y=110)
    bookButton = tk.Button(mainFrame, text='Book Now!', font=('Bold', 20), fg='black', activebackground='#158aff', activeforeground='black', bd=2, command=lambda: indicateButton(bookPage))
    bookButton.place(x=260, y=180)

    # Create a photoimage object of the image in the path



def deletePages():
    for frame in mainFrame.winfo_children():
        frame.destroy()

def paymentPage():
    paymentFrame = tk.Frame(mainFrame)
    #img = ImageTk.PhotoImage(Image.open(imagePAth).resize((150, 250)))
    #lbl = tk.Label(root, image=img)
    #lbl.img = img
    #lbl.place(relx=0.5, rely=0.5, y=0, x=0)
    pageTitle = tk.Label(mainFrame, text='Payment Page', font=('Trebuchet MS', 16), bg='#ffffff')
    pageTitle.place(x=root.winfo_width()/2, y=50, anchor='center')
    def check_payment():
        card_number = card_number_entry.get()
        cvv = cvv_entry.get()
        date = date_entry.get()
        card_number = card_number.replace(" ", "")

        # check if inputs are valid
        if not card_number.isdigit() or len(card_number) != 16:
            messagebox.showerror("Invalid Input", "Invalid card number")
        elif not cvv.isdigit() or len(cvv) != 3:
            messagebox.showerror("Invalid Input", "Invalid CVV")
        elif len(date)!=5 or "/" not in date:
            messagebox.showerror("Invalid Input", "Invalid date")
        else:
            messagebox.showinfo("Payment Successful", "Payment has been processed successfully")


    card_number_label = tk.Label(mainFrame, text="Card Number:")
    card_number_label.place(x=350, y=150, anchor='center')
    #card_number_label.place(x=100, y=100)

    card_number_entry = tk.Entry(mainFrame)
    card_number_entry.place(x=350, y=180, anchor='center')
    #card_number_entry.pack()

    cvv_label = tk.Label(mainFrame, text="CVV:")
    cvv_label.place(x=350, y=220, anchor='center')

    cvv_entry = tk.Entry(mainFrame)
    cvv_entry.place(x=350, y=250, anchor='center')

    date_label = tk.Label(mainFrame, text="Date:")
    date_label.place(x=350, y=290, anchor='center')

    date_entry = tk.Entry(mainFrame)
    date_entry.place(x=350, y=320, anchor='center')
    date_entry.pack()

    submit_button = tk.Button(mainFrame, text="Submit", command=check_payment)
    submit_button.pack()

    paymentFrame.pack(pady=20)

paymentPage()