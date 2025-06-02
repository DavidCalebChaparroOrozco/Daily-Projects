# Import necessary libraries
import re
from collections import defaultdict
import spacy
from spacy import displacy
from spacy.tokens import Span
from spacy.matcher import PhraseMatcher
from typing import List, Dict, Optional
import matplotlib.pyplot as plt
import pandas as pd

# Load English language model
nlp = spacy.load("en_core_web_sm")

# Enhanced lyrics analyzer with better entity recognition and genre detection.
class LyricsAnalyzer:    
    # Initialize with comprehensive patterns and dictionaries.
    def __init__(self):
        self.custom_patterns = {
            'PERSON': ['mr.', 'ms.', 'mrs.', 'dr.', 'prof.', 'sir', 'lady', 'dude', 'baby'],
            'EVENT': ['festival', 'concert', 'party', 'wedding', 'funeral', 'show', 'tour'],
            'CULTURE': ['hollywood', 'broadway', 'oscar', 'grammy', 'mtv', 'radio', 'tv'],
            'LOCATION': ['street', 'avenue', 'boulevard', 'highway', 'alley']
        }
        
        self.emotion_words = [
            'love', 'hate', 'happy', 'sad', 'anger', 'fear', 'joy', 
            'pain', 'lonely', 'heartbreak', 'ecstasy', 'cry', 'tears',
            'smile', 'laugh', 'broken', 'blue', 'happy', 'glad'
        ]
        
        self.genre_keywords = {
            'rock': ['rock', 'guitar', 'band', 'roll', 'electric', 'amplifier', 'drum'],
            'pop': ['pop', 'radio', 'hit', 'single', 'chart', 'dance', 'baby'],
            'hiphop': ['rap', 'hiphop', 'mc', 'rhyme', 'flow', 'street', 'money'],
            'country': ['country', 'truck', 'whiskey', 'cowboy', 'ranch', 'horse', 'train'],
            'blues': ['blues', 'mississippi', 'delta', 'train', 'heartache']
        }
        
        self._enhance_ner()
        self._add_emotion_patterns()
    
    # Enhance NER with comprehensive patterns
    def _enhance_ner(self) -> None:
        ruler = nlp.add_pipe("entity_ruler", before="ner")
        
        patterns = []
        for label, terms in self.custom_patterns.items():
            patterns.extend([{"label": label, "pattern": term} for term in terms])
        
        # Add common music-specific patterns
        patterns.extend([
            {"label": "PERSON", "pattern": [{"LOWER": {"IN": ["mr", "ms", "dr"]}}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": {"REGEX": "^[a-z]+$"}}]},
            {"label": "EVENT", "pattern": [{"LOWER": {"IN": ["music", "song"]}}, {"LOWER": {"IN": ["festival", "awards"]}}]}
        ])
        
        ruler.add_patterns(patterns)
    
    # Add patterns to detect emotional phrases
    def _add_emotion_patterns(self) -> None:
        emotion_phrases = [
            "broken heart", "fall in love", "tears of joy", 
            "crying over you", "can't stop smiling"
        ]
        
        ruler = nlp.add_pipe("entity_ruler", name="emotion_ruler", before="ner")
        patterns = [{"label": "EMOTION", "pattern": phrase} for phrase in emotion_phrases]
        ruler.add_patterns(patterns)
    
    # Enhanced mock lyrics database with more recognizable entities.
    def get_lyrics(self, artist: str, song: str) -> Optional[str]:
        mock_lyrics_db = {
            ('bob dylan', 'like a rolling stone'): """
            Once upon a time you dressed so fine
            Threw the bums a dime in your prime, didn't you?
            People call, say 'beware doll, you're bound to fall'
            You thought they were all kidding you
            On Broadway with your new American clothes
            Now you don't talk so loud, now you don't seem so proud
            About having to be scrounging your next meal
            
            How does it feel, how does it feel?
            To be without a home, like a complete unknown
            Like a rolling stone
            """,
            
            ('johnny cash', 'folsom prison blues'): """
            I hear the train a-comin', it's rolling round the bend
            And I ain't seen the sunshine since I don't know when
            I'm stuck in Folsom Prison and time keeps dragging on
            But that train keeps a-rollin' on down to San Antone
            
            When I was just a baby, my mama told me, 'Son
            Always be a good boy, don't ever play with guns'
            But I shot a man in Reno just to watch him die
            When I hear that whistle blowing, I hang my head and cry
            """
        }
        
        key = (artist.lower(), song.lower())
        return mock_lyrics_db.get(key, None)
    
    # Enhanced analysis with phrase matching and better entity grouping.
    def analyze_lyrics(self, lyrics: str) -> Dict[str, List[str]]:
        doc = nlp(lyrics)
        
        entities = defaultdict(list)
        for ent in doc.ents:
            entities[ent.label_].append(ent.text)
        
        # Detect emotions at phrase level
        emotions = []
        for chunk in doc.noun_chunks:
            if any(emotion in chunk.text.lower() for emotion in self.emotion_words):
                emotions.append(chunk.text)
        
        # Detect emotions at token level
        emotions.extend([token.text for token in doc 
                        if token.text.lower() in self.emotion_words])
        
        if emotions:
            entities['EMOTION'] = list(set(emotions))
        
        # Detect song-specific entities
        self._detect_song_entities(doc, entities)
        
        return dict(entities)
    
    # Detect song-specific entities that standard NER might miss.
    def _detect_song_entities(self, doc, entities: Dict) -> None:
        # Look for musical references
        music_terms = ['song', 'music', 'band', 'guitar', 'drum', 'sing']
        for token in doc:
            if token.text.lower() in music_terms:
                if 'MUSIC' not in entities:
                    entities['MUSIC'] = []
                entities['MUSIC'].append(token.text)
        
        # Look for geographic references
        geo_terms = ['street', 'road', 'city', 'town', 'river']
        for token in doc:
            if token.text.lower() in geo_terms:
                # Check if it's part of a proper noun
                if token.i > 0 and doc[token.i-1].ent_type_ == "PERSON":
                    if 'LOCATION' not in entities:
                        entities['LOCATION'] = []
                    entities['LOCATION'].append(f"{doc[token.i-1].text} {token.text}")
    
    # Enhanced genre detection with scoring system.
    def detect_genre(self, lyrics: str) -> str:
        scores = {genre: 0 for genre in self.genre_keywords}
        words = re.findall(r'\w+', lyrics.lower())
        
        for word in words:
            for genre, keywords in self.genre_keywords.items():
                if word in keywords:
                    scores[genre] += 1
        
        # Only return genre if we have strong confidence
        max_score = max(scores.values())
        if max_score < 2:  # Minimum threshold
            return 'unknown'
        
        return max(scores.items(), key=lambda x: x[1])[0]
    
    # Enhanced visualization with custom colors.
    def visualize_entities(self, lyrics: str) -> None:
        doc = nlp(lyrics)
        
        # Add custom colors
        colors = {
            "PERSON": "linear-gradient(90deg, #aa9cfc, #fc9ce7)",
            "LOCATION": "linear-gradient(90deg, #ff9569, #ff6961)",
            "EVENT": "#ffdf80",
            "EMOTION": "#a8e6cf",
            "CULTURE": "#dcedc1",
            "MUSIC": "#ffaaa5"
        }
        options = {"colors": colors}
        
        displacy.render(doc, style="ent", options=options, jupyter=False)
    
    # Enhanced report with more metrics and analysis.
    def generate_report(self, artist: str, song: str) -> Dict:
        lyrics = self.get_lyrics(artist, song)
        if not lyrics:
            return {"error": "Lyrics not found"}
        
        entities = self.analyze_lyrics(lyrics)
        genre = self.detect_genre(lyrics)
        
        # Calculate emotional density
        emotion_count = len(entities.get('EMOTION', []))
        word_count = len(re.findall(r'\w+', lyrics))
        emotion_density = emotion_count / word_count if word_count > 0 else 0
        
        return {
            "artist": artist,
            "song": song,
            "genre": genre,
            "entities": entities,
            "entity_counts": {k: len(v) for k, v in entities.items()},
            "word_count": word_count,
            "emotion_density": round(emotion_density, 4),
            "unique_entities": len(set([item for sublist in entities.values() for item in sublist])),
            "lyrics_sample": lyrics[:150] + ("..." if len(lyrics) > 150 else "")
        }


# Enhanced visualization with multiple charts.
def plot_entity_distribution(reports: List[Dict]) -> None:
    if not reports or all('error' in r for r in reports):
        print("No valid data to plot")
        return
    
    # Prepare data
    entity_data = defaultdict(int)
    genre_data = defaultdict(int)
    
    for report in reports:
        if 'error' in report:
            continue
            
        for entity_type, count in report['entity_counts'].items():
            entity_data[entity_type] += count
        
        genre_data[report['genre']] += 1
    
    # Plot entity distribution
    if entity_data:
        df_entities = pd.DataFrame({
            'Entity Type': list(entity_data.keys()),
            'Count': list(entity_data.values())
        }).sort_values('Count', ascending=False)
        
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.bar(df_entities['Entity Type'], df_entities['Count'], color='skyblue')
        plt.title('Entity Distribution')
        plt.xticks(rotation=45)
        
    # Plot genre distribution
    if len(genre_data) > 1:  # More than just 'unknown'
        df_genres = pd.DataFrame({
            'Genre': list(genre_data.keys()),
            'Count': list(genre_data.values())
        }).sort_values('Count', ascending=False)
        
        plt.subplot(1, 2, 2)
        plt.pie(df_genres['Count'], labels=df_genres['Genre'], autopct='%1.1f%%')
        plt.title('Genre Distribution')
        
    plt.tight_layout()
    plt.show()


# Example usage with enhanced output
if __name__ == "__main__":
    analyzer = LyricsAnalyzer()
    
    print("Enhanced LyricsNER Analysis by David Caleb")
    print("=".center(50, "="))
    
    # Analyze Bob Dylan song
    print("\nAnalyzing 'Like a Rolling Stone' by Bob Dylan:")
    print("-".center(50, "-"))
    dylan_report = analyzer.generate_report("Bob Dylan", "Like a Rolling Stone")
    
    for key, value in dylan_report.items():
        if key == 'entities':
            print("\nENTITIES:")
            for entity, items in value.items():
                print(f"  {entity}: {', '.join(items[:3])}{'...' if len(items) > 3 else ''}")
        elif key not in ['lyrics_sample', 'error']:
            print(f"{key.upper()}: {value}")
    
    # Visualize entities
    print("\nEntity Visualization:")
    dylan_lyrics = analyzer.get_lyrics("Bob Dylan", "Like a Rolling Stone")
    if dylan_lyrics:
        analyzer.visualize_entities(dylan_lyrics)
    
    # Analyze Johnny Cash song
    print("\nAnalyzing 'Folsom Prison Blues' by Johnny Cash:")
    print("-".center(50, "-"))
    cash_report = analyzer.generate_report("Johnny Cash", "Folsom Prison Blues")
    
    for key, value in cash_report.items():
        if key == 'entities':
            print("\nENTITIES:")
            for entity, items in value.items():
                print(f"  {entity}: {', '.join(items[:3])}{'...' if len(items) > 3 else ''}")
        elif key not in ['lyrics_sample', 'error']:
            print(f"{key.upper()}: {value}")
    
    # Comparative analysis
    print("\nComparative Analysis:")
    print("-".center(50, "-"))
    reports = [dylan_report, cash_report]
    plot_entity_distribution(reports)