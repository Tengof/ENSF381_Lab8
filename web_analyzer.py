import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = "https://en.wikipedia.org/wiki/University_of_Calgary"

try:
    response = requests.get(url)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")
    
except Exception as e:
    print(f"Error fetching content: {e}")
    
# print(soup.prettify())

headings = 0
for num in range(1, 7):
    header = "h" + str(num)
    headings += len(soup.find_all(header))

links = len(soup.find_all('a'))
paragraphs = len(soup.find_all('p'))

print("There are {} <h> tags".format(headings))
print("There are {} <a> tags".format(links))
print("There are {} <p> tags".format(paragraphs))


userInput = input("Enter a keyword: ")

soupString = soup.get_text()
soupStringList = soupString.split(" ")

keywordCount = 0
for word in soupStringList:
    word = word.lower()
    if(userInput == word):
        keywordCount += 1
    
print("\nThere are {} occurances of the key: {}".format(keywordCount, userInput))

soupDict = {}
for word in soupStringList:
    word = word.lower()
    if(word in soupDict):
        soupDict[word] += 1
    else:
        soupDict[word] = 1

print("\nThe top 5 most frequently occuring words are:")

for num in range(1, 6):
    maximum = max(soupDict, key=soupDict.get)
    print("{}. {}: {}".format(num, maximum, soupDict[maximum]))
    soupDict.pop(maximum)

longestStr = ""

soupString = soup.get_text('p')
elementList = soup.find_all('p')
for element in elementList:
    text = element.get_text(strip=True)
    if(len(text) > len(longestStr)):
        longestStr = text

longestStrWords = longestStr.split(" ")
print("\nThe longest paragraph has {} words".format(len(longestStrWords)))
print("\nThe longest paragraph is: \n{}".format(longestStr))

labels = ['Headings', 'Links', 'Paragraphs']
values = [headings, links, paragraphs]
plt.bar(labels, values)
plt.title('Group #29')
plt.ylabel('Count')
plt.show()