# :arrow_down_small: CSV to PDF

CSV to PDF is a python script used to feed info from a CSV into a pdf file. In order to be able to use the script you'd need to have a compatible data.csv and form.pdf

## :arrow_forward: What CSV Stands For ?

**CSV** stands for **Comma Separated Values File** is just like a plain file that uses
a different approach for structuring data.

If you open a csv file in Sublime Text you will find simple plain text separated with
commas

**Example**

```
id,name,email,amount,date,sent
1,Hopper,email-address,269,03 Sep at 21:14,False
2,Drake,email-address,690,03 Sep at 21:14,False
3,Adam,email-address,20,03 Sep at 21:14,False
4,Justin,email-address,199,03 Sep at 21:14,False
```

In general, the separator character is called a delimiter, and the comma is not the
only one used. Other popular delimiters include the tab (\t), colon (:) and semi-colon
(;) characters. Properly parsing a CSV file requires us to know which delimiter is
being used.

CSV files are very useful for handling large chunk of data and this type of data can be
very easily handled with any programming language which supports string handling like
python.

## :question: Problem Solved

From the values of the CSV one might want to be able to feed those information into a PDF form. It's in that vein that csvtopdf was created.

## :hammer_and_wrench: Usage

1. Install python

2. Clone repo

```bash
git clone https://github.com/pdd27673/csvtopdf.git
```

3. Import correct **_data.csv_** and **_form.pdf_** in folder

4. Run csvtopdf.py

```bash
python3 csvtopdf.py
```

## :raised_hands: Contributing

Features being worked on:

1. Adding support for all **_.csv_** files
2. Adding support for an .exe compacted version

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
