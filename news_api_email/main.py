import requests, os
from send_email import send_email

topic = "tesla"

api_key = os.getenv("NEWS_API_KEY")
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2024-09-20" \
      "&sortBy=publishedAt&" \
      f"apiKey={api_key}&" \
      "language=en"

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()


# Access article title and description
body = "Subject: Today's News\n"
for article in content["articles"][0:20]:
    body = body + str(article["title"]) + "\n" \
         + str(article["description"]) \
         + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(body)

