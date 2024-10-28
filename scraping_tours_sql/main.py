import requests, time
import selectorlib
from emailing import send_email
import sqlite3

# INSERT INTO events VALUES('Agnee','Mumbai','2024.11.06')
# SELECT * FROM events WHERE band='Indian Ocean'
# DELETE FROM events WHERE band='Agnee'

connection = sqlite3.connect("data.db")


URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def scrape(url):
    "Scrape the page source from the URL"
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value

def store(extracted):
    # with open("data.txt", "a") as file:
    #     file.write(extracted + "\n")
    row = extracted.split(",")
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
    connection.commit()

def read(extracted):
    # with open("data.txt", "r") as file:
    #     return file.read()
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band, city, date = row

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
    rows = cursor.fetchall()
    return rows

if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        if extracted != "No upcoming tours":
            row = read(extracted)
            # if extracted not in content:
            if not row:
                store(extracted)
                send_email(extracted)
        time.sleep(3)