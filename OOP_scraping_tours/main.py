import requests, time
import selectorlib
from emailing import Email
import sqlite3


URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

class Event:
    def scrape(self, url):
        "Scrape the page source from the URL"
        response = requests.get(url, headers=HEADERS)
        source = response.text
        return source

    def extract(self, source):
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(source)["tours"]
        return value
    
class Database:
    def __init__(self, database_path):
        self.connection = sqlite3.connect("data.db", database_path)
        
    def store(self, extracted):
        # with open("data.txt", "a") as file:
        #     file.write(extracted + "\n")
        row = extracted.split(",")
        row = [item.strip() for item in row]
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
        self.connection.commit()

    def read(self, extracted):
        # with open("data.txt", "r") as file:
        #     return file.read()
        row = extracted.split(",")
        row = [item.strip() for item in row]
        band, city, date = row

        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
        rows = cursor.fetchall()
        return rows

if __name__ == "__main__":
    while True:
        event = Event()
        scraped = event.scrape(URL)
        extracted = event.extract(scraped)
        print(extracted)
        if extracted != "No upcoming tours":
            database = Database(database_path="data.db")
            row = database.read(extracted)
            # if extracted not in content:
            if not row:
                database.store(extracted)
                email = Email()
                email.send(extracted)
        time.sleep(3)