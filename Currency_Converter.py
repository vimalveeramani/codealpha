import requests
import tkinter as tk
from tkinter import ttk

def convert_currency(amount, from_currency, to_currency):
    base_url = "https://api.exchangerate-api.com/v4/latest/"

    
    response = requests.get(base_url + from_currency)
    data = response.json()

    if 'rates' in data:
        rates = data['rates']
        if from_currency == to_currency:
            return amount

        if from_currency in rates and to_currency in rates:
            conversion_rate = rates[to_currency] / rates[from_currency]
            converted_amount = amount * conversion_rate
            return converted_amount
        else:
            raise ValueError("Invalid currency!")
    else:
        raise ValueError("Unable to fetch exchange rates!")

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        self.amount_label = ttk.Label(root, text="Amount:")
        self.amount_label.grid(row=0, column=0, padx=10, pady=10)

        self.amount_entry = ttk.Entry(root)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        self.from_currency_label = ttk.Label(root, text="From Currency:")
        self.from_currency_label.grid(row=1, column=0, padx=10, pady=10)

        self.from_currency_combobox = ttk.Combobox(root, values=["USD", "EUR", "GBP", "JPY", "CAD", "AUD","INR"])
        self.from_currency_combobox.grid(row=1, column=1, padx=10, pady=10)

        self.to_currency_label = ttk.Label(root, text="To Currency:")
        self.to_currency_label.grid(row=2, column=0, padx=10, pady=10)

        self.to_currency_combobox = ttk.Combobox(root, values=["USD", "EUR", "GBP", "JPY", "CAD", "AUD","INR"])
        self.to_currency_combobox.grid(row=2, column=1, padx=10, pady=10)

        self.convert_button = ttk.Button(root, text="Convert", command=self.perform_conversion)
        self.convert_button.grid(row=3, columnspan=2, padx=10, pady=10)

        self.result_label = ttk.Label(root, text="")
        self.result_label.grid(row=4, columnspan=2, padx=10, pady=10)

    def perform_conversion(self):
        amount = float(self.amount_entry.get())
        from_currency = self.from_currency_combobox.get()
        to_currency = self.to_currency_combobox.get()

        try:
            converted_amount = convert_currency(amount, from_currency, to_currency)
            self.result_label.config(text=f"{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
        except ValueError as e:
            self.result_label.config(text=str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
