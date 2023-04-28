# Import necessary modules
import requests
from bs4 import BeautifulSoup
import re


# Defining a function to extract relevant features from a website
def extract_features(url):
    # Retrieve the website HTML content
    response = requests.get(url)
    html = response.text

    # Parsing the HTML using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Extracting the website title
    title = soup.title.string if soup.title else ''

    # Extracting the website domain
    domain = re.search('https?://([\w\.]+)/?', url).group(1)

    # Extracting the number of external links on the website
    external_links = len(
        [link for link in soup.find_all('a') if link.has_attr('href') and not link['href'].startswith(domain)])

    # Extracting the website text content
    text = soup.get_text()

    # Extracting the number of spam keywords in the text content
    spam_keywords = len([word for word in text.split() if word.lower() in ['buy', 'free', 'offer', 'discount']])

    # Return a dictionary of the extracted features
    return {'title': title, 'domain': domain, 'external_links': external_links, 'spam_keywords': spam_keywords}


# Defining a function to classify a website as spam or not
def classify_website(url):
    # Extract the features of the website
    features = extract_features(url)

    # Defining a simple rule-based classifier
    if features['external_links'] > 10 or features['spam_keywords'] > 5:
        return 'SPAM'
    else:
        return 'NOT SPAM'
