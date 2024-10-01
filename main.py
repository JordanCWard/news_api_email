import requests

# https://newsapi.org/

api_key = "0104be7090ad48f9ad65a4ca468f544a"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-09-01&sortBy=" \
      "publishedAt&apiKey=0104be7090ad48f9ad65a4ca468f544a"

# Make a request
website = requests.get(url)

# Get a dictionary with data
content = website.json()

# Access the article titles and descriptions
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
