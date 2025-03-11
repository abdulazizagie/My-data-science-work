from urllib import response
import requests as re
import bs4



url = input("Enter your URL")
response = re.get(url)
print(type(response))
print(response.text)
