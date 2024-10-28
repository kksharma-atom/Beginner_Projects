import requests, selectorlib
from datetime import datetime
import time

URL = "https://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def scrape(url):
    response = requests.get(url, headers=HEADERS)
    return response.text

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    return extractor.extract(source)["temperatures"]

def store(time1, extracted):
    with open("data.txt", "a") as file:
        # file.write(time1 + "," + extracted + "\n")
        file.write(f"{time1},{extracted}\n")


if __name__ == "__main__":
    while True:
        source = scrape(URL)
        extracted = extract(source)

        time1 = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")  
        store(time1, extracted)

        time.sleep(3)

       