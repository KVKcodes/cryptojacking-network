import requests
from bs4 import BeautifulSoup
import os

# Function to scrape article text from a given URL
def scrape_article(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extracting main article text
        article_text = ""
        for paragraph in soup.find_all('p'):
            article_text += paragraph.get_text() + "\n"
        return article_text.strip()
    except Exception as e:
        print(f"Error scraping article from {url}: {e}")
        return ""

# Function to read the URLs from "muzamil.txt" and scrape article text from each URL
def scrape_articles_from_muzamil_file():
    with open("muzamil.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip():
                url, year = line.strip().split(" (")
                year = int(year[:-1])  # Removing the closing brace and converting to integer
                article_text = scrape_article(url)
                if article_text:
                    # Append article text to corresponding year.txt file
                    with open(f"{year}.txt", 'a') as year_file:
                        year_file.write("============\n")
                        year_file.write(article_text)
                        year_file.write("\n")

# Scrape articles from "muzamil.txt" and append them to corresponding year.txt files
scrape_articles_from_muzamil_file()
