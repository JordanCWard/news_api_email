import requests
from send_email import email_function

# Link for News API: https://newsapi.org/

topic = "tesla"

api_key = "0104be7090ad48f9ad65a4ca468f544a"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&sortBy=publishedAt&" \
      "apiKey=0104be7090ad48f9ad65a4ca468f544a&language=en"

# Get a JSON dictionary with the data
website = requests.get(url)
content = website.json()

# Combine 20 news articles into a string to send in an email
all_text = "Subject: Today's News"
for article in content["articles"][0:20]:
    all_text = all_text + "\n" + article["title"] \
               + '\n' + str(article["description"]) + "\n" \
               + article["url"] + 2*'\n'

# Encode the articles to a readable format
all_text = all_text.encode("utf-8")

# Send the string in an email
email_function(all_text)
