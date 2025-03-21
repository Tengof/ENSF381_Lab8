import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/University_of_Calgary"

try:
    response = requests.get(url)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")
    
except Exception as e:
    print(f"Error fetching content: {e}")
    
# print(soup.prettify())

hCount = 0
for num in range(1, 7):
    header = "h" + str(num)
    hCount += len(soup.find_all(header))

aCount = len(soup.find_all('a'))
pCount = len(soup.find_all('p'))

userInput = input("Enter a keyword")
print(userInput)