import pandas

df = pandas.read_csv("articles.csv", dtype={"id":str})

class Article:
    def __init__(self, article_id):
        self.article_id = article_id
        self.name = df.loc[df["id"] == self.article_id, "name"].squeeze()

    def available(self):
        """Checks if the article is available"""
        availability = df.loc[df["id"] == self.article_id, "instock"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReceiptGeneration:
    def __init__(self, article_object):
        self.article = article_object

    def generate(self):
        content = f"""
        Article Name: {self.article.name}
        """
        return content


print(df)
article_ID = input("Enter the id of the article: ")
article = Article(article_ID)
if article.available():
    receipt = ReceiptGeneration(article_object=article)
    print(receipt.generate())
else:
    print("Article does not exist")

