import requests

# https://newsapi.org/

api_key = "0104be7090ad48f9ad65a4ca468f544a"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-09-01&sortBy=" \
      "publishedAt&apiKey=0104be7090ad48f9ad65a4ca468f544a"

website = requests.get(url)
content = website.text
print(content)
