from pathlib import Path
from fpdf import FPDF
import glob

# Create one PDF file
pdf = FPDF(orientation="P", unit="mm",format="A4")

filepaths = sorted(glob.glob("text_files/*.txt"))

for filepath in filepaths:
    # add page to the pdf
    pdf.add_page()

    # extract filename
    filename = (Path(filepath).stem).title()

    # Set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=filename, align="L", ln=1)

    # Get the content of each file
    with open(filepath, "r") as file:
        content = file.read()
    # Add text file to the PDF
    pdf.set_font(family="Times", style="B", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

# produce the PDF
pdf.output("output.pdf")