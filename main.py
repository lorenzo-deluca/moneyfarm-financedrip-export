import sys
import os
import glob

from datetime import datetime
import tabula
import pandas as pd

if len(sys.argv) > 1:
    file_pdf = sys.argv[1]
else:
    file_pdf = glob.glob(os.path.join(os.getcwd(), '*.pdf'))[0]

if not os.path.exists(file_pdf):
    print (f"File {file_pdf} not found")
    exit(1)

print (f"Analyzing File: {file_pdf}")

try:
    # Exstract tables from pdf
    df = tabula.read_pdf(file_pdf, pages='all', multiple_tables=True)

    # Spread tables in a list
    pf = []

    for table in df:
        if "TITOLO" in table.columns[0]:
            table.drop(range(2), inplace=True)
            print(table)

            # scorro righe a due a due
            for row1, row2 in zip(table.iloc[::2].itertuples(), table.iloc[1::2].itertuples()):
                if not pd.isna(row1[1]):
                    titolo = row1[1]
                    riga = []
                    riga.append(datetime.today().strftime('%d-%m-%Y'))

                    qty = row1[4].split(" ")[0]
                    pmc = row1[4].split(" ")[1]
                    isin = row2[1].replace("Cod.", "").replace("Div.", "").strip()
                    div = "EUR"

                    print (f"ISIN: {isin}, Titolo: {titolo}, Quantità: {qty}, PMC: {pmc}")
                    riga.append(isin)
                    riga.append('B')
                    riga.append(float(qty.replace(',', '.')))
                    riga.append(float(pmc.replace(',', '.')))
                    riga.append(div)

                    pf.append(riga)

    # Export to csv
    print ("Exporting to export_for_financedrip.csv")
    df = pd.DataFrame(pf, columns=["Date", "ISIN", "Type", "Qty", "Price", "Currency"])
    df.to_csv("export_for_financedrip.csv", index=False)

except Exception as e:
    print (f"Error: {e}")
    exit(1)
