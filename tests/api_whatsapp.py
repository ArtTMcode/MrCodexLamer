# import requests

# phone = "79771730759"

# url = "https://whatsapp.checkleaked.cc/" + phone
# params = {
#     # "token": "1234567890"
# }
# req = requests.get(url, params=params)

# with open('page.html', 'wb') as file:
#     file.write(req.content)

# import requests

# url = "https://whatsapp-data1.p.rapidapi.com/number/59898297150"

# headers = {
# 	"x-rapidapi-key": "8324bd4d75msh953a6d713508a9dp169e9djsn3a3e89f0ff64",
# 	"x-rapidapi-host": "whatsapp-data1.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers)

# print(response.json())

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

phone = "79771730759"
url = "https://whatsapp.checkleaked.cc/" + phone
driver.get("https://whatsapp.checkleaked.cc/")

input("Нажмите любую клавишу для продолжения...")




