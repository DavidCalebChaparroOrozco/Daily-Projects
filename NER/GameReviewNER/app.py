# Import necessary libraries
import requests
import spacy
from collections import Counter
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from datetime import datetime
from wordcloud import WordCloud
import time
import re
import warnings
warnings.filterwarnings("ignore")

# Load English language model for spaCy
try:
    nlp = spacy.load("en_core_web_lg")
except OSError:
    print("Downloading spaCy model 'en_core_web_lg' (this may take a moment)...")
    spacy.cli.download("en_core_web_lg")
    nlp = spacy.load("en_core_web_lg")

# A class to analyze video game reviews from Steam.
# Detects games, platforms, features, reported issues, and emotions.
class GameReviewAnalyzer:
    def __init__(self):
        # Custom patterns for entity recognition
        self.custom_patterns = [
            {"label": "GAME", "pattern": [{"LOWER": {"IN": ["game", "title", "release"]}}]},
            {"label": "PLATFORM", "pattern": [{"LOWER": {"IN": ["pc", "steam", "windows", "mac", "linux", "console", "xbox", "playstation"]}}]},
            {"label": "FEATURE", "pattern": [{"LOWER": {"IN": ["graphics", "sound", "gameplay", "controls", "story", "performance"]}}]},
            {"label": "ISSUE", "pattern": [{"LOWER": {"IN": ["bug", "crash", "lag", "glitch", "error", "problem"]}}]},
            {"label": "GENRE", "pattern": [{"LOWER": {"IN": ["rpg", "fps", "shooter", "strategy", "adventure", "indie", "simulation", "sports", "racing", "horror"]}}]}
        ]
        # Store the labels of custom patterns for easy lookup (in uppercase to match spaCy's default entity label case)
        self.custom_patterns_labels = {p["label"].upper() for p in self.custom_patterns}

        # Add custom patterns to the pipeline
        # Check if 'entity_ruler' is already in the pipeline to avoid adding it multiple times
        if "entity_ruler" not in nlp.pipe_names:
            ruler = nlp.add_pipe("entity_ruler", before="ner")
            ruler.add_patterns(self.custom_patterns)
        else:
            # If it exists, you might want to clear existing patterns or handle re-initialization
            # For this context, we assume it's already configured correctly or we'll skip adding.
            # In a long-running app, you might want to `nlp.remove_pipe("entity_ruler")` and then re-add.
            pass

        # Steam API configuration
        self.steam_api_url = "https://store.steampowered.com/api/"

    # Search games on Steam by title.
    def search_game_by_name(self, query):
        url = f"{self.steam_api_url}storesearch"
        params = {'term': query, 'cc': 'us', 'l': 'english'}

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            return [(item['id'], item['name']) for item in data.get('items', [])]
        except Exception as e:
            print(f"Error searching games: {e}")
            return []

    # Get game details by AppID
    def get_game_details(self, app_id):
        url = f"{self.steam_api_url}appdetails"
        params = {'appids': app_id, 'cc': 'us', 'l': 'english'}

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get(str(app_id), {}).get('data') if data.get(str(app_id), {}).get('success') else None
        except Exception as e:
            print(f"Error getting game details: {e}")
            return None

    # Scrape reviews from Steam using direct API calls.
    def scrape_steam_reviews(self, app_id, num_reviews=100):
        reviews = []
        cursor = '*'
        query_count = 0

        print(f"\nFetching reviews for appID {app_id}...")

        while len(reviews) < num_reviews and query_count < 10: # Limit queries to avoid rate limiting or infinite loops
            params = {
                'json': 1,
                # Can change to 'all' or 'updated'
                'filter': 'all', 
                'language': 'english',
                # Increased day_range to get more reviews potentially
                'day_range': 365, 
                'review_type': 'all',
                'purchase_type': 'all',
                # Max 100 per page
                'num_per_page': min(100, num_reviews - len(reviews)), 
                'cursor': cursor
            }

            try:
                response = requests.get(f"https://store.steampowered.com/appreviews/{app_id}", params=params)
                response.raise_for_status()
                data = response.json()

                if not data.get('success', False) or not data.get('reviews'):
                    # No more reviews or API error
                    break

                reviews.extend(review.get('review') for review in data.get('reviews', []) if 'review' in review)
                cursor = data.get('cursor', None)
                query_count += 1
                print(f"Collected {len(reviews)}/{num_reviews} reviews...")
                # Rate limiting: wait 1 second between requests
                time.sleep(1)  

                # If cursor is None, there are no more pages
                if cursor is None: 
                    break

            except Exception as e:
                print(f"Error during API request: {e}")
                break

        print(f"Finished collecting {len(reviews)} reviews.")
        return reviews

    # Analyze reviews to extract entities and sentiments
    def analyze_reviews(self, reviews):
        results = {
            "games": Counter(),
            "platforms": Counter(),
            "features": Counter(),
            "issues": Counter(),
            "genres": Counter(),
            "sentiments": [],
            "review_details": []
        }

        for review in reviews:
            doc = nlp(review)
            sentiment = TextBlob(review).sentiment

            results["sentiments"].append(sentiment.polarity)
            results["review_details"].append({
                "text": review,
                "sentiment": sentiment.polarity,
                "entities": [(ent.text, ent.label_) for ent in doc.ents]
            })

            for ent in doc.ents:
                # Ensure the entity label is converted to lowercase to match counter keys
                if ent.label_.lower() in results:
                    results[ent.label_.lower()][ent.text] += 1

        return results

    # Generate a comprehensive text report for a video game investigation
    def generate_report(self, analysis_results, game_name):
        report_lines = [
            f" Game Review Analysis: {game_name} ",
            f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "="*60,
            "\n## Overall Sentiment Summary",
            f"Total Reviews Analyzed: {len(analysis_results['sentiments'])}",
            f"Average Review Sentiment: {'Positive' if (avg := np.mean(analysis_results['sentiments'])) > 0.1 else 'Negative' if avg < -0.1 else 'Neutral'} ({avg:.2f})",
            f"Sentiment Variability (Std Dev): {np.std(analysis_results['sentiments']):.2f}",
            "",
            "**Interpretation:** This score indicates the general player reception. A positive score suggests satisfaction, while a negative score points to overall dissatisfaction.",
            "",
        ]

        # Helper to add entity sections with sentiment context for features/issues
        def append_relevant_entity_section(lines_list, entities_counter, review_details, title, entity_label_filter=None):
            lines_list.append(f"\n## {title}")
            entity_sentiment_data = []

            for review_detail in review_details:
                review_sentiment = review_detail["sentiment"]
                for entity_text, entity_label in review_detail["entities"]:
                    # Filter by specific entity label
                    if entity_label.upper() == entity_label_filter: 
                        entity_sentiment_data.append({
                            'Term': entity_text.lower(),
                            'Sentiment': review_sentiment
                        })

            if entity_sentiment_data:
                df_entity_sentiment = pd.DataFrame(entity_sentiment_data)
                term_summary = df_entity_sentiment.groupby('Term').agg(
                    Count=('Term', 'size'),
                    AverageSentiment=('Sentiment', 'mean')
                ).reset_index()

                # Sort by count first, then by average sentiment
                top_terms = term_summary.sort_values(by='Count', ascending=False).head(10) # Top 10 by count

                if not top_terms.empty:
                    for index, row in top_terms.iterrows():
                        sentiment_category = 'Positive' if row['AverageSentiment'] > 0.1 else 'Negative' if row['AverageSentiment'] < -0.1 else 'Neutral'
                        lines_list.append(f"- **{row['Term']}** (Mentions: {row['Count']}, Avg Sentiment: {row['AverageSentiment']:.2f} - {sentiment_category})")
                else:
                    lines_list.append("- No specific relevant mentions found.")
            else:
                lines_list.append("- No relevant data found.")
            lines_list.append("")
            return lines_list

        # Relevant Sections for Video Game Investigation
        # Most Mentioned Features & Their Sentiment
        append_relevant_entity_section(report_lines, analysis_results["features"], analysis_results["review_details"],
                                    "Top Features Mentioned & Their Associated Sentiment", "FEATURE")

        # Most Reported Issues & Their Sentiment
        append_relevant_entity_section(report_lines, analysis_results["issues"], analysis_results["review_details"],
                                        "Top Issues Reported & Their Associated Sentiment", "ISSUE")

        # Other General Entities (Optional, but still useful) 
        report_lines.append("\n## Other Key Mentions (Counts Only)")
        # Combine all entities for overall popular terms (excluding features/issues already covered in detail)
        other_entities_combined = Counter()
        for entity_type_key in ["games", "platforms", "genres"]: # Only these for this section
            other_entities_combined.update(analysis_results[entity_type_key])

        if other_entities_combined:
            for item, count in other_entities_combined.most_common(5): # Top 5 other terms
                report_lines.append(f"- {item}: {count} mentions")
        else:
            report_lines.append("- No other key terms found.")
        report_lines.append("")

        # Key Review Examples 
        report_lines.append("\n## Key Review Examples for Context")
        if analysis_results["review_details"]:
            if len(analysis_results["review_details"]) > 0:
                sorted_reviews = sorted(analysis_results["review_details"], key=lambda x: x['sentiment'])

                report_lines.append(f"### Most Positive Review (Sentiment: {sorted_reviews[-1]['sentiment']:.2f}):")
                report_lines.append(f"```\n{sorted_reviews[-1]['text'][:min(len(sorted_reviews[-1]['text']), 300)]}...\n```")
                report_lines.append("")

                report_lines.append(f"### Most Negative Review (Sentiment: {sorted_reviews[0]['sentiment']:.2f}):")
                report_lines.append(f"```\n{sorted_reviews[0]['text'][:min(len(sorted_reviews[0]['text']), 300)]}...\n```")
                report_lines.append("")

                most_neutral = min(analysis_results["review_details"], key=lambda x: abs(x['sentiment']))
                report_lines.append(f"### Most Neutral Review (Sentiment: {most_neutral['sentiment']:.2f}):")
                report_lines.append(f"```\n{most_neutral['text'][:min(len(most_neutral['text']), 300)]}...\n```")
                report_lines.append("")
            else:
                report_lines.append("- Not enough reviews to provide examples.")
        else:
            report_lines.append("- No reviews available for examples.")
        report_lines.append("="*60)


        return "\n".join(report_lines)

    # Create a comprehensive visualization dashboard
    def create_comprehensive_visualization(self, analysis_results, game_name):
        if not analysis_results["review_details"]:
            print("No data to visualize")
            return

        # Prepare data for visualization
        sentiment_data = pd.DataFrame({
            'sentiment': analysis_results["sentiments"],
            'review_length': [len(r['text']) for r in analysis_results["review_details"]]
        })

        # Set the style
        plt.style.use('default')
        sns.set_style("whitegrid")
        background_color = "#f8fafc"

        # Create the figure with a 3x2 grid (6 subplots total)
        fig = plt.figure(figsize=(18, 24))
        gs = fig.add_gridspec(3, 2)
        gs.update(wspace=0.3, hspace=0.5)

        # Create axes
        ax1 = fig.add_subplot(gs[0, 0])  # Sentiment distribution (overall review)
        ax2 = fig.add_subplot(gs[0, 1])  # Review length vs sentiment
        ax3 = fig.add_subplot(gs[1, 0])  # Sentiment over time
        ax4 = fig.add_subplot(gs[1, 1])  # Sentiment by review length category
        ax5 = fig.add_subplot(gs[2, 0])  # NEW: Sentiment Distribution of Sentences
        ax6 = fig.add_subplot(gs[2, 1])  # Word cloud

        # Set background color
        for ax in [ax1, ax2, ax3, ax4, ax5, ax6]:
            ax.set_facecolor(background_color)

        # Main title
        fig.suptitle(f'{game_name} Review Analysis', fontsize=20, fontweight='bold', y=1.02)

        # 1. Sentiment distribution (ax1) - Overall Review Sentiment
        sns.histplot(ax=ax1, data=sentiment_data, x='sentiment', bins=20, kde=True, color='skyblue')
        ax1.set_title('1. Overall Review Sentiment Distribution', fontsize=14, fontweight='bold')
        ax1.set_xlabel('Sentiment Polarity (-1 to 1)')
        ax1.set_ylabel('Number of Reviews')
        ax1.axvline(x=0, color='red', linestyle='--', alpha=0.5)

        # 2. Review length vs sentiment (ax2)
        sns.scatterplot(ax=ax2, data=sentiment_data, x='review_length', y='sentiment', alpha=0.6, color='skyblue', s=80)
        ax2.set_title('2. Review Length vs Sentiment', fontsize=14, fontweight='bold')
        ax2.set_xlabel('Review Length (characters)')
        ax2.set_ylabel('Sentiment Polarity')
        ax2.axhline(y=0, color='red', linestyle='--', alpha=0.5)

        # 3. Sentiment trend over time (ax3)
        try:
            dates = pd.to_datetime(pd.date_range(end=datetime.now(), periods=len(sentiment_data), freq='D'))
            sentiment_data['date'] = dates
            sentiment_data['rolling_sentiment'] = sentiment_data['sentiment'].rolling(window=7, min_periods=1).mean()

            sns.lineplot(ax=ax3, data=sentiment_data, x='date', y='rolling_sentiment', color='purple', linewidth=2.5)
            ax3.set_title('3. Sentiment Trend (7-review rolling avg)', fontsize=14, fontweight='bold')
            ax3.set_xlabel('Date')
            ax3.set_ylabel('Average Sentiment')
            ax3.axhline(y=0, color='red', linestyle='--', alpha=0.5)
            ax3.tick_params(axis='x', rotation=30)
        except Exception as e:
            ax3.text(0.5, 0.5, f"Could not create sentiment trend: {e}", ha='center', va='center', transform=ax3.transAxes)
            ax3.set_title('3. Sentiment Trend (Error)', fontsize=14, fontweight='bold')

        # 4. Sentiment by review length category (ax4)
        try:
            sentiment_data['length_category'] = pd.cut(sentiment_data['review_length'],
                                                        bins=[0, 100, 500, 1000, float('inf')],
                                                        labels=['Short (<100)', 'Medium (100-500)',
                                                                'Long (500-1000)', 'Very Long (>1000)'])

            sns.boxplot(ax=ax4, data=sentiment_data, x='length_category', y='sentiment',
                        palette='coolwarm', showfliers=False)
            ax4.set_title('4. Sentiment by Review Length', fontsize=14, fontweight='bold')
            ax4.set_xlabel('Review Length Category')
            ax4.set_ylabel('Sentiment Polarity')
            ax4.tick_params(axis='x', rotation=45)
            ax4.axhline(y=0, color='red', linestyle='--', alpha=0.5)
        except Exception as e:
            ax4.text(0.5, 0.5, f"Could not create length analysis: {e}", ha='center', va='center', transform=ax4.transAxes)
            ax4.set_title('4. Sentiment by Length (Error)', fontsize=14, fontweight='bold')

        # 5. Word cloud (ax6)
        try:
            text = " ".join(review['text'] for review in analysis_results["review_details"] if review and review['text'])
            if text:
                wordcloud = WordCloud(width=800, height=400,
                                        background_color=background_color,
                                        max_words=100, collocations=False).generate(text)
                ax5.imshow(wordcloud, interpolation='bilinear')
                ax5.set_title('6. Most Frequent Words in Reviews', fontsize=14, fontweight='bold')
                ax5.axis('off')
            else:
                ax5.text(0.5, 0.5, "No text available for word cloud", ha='center', va='center', transform=ax5.transAxes)
                ax5.set_title('6. Word Cloud (No Text)', fontsize=14, fontweight='bold')
                ax5.axis('off')
        except Exception as e:
            ax5.text(0.5, 0.5, f"Could not create word cloud: {e}", ha='center', va='center', transform=ax5.transAxes)
            ax5.set_title('6. Word Cloud (Error)', fontsize=14, fontweight='bold')
            ax5.axis('off')
        
        
        # Save the figure
        plt.tight_layout()
        safe_game_name = re.sub(r'[^\w\s-]', '', game_name).replace(' ', '_')
        filename = f"{safe_game_name}_review_analysis.png"
        plt.savefig(filename, bbox_inches='tight', dpi=300)
        plt.close()
        print(f"\nVisualization saved as {filename}")

# # Display the main menu options
def display_menu():
    print("\n" + "="*50)
    print("GAME REVIEW ANALYZER - MAIN MENU")
    print("=".center(50, "="))
    print("1. Search game by name")
    print("2. Analyze game by AppID")
    print("3. Exit")
    print("=".center(50, "="))

def main():
    analyzer = GameReviewAnalyzer()

    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            # Search by name
            game_title = input("Enter game title to search: ")
            games = analyzer.search_game_by_name(game_title)

            if not games:
                print("No games found with that title.")
                continue

            print("\nFound games:")
            for idx, (appid, name) in enumerate(games, 1):
                print(f"{idx}. {name} (AppID: {appid})")

            try:
                selection = int(input("\nEnter number to analyze (or 0 to cancel): "))
                if 1 <= selection <= len(games):
                    app_id, game_name = games[selection-1]
                    analyze_game(analyzer, app_id, game_name)
                elif selection == 0:
                    print("Analysis cancelled.")
                else:
                    print("Invalid selection. Please enter a number within the range.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "2":
            try:
                app_id = int(input("Enter Steam AppID to analyze: "))
                game_details = analyzer.get_game_details(app_id)

                if game_details:
                    analyze_game(analyzer, app_id, game_details.get('name', f"AppID {app_id}"))
                else:
                    print("Could not find game with that AppID.")
            except ValueError:
                print("Please enter a valid numeric AppID.")

        elif choice == "3":
            print("Exiting Game Review Analyzer. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

# # Helper function to analyze a game and generate outputs
def analyze_game(analyzer, app_id, game_name):
    print(f"\nAnalyzing: {game_name}")
    reviews = analyzer.scrape_steam_reviews(app_id)

    if not reviews:
        print("No reviews were collected. Analysis aborted.")
        return

    analysis_results = analyzer.analyze_reviews(reviews)

    # Generate and save report
    report = analyzer.generate_report(analysis_results, game_name)
    print("\n" + report)

    # Save report with proper encoding
    safe_game_name_for_file = re.sub(r'[^\w\s-]', '', game_name).replace(' ', '_')
    filename = f"{safe_game_name_for_file}_review_report.txt"
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"\nReport saved as {filename}")
    except Exception as e:
        print(f"\nError saving report: {e}")

    # Create visualizations
    analyzer.create_comprehensive_visualization(analysis_results, game_name)

if __name__ == "__main__":
    main()