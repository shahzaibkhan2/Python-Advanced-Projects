# Import necessary modules
import requests
from bs4 import BeautifulSoup

# Define the URL to scrape data from website
url = 'https://www.example.com'

# Make a GET request to the website
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the links on the page
links = soup.find_all('a')

# Print out the text of each link
for link in links:
    print(link.text)
