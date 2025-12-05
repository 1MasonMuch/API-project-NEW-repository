from tkinter import *
import requests
root = Tk()
api = requests.get(f"https://api.frankfurter.dev/v1/latest?base=USD")
data = api.json()

#def convert():
 #   for i in api:
  #      if choose.get == i[api]:
        

choose_currency = Entry(root, width = 10, borderwidth = 2)
currency_input = Label(root, text = "Input a currency you would like to convert USD to:", font = "Arial")

choose_currency.grid(row = 1, column = 0)
choose_currency.grid(row = 0, column = 0)



root.mainloop()