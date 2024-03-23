# Import necessary libraries
import tkinter as tk  # For GUI
from tkinter import messagebox, PhotoImage, filedialog
import nltk  # For natural language processing
from textblob import TextBlob  # For sentiment analysis
from newspaper import Article  # For web content extraction


# # Test
# # Download NLTK data required for tokenization
# nltk.download("punkt")

# # Example URL for testing
# url = "https://www.cnbc.com/2024/03/21/microsoft-debuts-its-first-surface-pcs-with-dedicated-copilot-key.html"

# # Create an Article object and extract content from the provided URL
# article = Article(url)
# article.download()  # Download the article
# article.parse()  # Parse the article content
# article.nlp()  # Perform natural language processing on the article

# # Print extracted information from the article
# print(f"Title: {article.title}")
# print(f"Authors: {article.authors}")
# print(f"Publication Date: {article.publish_date}")
# print(f"Summary: {article.summary}")

# # Perform sentiment analysis on the article text
# analysis = TextBlob(article.text)
# print(f"Polarity: {analysis.polarity}")
# print(f"Sentiment: {'positive' if analysis.polarity > 0 else 'negative' if analysis.polarity < 0 else 'neutral'}")


# Function to summarize the article and analyze its sentiment
def summarize():
    try:
        # Get URL from user input text
        url = utext.get("1.0", "end").strip()
        # http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/
        # https://www.cnbc.com/2024/03/21/microsoft-debuts-its-first-surface-pcs-with-dedicated-copilot-key.html

        # Download and parse the article using Newspaper library
        article = Article(url)  # Initialize Article object with the provided URL
        article.download()  # Download the article content
        article.parse()  # Parse the article

        if not article.title:  # Check if the article title is empty
            raise ValueError("Unable to extract article title. Please check the provided URL.")
        article.nlp()  # Perform natural language processing on the article content

        # Enable editing of text fields
        title.config(state="normal")
        author.config(state="normal")
        publication.config(state="normal")
        summary.config(state="normal")
        sentiment.config(state="normal")

        # Display article title
        title.delete("1.0", "end")
        title.insert("1.0", article.title)

        # Display author(s) of the article
        author.delete("1.0", "end")
        author.insert("1.0", article.authors)

        # Display publication date of the article
        publication.delete("1.0", "end")
        publication.insert("1.0", article.publish_date)

        # Display summary of the article content
        summary.delete("1.0", "end")
        summary.insert("1.0", article.summary)

        # Perform sentiment analysis on the article text
        analysis = TextBlob(article.text)
        # print(analysis.polarity)
        sentiment.delete("1.0", "end")
        sentiment.insert("1.0",f"Polarity: {analysis.polarity}, Sentiment: {'positive' if analysis.polarity > 0 else 'negative' if analysis.polarity < 0 else 'neutral'}")

        # Disable editing of text fields to prevent accidental changes
        title.config(state="disabled")
        author.config(state="disabled")
        publication.config(state="disabled")
        summary.config(state="disabled")
        sentiment.config(state="disabled")

    except Exception as e:
        messagebox.showerror("Error", str(e))  # Display error message in case of exception

# Function to clear the URL field.
def clear_url():
    utext.delete("1.0", "end")

# Create the main application window
root = tk.Tk()
root.title("News Summarizer")
root.geometry("1200x625")
root.tk.call("wm", "iconphoto", root._w, PhotoImage(file="newspaper.png"))

# Label and text field to display the article title
tlabel = tk.Label(root, text="Title")
tlabel.pack()
title = tk.Text(root, height=1, width=140)
title.config(state="disabled", bg="#dddddd")
title.pack()

# Label and text field to display the author(s) of the article
alabel = tk.Label(root, text="Author")
alabel.pack()
author = tk.Text(root, height=1, width=140)
author.config(state="disabled", bg="#dddddd")
author.pack()

# Label and text field to display the publication date of the article
plabel = tk.Label(root, text="Publishing Date")
plabel.pack()
publication = tk.Text(root, height=1, width=140)
publication.config(state="disabled", bg="#dddddd")
publication.pack()

# Label and text field to display a summary of the article
slabel = tk.Label(root, text="Summary")
slabel.pack()
summary = tk.Text(root, height=20, width=140)
summary.config(state="disabled", bg="#dddddd")
summary.pack()

# Label and text field to display sentiment analysis of the article
selabel = tk.Label(root, text="Sentiments Analysis")
selabel.pack()
sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state="disabled", bg="#dddddd")
sentiment.pack()

# Label and text field for user to input the article URL
ulabel = tk.Label(root, text="URL")
ulabel.pack()
utext = tk.Text(root, height=1, width=140)
utext.pack()

# Button to trigger the summarize function when clicked
btn = tk.Button(root,text="Summarize", command=summarize)
btn.pack()

# Button to clear URL field
clear_btn = tk.Button(root, text="Clear", command=clear_url)
clear_btn.pack()

root.mainloop()
