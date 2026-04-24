# strted on: 14/04/26

import tkinter as tk
window = tk.Tk()
window.title('Mortgage Calculator')
window.geometry('350x250')

# How much is the property?
property_price = tk.Label(
    window, text="How much is the property? ", font=("Arial", 11))
property_price.place(x=90,y=10)
property_price_pound = tk.Label(window, text="£", font=("Arial", 11))
property_price_pound.place(x=90,y=30)
property_price_entry = tk.Entry(
    window, text="How much is the property?", font=("Arial", 11))
property_price_entry.place(x=100,y=30)

# How much do you want to pay as a deposit?

property_deposit = tk.Label(
    window, text="How much do you want to pay as a deposit?", font=("Arial", 11))
property_deposit.place(x=90,y=50)
property_deposit_pound = tk.Label(window, text="£", font=("Arial", 11))
property_deposit_pound.place(x=90,y=70)
property_deposit_entry = tk.Entry(window, font=("Arial", 11))
property_deposit_entry.place(x=100,y=70)

# How many years will the term on your mortgage be?

years_of_mortgage = tk.Label(
    window, text="How many years will the term be on your mortgage?", font=("Arial", 11), )
years_of_mortgage.place(x=90,y=90)
years_of_mortgage_entry = tk.Entry(window, font=("Arial", 11))
years_of_mortgage_entry.place(x=100,y=110)
years_pound = tk.Label(window, text="years", font=("Arial", 11))
years_pound.place(x=250,y=110)

# How much is the annual interest rate?

interest = tk.Label(
    window, text="How much is the annual interest rate?", font=("Arial", 11))
interest.place(x=90,y=130)
interest_entry = tk.Entry(window, font=("Arial", 11))
interest_entry.place(x=100,y=150)
years_pound = tk.Label(window, text="%", font=("Arial", 11))
years_pound.place(x=250,y=150)

# Define a button function

def calculate_mortgage_button():
    principlal = float(property_price_entry.get())

    deposit = float(property_deposit_entry.get())

    principlal = principlal - deposit
    annual_interest_rate = float(interest_entry.get())/100

    term = float(years_of_mortgage_entry.get())

    monthly_payment = principlal * \
        (annual_interest_rate/12)/1-(1 + annual_interest_rate/12)**-12*term
    monthly_payment = round(monthly_payment, 2)
    monthly_payment_label = tk.Label(
        window, text=f"Your monthly payments are: £{monthly_payment}", font=("Arial", 11))
    monthly_payment_label.place(x=90,y=190)

# Mortgage calculator button

mortgage_button = tk.Button(
    window, text='Calculate monthly mortgage payments', command=calculate_mortgage_button)
mortgage_button.config(command=calculate_mortgage_button)
mortgage_button.config(font=('Arial', 11))
mortgage_button.place(x=90,y=170)

window.mainloop()

# completed on: 22/04/26
