from datetime import datetime
import tabula
import pandas as pd

# Estrarre le tabelle dal file PDF
df = tabula.read_pdf("Rendiconto+Gestione+Patrimoniale+<moneyfarm>.pdf", pages='all', multiple_tables=True)

# Stampa le tabelle estratte
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

df = pd.DataFrame(pf, columns=["Date", "ISIN", "Type", "Qty", "Price", "Currency"])
df.to_csv("export_for_financedrip.csv", index=False)
          
