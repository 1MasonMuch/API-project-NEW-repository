from tkinter import *
import requests

root = Tk()

api = requests.get(f"https://api.frankfurter.dev/v1/latest?base=USD")
data = api.json()
rates = data["rates"]

def convert():
  for i in api:
    if choose_currency.get == i[data]:
      amt = amt * i[rates]
      total = Label(root, text = amt + choose_currency.get)
      total.grid(row = 3, column = 0)

choose_currency = Entry(root, width = 10, borderwidth = 2)
currency_input = Label(root, text = "Input a currency you would like to convert USD to:", font = "Arial")
submit = Button(root, text="Submit", padx= 5, pady= 5, command= convert)
amt = Entry(root, width = 10, borderwidth= 2)


currency_input.grid(row = 0, column = 0)
choose_currency.grid(row = 1, column = 0)
submit.grid(row = 3, column = 0)


root.mainloop()