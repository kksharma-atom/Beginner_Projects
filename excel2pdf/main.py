import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    # loading dataframe from excel
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    # creating instance of FPDF 
    pdf = FPDF(orientation="P", unit="mm",format="A4")
    pdf.add_page()
    # extracting invoice number and date from filepath
    filename = Path(filepath).stem
    invoice_nr = filename.split("-")[0]
    date = filename.split("-")[1]

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice No. {invoice_nr} \n\n {date}")
    

    pdf.output(f"PDFs/{filename}.pdf")