# Importing necessary libraries
from bs4 import BeautifulSoup
import requests

# Function to scrape XML feed
def scrape_xml_feed(feed_url):
    try:
        # Sending HTTP request to fetch XML feed
        response = requests.get(feed_url)
        # Raises HTTPError if request was unsuccessful
        response.raise_for_status() 
        soup = BeautifulSoup(response.content, "xml")
        
        # Determining the type of feed (RSS or Atom)
        if soup.find("rss"):  
            items = soup.find_all("item")
        elif soup.find("feed"):
            items = soup.find_all("entry")
        else:
            print("Couldn't determine the feed type.")
            return
        
        # Iterating through each item in the feed
        for item in items:
            if soup.find("rss"):
                title = item.title.text
                description = item.description.text
                link = item.link.text
            elif soup.find("feed"):
                title = item.title.text
                description = item.summary.text
                link = item.link['href']
            else:
                continue

            # Printing information of each item
            print(f"Title: {title}\n\nDescription: {description}\n\nLink: {link}\n{'-'*50}")
    except requests.RequestException as e:
        # Handling request exceptions
        print(f"Error fetching XML feed: {e}")


if __name__ == "__main__":
    # List of feed URLs to scrape
    feeds = [
        "https://realpython.com/atom.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
        "https://nvidianews.nvidia.com/releases.xml"
    ]
    # Iterating through each feed URL
    for feed_url in feeds:
        print(f"Scraping feed from {feed_url}:\n")
        scrape_xml_feed(feed_url)
        print("\n")