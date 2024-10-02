import requests
from send_email import email_function

# https://newsapi.org/

api_key = "0104be7090ad48f9ad65a4ca468f544a"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-09-02&" \
      "sortBy=publishedAt&apiKey=0104be7090ad48f9ad65a4ca468f544a"

# Make a request
website = requests.get(url)

# Get a dictionary with the data
content = website.json()

# Write all titles and descriptions to a string
all_text = ""
for article in content["articles"]:
    all_text = all_text + article["title"] + '\n' \
               + str(article["description"]) + 2*'\n'

# Remove extra lines and spaces
remove_new_lines = all_text.strip()
# Encode the code
encoded_text = remove_new_lines.encode("utf-8")

# Send the string in an email
email_function(encoded_text)
