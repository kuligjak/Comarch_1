# -*- coding: utf-8 -*-

"""
Prosty skrypt do generowania pliku Markdown
https://www.markdownguide.org/basic-syntax/
"""
import snakemd
from snakemd import Paragraph, InlineText
import pandas as pd
import subprocess #wywołanie poleceń systemowych!!!

df = pd.read_csv('dane_sprzedazowe.csv', sep=';')
print(df)

doc = snakemd.new_doc("simple_md_file")
my_par_cars = "Tutaj opisujemy wyniki sprzedaży samochodów"
my_par_boats = "Tutaj opisujemy wyniki sprzedaży łodzi"
table_header = ['Rok', 'Sprzedaż Kart 5GB', 'Sprzedaż Abonamentów', 'Sprzedaż Światłowodów']
doc.add_header("Raport sprzedaży 2022", 1)
doc.add_horizontal_rule()
# Paragraf z pochyłym tekstem:
doc.add_element(Paragraph([InlineText("Test DataFrame", italics=True)]))

data_sales = df.values.tolist()
doc.add_table(table_header,
              data_sales,)

print(data_sales)

doc.add_header("1. Sprzedaż samochodów", 3)
doc.add_horizontal_rule()
doc.add_paragraph(my_par_cars)
doc.add_header("2. Sprzedaż łodzi", 3)
doc.add_horizontal_rule()
doc.add_paragraph(my_par_boats)

doc.output_page()

ret_code = None
try:
    ret_code = subprocess.run([".\pandoc", "-o", "dokument.docx", "simple_md_file.md"], capture_output=True)
    print(ret_code)
except:
    print("Error")
