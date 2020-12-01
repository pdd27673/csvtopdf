# Import TK, CSV and PyPDFTK
import tkinter as tk
from tkinter.constants import END
from tkinter.filedialog import askopenfilename
import csv

import pypdftk

# Handler functions
def import_pdf():
    global x
    global b
    pdf_path_file = askopenfilename()
    b = pdf_path_file
    x.set(pdf_path_file)
    results_field.delete(0, END)

def import_csv_data():
    global v
    global c
    csv_file_path = askopenfilename()
    c = csv_file_path
    v.set(csv_file_path)
    results_field.delete(0, END)

def clear():
    global c
    global b
    data_field.delete(0, END)
    form_field.delete(0, END)
    results_field.delete(0, END)
    del c, b

# Conversion function
def convert():
    # Check if data.csv has been provided
    try:
        c
    # Error if not provided
    except NameError:
        y.set('Data.csv file has not been provided. Try again.')
    # Making Files
    else:
        with open(c) as csv_file:
            # read csv elements
            csv_reader = csv.reader(csv_file, delimiter=',')

            # variables holder
            line_count = 0

            # loop each row to read elements
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    # pull values
                    name = row[26]
                    invDate = row[1]
                    invID = row[11]
                    invAddress = row[30]
                    invAccount = row[13]
                    fund = row[14]
                    dept = row[15]
                    amt = row[10]
                    city = row[34]
                    state = row[35]
                    postal = row[36]

                    lastName, firstName = name.split('*', 1)
                    firstName = firstName.lstrip()

                    data = {
                        "First Name": f"{firstName}",
                        "Last Name": f"{lastName}",
                        "City": f"{city}",
                        "State": f"{state}",
                        "Zip Code": f"{postal}",
                        "Account": f"{invAccount}",
                        "Fund": f"{fund}",
                        "Department": f"{dept}",
                        "Amount": f"{amt}",
                        "Street Address": f"{invAddress}",
                        "Account Date": f"{invDate}",
                        "Invoice ID": f"{invID}"
                    }
                    # Creating file name
                    file_name = f'{lastName},{firstName}.pdf'
                    # Filling form
                    pypdftk.fill_form(b, data, file_name)
                    line_count += 1

            print(f'Processed {line_count-1} lines.')
            y.set(f'Processed {line_count-1} lines.')

# GUI Stuff, ugh
root = tk.Tk()

# Window properties
root.title("CSV to PDF")
root.geometry("300x355")

# Field holding values
v = tk.StringVar()
x = tk.StringVar()
y = tk.StringVar()

# Widgets

## Messages
welcome_message = tk.Label(root, text='Welcome to CSV to PDF Form filler :)')
instructions_message = tk.Label(
    root, text='To use this program you\'ll need: \n1. Select a data.csv file \n2. Select your form.pdf \n3. Click run!')

## Data Fields
data_field = tk.Entry(root, textvariable=v, width=30)
form_field = tk.Entry(root, textvariable=x, width=30)
results_field = tk.Entry(root, textvariable=y, width=30, )

## Buttons
data_button = tk.Button(root, text='Select data.csv', highlightbackground='blue', font=18,command=import_csv_data)
form_button = tk.Button(root, text='Select form.pdf', highlightbackground='blue', font=18,command=import_pdf)

convert_button = tk.Button(root, text='Run', highlightbackground='green', command=convert)
clear_button = tk.Button(root, text='Clear', highlightbackground='red', command=clear)

# Organizing on GUI.
instructions_message.grid(row=1, column=0, columnspan=2)
welcome_message.grid(row=0, column=0, columnspan=2)

data_field.grid(row=2, column=0, columnspan=2)
form_field.grid(row=3, column=0, columnspan=2)

data_button.grid(row=4, column=0, padx=5, pady=2)
form_button.grid(row=4, column=1, padx=5, pady=2)

convert_button.grid(row=5, column=0, padx=5, pady=10)
clear_button.grid(row=5, column=1)

results_field.grid(row=6, column=0, ipady=30, columnspan=2)

root.mainloop()
