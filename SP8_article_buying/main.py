import pandas
from fpdf import FPDF

df = pandas.read_csv("articles.csv", dtype={"id":str})

class Article:
    def __init__(self, article_id):
        self.article_id = article_id
        self.name = df.loc[df["id"] == self.article_id, "name"].squeeze()
        self.price = df.loc[df["id"] == self.article_id, "price"].squeeze()

    def available(self):
        """Checks if the article is available"""
        availability = df.loc[df["id"] == self.article_id, "instock"].squeeze()
        return availability


class ReceiptGeneration:
    def __init__(self, article_object):
        self.article = article_object

    def generate(self):
        pdf = FPDF(orientation="P", unit="mm",format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr. {self.article.article_id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.article.name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.article.price}", ln=1)

        pdf.output("receipt.pdf")
        # content = f"""
        # Article Name: {self.article.name}
        # """
        # return content
        df.loc[df["id"] == self.article.article_id, "instock"] = article.available() - 1
        df.to_csv("articles.csv", mode="w", index=False)
        

print(df)
article_ID = input("Enter the id of the article: ")
article = Article(article_ID)
if article.available():
    receipt = ReceiptGeneration(article_object=article)
    print(receipt.generate())
else:
    print("Article does not exist")

