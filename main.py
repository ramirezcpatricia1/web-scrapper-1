import requests
import csv
from bs4 import BeautifulSoup

# make the request to get the html content
response = requests.get('https://www.espn.com.co/')

# parse the response
soup = BeautifulSoup(response.content, 'html.parser')

# get all h2 tags
titles = soup.find_all('h2')

# fill a variable with the text from h2 tags
data = []

for title in titles:
    titleText = title.text
    keyword = "diego"

    # only push texts that contain the word diego
    if keyword in titleText.lower():
        data.append([titleText])

# write the file with the list created
with open('data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("The file has been created successfully!")
