import requests

url = "https://api.nasa.gov/planetary/apod?api_key=GAvNVTuWPatl4VEbMkXgSHiMXKePC4hfoqFhqyWS"
image = requests.get(url)
image = image.json()
#print(image)
hdurl = image["hdurl"]
explaination = image["explanation"]
titl = image["title"]
response = requests.get(hdurl)
filename = "picture.jpg"
with open(filename, "wb") as file:
    file.write(response.content)
