from tkinter import filedialog
import tkinter as tk
from tkinter.constants import END
from tkinter.filedialog import askopenfilename
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen.canvas import Canvas
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
import csv


def clear():
    entry.delete(0, END)


def import_csv_data():
    global v
    global c
    csv_file_path = askopenfilename()
    c = csv_file_path
    print(csv_file_path)
    v.set(csv_file_path)


def convert():
    with open(c) as csv_file:
        # read csv elements
        csv_reader = csv.reader(csv_file, delimiter=',')

        # variables holder
        line_count = 0
        name = ''
        invAddress = ''
        city = ''
        state = ''
        postal = ''
        invDate = ''
        invID = ''
        invAccount = ''
        fund = ''
        dept = ''
        amt = ''

        # loop each row to read elements
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                # pull values
                invDate = row[1]
                invID = row[7]
                invAddress = row[14]
                invAccount = row[8]
                fund = row[9]
                dept = row[10]
                amt = row[5]
                name = row[11]
                city = row[15]
                state = row[16]
                postal = row[17]

                # separate first name from last name
                lastName, firstName = name.split('*')

                # making files
                packet = io.BytesIO()
                canvas = Canvas(packet, pagesize=LETTER)
                canvas.setFont("Times-Roman", 12)

                # adding values to document
                canvas.drawString(105, 720, invDate)
                canvas.drawString(330, 710, invID)
                canvas.drawString(142, 605, firstName)
                canvas.drawString(142, 580, lastName)
                canvas.drawString(142, 535, invAddress)
                canvas.drawString(142, 505, city)
                canvas.drawString(100, 470, state)
                canvas.drawString(100, 445, postal)
                canvas.drawString(70, 355, invAccount)
                canvas.drawString(190, 355, fund)
                canvas.drawString(330, 355, dept)
                canvas.drawString(465, 355, amt)

                canvas.save()

                # move to the beginning of the StringIO buffer
                packet.seek(0)
                new_pdf = PdfFileReader(packet)

                # read your existing PDF
                existing_pdf = PdfFileReader(open("form.pdf", "rb"))
                output = PdfFileWriter()

                # add the "watermark" (which is the new pdf) on the existing page
                page = existing_pdf.getPage(0)
                page.mergePage(new_pdf.getPage(0))
                output.addPage(page)

                # finally, write "output" to a real file
                outputStream = open(f"{lastName},{firstName}.pdf", "wb")
                output.write(outputStream)
                outputStream.close()

                line_count += 1

        print(f'Processed {line_count} lines.')


root = tk.Tk()

root.title("CSV to Python")
root.geometry("500x175")
root.iconphoto(False, tk.PhotoImage(file='icon.png'))
v = tk.StringVar()

label = tk.Label(root, text='Please select your compatible data.csv file')
label2 = tk.Label(
    root, text='to use this program you\'d need a data.csv file and a form.pdf file in the same window')
entry = tk.Entry(root, textvariable=v, width=30)
button = tk.Button(root, text='Browse files', command=import_csv_data)
convert_button = tk.Button(root, text='Convert', command=convert)
clear_button = tk.Button(root, text='Clear', command=clear)

label2.grid(row=0, column=0, columnspan=2)
label.grid(row=1, column=0)
entry.grid(row=1, column=1, columnspan=2)
button.grid(row=2, column=1, padx=5, pady=3)
convert_button.grid(row=2, column=2, padx=5, pady=3)
clear_button.grid(row=3, column=1)

root.mainloop()
