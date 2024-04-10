import requests
import smtplib, ssl

api_key = "8d5b86b98fd74d02b6e23f6a647bd8fb"
url = "https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=8d5b86b98fd74d02b6e23f6a647bd8fb"

# make request
request = requests.get(url)
# content = request.text --> gives the output in str format

#Get a dictionary with data
content = request.json()
username = "pranithatwitteracct@gmail.com"
password = "wzru dddv yaih atti"

host = "smtp.gmail.com"
port = 465
receiver = "pranithatwitteracct@gmail.com"
context = ssl.create_default_context()

#Access the article tirles and description
for article in content["articles"]:
    title = article["title"]
    desc = article["description"]
    message = f"""\
     From :{username}
     Subject : {title}\
     {desc}
     """
    print(message)

message = message.encode("utf-8")
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)


