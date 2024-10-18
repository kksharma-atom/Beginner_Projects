import requests
import streamlit as st

# Prepare API key and API url
api_key = "fm7BX6T8AE0UooOjbyXFw4s5IyNL9YzTDmF9WTx7"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"

# Get the data as dictionary
response1 = requests.get(url)
content = response1.json()

# Extract data
title = content['title']
image_url = content['url']
description = content['explanation']

# Download the image
response2 = requests.get(image_url)
with open("image.jpg", "wb") as file:
    file.write(response2.content)

# Render data on the web page 
st.title(title)
st.image("image.jpg")
st.write(description)




