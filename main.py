#This is my first web scrapping project to take a website and extract information to be converted into a panda table
#The website is an Arts and Crafts store that I'm looking to get updated on the most current prices

#Importing the Python modules required for this project
from bs4 import BeautifulSoup
import pandas as pd

#Opening the local HTML file I created from my previous Codecademy website development project
with open('index.html', 'r') as file:
    content = file.read()
    soup = BeautifulSoup(content, 'lxml')
    Dict = {}
    Price = []

#locating the store items needed from the h1 tag from the HTML website
    tags = soup.find_all('h1')

#Obtaining the string from the element and adding it to the dictionary object
    for topic in tags:
        topics = topic.text
        Dict[topics] = []

#Removing the unnecessary string
    del Dict['Navigation:']

#Extracting the price from the span element and adding them to the price list
    for item in soup.find_all('span'):
        prices = item.text.split()[2]
        Price.append(prices)

#Cleaning up the data and creating variables to feed into the numpy DataFrame
topic_name = (
    f'{list(Dict.keys())[0]},{list(Dict.keys())[1]},{list(Dict.keys())[2]}'
    )
store_items = topic_name.split(',')

#Needed to join together the separated numbers in each price element to make three items
amount = ''.join(f'{(Price[0])},{Price[1]},{Price[2]}')
price_num = list(amount.split(','))
print(store_items)
print(price_num)

#Setting up the Numpy DataFrame with the scraped data
df = pd.DataFrame(store_items)
df.columns = ['Inventory']
df['Price'] = price_num

#Displaying the Table
print(df)

#Displaying the HTML content
print(soup.prettify())
'''Output should show the following:
['Brushes', 'Frames', 'Paint']
['$3.00', '$2.00', '$5.00']
  Inventory  Price
0   Brushes  $3.00
1    Frames  $2.00
2     Paint  $5.00'''