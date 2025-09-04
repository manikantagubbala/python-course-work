# WebScraping.py

import pandas as pd
import requests
from bs4 import BeautifulSoup

URL = "https://timely-sunshine-e821b3.netlify.app/"

# Loading the WebPage in Memory using requests library
page = requests.get(URL)

# Check the Status Code Of the Page
page.status_code

htmlcode = page.text
print(htmlcode)
print("\n\n\n")

soup = BeautifulSoup(htmlcode, 'html.parser')
print(soup)

content = soup.find_all('div',attrs={'class':'a'})
for i in content:
  print("Div:{a}",i,end="\n\n\n\n\n")


content1 = soup.find('div', attrs={'class' : 'image'})
print(content1)

####
####

items = soup.find_all('div', class_ = 'a')

# Lists to store extracted data
names = []
prices = []
images = []

# Loop through each item and extract details
for item in items:
  name = item.find('div', class_ = "name").text.strip()
  price = item.find('div', class_ = "price").text.strip()
  image_tag = item.find('div', class_ = "image").find("img")
  image_src = image_tag['src'] if image_tag else None   # Extract src attribute

  # Append the data to lists
  names.append(name)
  prices.append(price)
  images.append(image_src)

# Print results
print("Names:",names)
print("Prices:",prices)
print("Images:",images)


web_data = {
  "Product_Name" : names,
  "MRP" : prices,
  "Images_SRC" : images
}

wb_df = pd.DataFrame(web_data)

print("\nConert the web data into DataFrame:\n\n",wb_df)

