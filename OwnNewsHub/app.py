# Import necessary libraries
import feedparser  
from flask import Flask, render_template, request  
from pyspark.sql.connect.functions import array_insert 

# Initialize the Flask app
app = Flask(__name__)

# Define a dictionary of RSS feed sources with their URLs
RSS_FEEDS = {
    'Yahoo Finance': 'https://finance.yahoo.com/news/rssindex',
    'Hacker News': 'https://news.ycombinator.com/rss',
    'Wall Street Journal': 'https://feeds.a.dj.com/rss/RSSMarketsMain.xml',
    'CNBC': 'https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=15839069'
}

# Route for the homepage
@app.route('/')
def index():
    # Initialize an empty list to store articles
    articles = []
    # Loop through the RSS feeds and parse each one
    for source, feed in RSS_FEEDS.items():
        # Parse the RSS feed
        parsed_feed = feedparser.parse(feed)  
        # Add each entry (article) along with its source to the articles list
        entries = [(source, entry) for entry in parsed_feed.entries]
        articles.extend(entries)

    # Sort the articles by their published date in descending order
    articles = sorted(articles, key=lambda x: x[1].published_parsed, reverse=True)

    # Handle pagination
    # Get the page number from the URL
    page = request.args.get('page', 1, type=int)  
    # Number of articles to display per page
    per_page = 10  
    # Total number of articles
    total_articles = len(articles)  
    # Calculate the starting index for pagination
    start = (page-1) * per_page  
    # Calculate the ending index for pagination
    end = start + per_page  
    # Get the articles for the current page
    paginated_articles = articles[start:end]

    # Render the homepage with paginated articles and pagination info
    return render_template('index.html', articles=paginated_articles, page=page,
                           total_pages=total_articles // per_page + 1)

# Route for search functionality
@app.route('/search')
def search():
    # Get the search query from the URL
    query = request.args.get('q')  

    # Initialize an empty list to store articles
    articles = []
    # Loop through the RSS feeds and parse each one
    for source, feed in RSS_FEEDS.items():
        # Parse the RSS feed
        parsed_feed = feedparser.parse(feed)  
        # Add each entry (article) along with its source to the articles list
        entries = [(source, entry) for entry in parsed_feed.entries]
        articles.extend(entries)

    # Filter the articles based on the search query
    results = [article for article in articles if query.lower() in article[1].title.lower()]

    # Render the search results page with the filtered articles and the query
    return render_template('search_results.html', articles=results, query=query)

# Run the app in debug mode if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)