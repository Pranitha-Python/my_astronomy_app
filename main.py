import requests
from sendemail import send_email

topic = "telsa"
api_key = "8d5b86b98fd74d02b6e23f6a647bd8fb"
url = "https://newsapi.org/v2/everything?"\
       f"q={topic}&" \
        "sortBy=publishedAt&" \
        "apiKey=8d5b86b98fd74d02b6e23f6a647bd8fb&"\
        "language=en"

# make request
request = requests.get(url)
# content = request.text --> gives the output in str format

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article['title'] is not None:
        body = "Subject:Today's News" \
                + "\n" + body + article['title'] + "\n" \
               + str(article["description"]) \
               + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)


