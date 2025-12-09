from tkinter import *
import ttkbootstrap as ttk
import requests

root = Tk()

# Get API data
api = requests.get("https://api.frankfurter.dev/v1/latest?base=USD")
data = api.json()
rates = data["rates"]

def convert():
    currency = choose_currency.get().upper() 
    amount = float(amt_entry.get()) 
    
    if currency in rates:
        converted = amount * rates[currency]
        result_label.config(text=f"{amount} USD = {converted:.2f} {currency}")
    else:
        result_label.config(text="Currency not found!")

#def dark_mode():
    

#__________________________________________________________________________________
root.columnconfigure(0, weight=1) 
root.rowconfigure(0, weight=1)    



# Widgets
currency_input = Label(root, text="Currency to convert USD → ?", font=("Arial", 14))
choose_currency = Entry(root, width=10, borderwidth=2)

amt_label = Label(root, text="Amount in USD:")
amt_entry = Entry(root, width=10, borderwidth=2)

submit = Button(root, text="Submit", padx=5, pady=5, command=convert)
result_label = Label(root, text="", font=("Arial", 12))

# placement
currency_input.grid(row=0, column=0)
choose_currency.grid(row=1, column=0)

amt_label.grid(row=2, column=0)
amt_entry.grid(row=3, column=0)

submit.grid(row=4, column=0, pady=10)
result_label.grid(row=5, column=0)

root.mainloop()
