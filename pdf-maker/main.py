from fpdf import FPDF
import pandas

pdf = FPDF(orientation="P", unit="mm",format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pandas.read_csv("topics.csv")

for index, row in df.iterrows():
    for no_of_pages in range(row["Pages"]):
        if no_of_pages == 0:
            
            pdf.add_page()

            # Set the header
            pdf.set_font(family="Times", style="B", size=24)
            pdf.set_text_color(100, 100, 100)
            # pdf.line(10, 21, 200, 21)

            pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

            # Insert lines in the page
            for y in range(20, 298, 10):
                pdf.line(10, y, 200, y)

            # Set the footer
            pdf.ln(266)
            pdf.set_font(family="Times", style="I", size=10)
            pdf.set_text_color(180, 180, 180)
            pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


        else:
            pdf.add_page()
        
            # Insert lines in the page
            for y in range(20, 298, 10):
                pdf.line(10, y, 200, y)
        
            # Set the footer
            pdf.ln(278)
            pdf.set_font(family="Times", style="I", size=10)
            pdf.set_text_color(180, 180, 180)
            pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")
