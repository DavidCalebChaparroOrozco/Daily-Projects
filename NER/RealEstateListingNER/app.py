# Import necessary libraries
import re
import pandas as pd
from typing import List, Dict, Tuple
import matplotlib.pyplot as plt
import seaborn as sns

# Set up visualization defaults
sns.set(style="whitegrid", palette="pastel")
plt.rcParams["figure.figsize"] = (10, 6)


# A rule-based NER system for extracting real estate entities from property listings.
# Identifies property types, amenities, and exclusive neighborhoods.
class RealEstateNER:
    def __init__(self):
        # Initialize patterns for different entity types
        self._init_patterns()
        
    # Initialize regex patterns for entity extraction
    def _init_patterns(self):
        
        # Property types (add more as needed)
        self.property_types = {
            'loft': r'\blofts?\b|\bopen[- ]space\b',
            'penthouse': r'\bpenthouse(s)?\b|\bph\b',
            'villa': r'\bvillas?\b',
            'condo': r'\bcondo(minium)?s?\b',
            'townhouse': r'\btown[- ]?houses?\b',
            'studio': r'\bstudios?\b|\bstudio[- ]apartment\b'
        }
        
        # Amenities (grouped by categories)
        self.amenities = {
            'luxury': r'\bconcierge\b|\bdoorman\b|\bvalet\b|\bporter\b',
            'outdoor': r'\bterrace\b|\bbalcon(y|ies)\b|\bpatio\b|\bdeck\b',
            'kitchen': r'\bgourmet kitchen\b|\bchef\'?s kitchen\b|\bstainless steel\b',
            'tech': r'\bsmart home\b|\bhome automation\b|\bpre[- ]wired\b',
            'wellness': r'\bgym\b|\bfitness center\b|\bpool\b|\bspa\b|\bsauna\b'
        }
        
        # Example exclusive neighborhoods (customize for your target market)
        self.neighborhoods = {
            'manhattan': r'\bupper east side\b|\bues\b|\bwest village\b|\btribeca\b|\bsoho\b',
            'london': r'\bchelsea\b|\bkensington\b|\bmayfair\b|\bnotting hill\b',
            'paris': r'\ble marais\b|\bsaint[- ]germain\b|\bchamps[- ]elysées\b'
        }
        
    # Extract real estate entities from text.
    def extract_entities(self, text: str) -> Dict[str, List[Tuple[str, str]]]:
        """    
        Args:
            text: Input real estate listing text
            
        Returns:
            Dictionary of entity types with list of (entity, entity_type) tuples
        """
        entities = {
            'property_types': [],
            'amenities': [],
            'neighborhoods': []
        }
        
        # Extract property types
        for prop_type, pattern in self.property_types.items():
            matches = re.finditer(pattern, text, flags=re.IGNORECASE)
            entities['property_types'].extend(
                (match.group(), prop_type) for match in matches
            )
        
        # Extract amenities
        for amenity_type, pattern in self.amenities.items():
            matches = re.finditer(pattern, text, flags=re.IGNORECASE)
            entities['amenities'].extend(
                (match.group(), amenity_type) for match in matches
            )
        
        # Extract neighborhoods
        for city, pattern in self.neighborhoods.items():
            matches = re.finditer(pattern, text, flags=re.IGNORECASE)
            entities['neighborhoods'].extend(
                (match.group(), city) for match in matches
            )
            
        return entities
    
    # Analyze a dataframe of real estate listings and extract entities.
    def analyze_listings(self, listings_df: pd.DataFrame, text_col: str = 'description') -> pd.DataFrame:
        """    
        Args:
            listings_df: DataFrame containing real estate listings
            text_col: Name of column containing listing text
            
        Returns:
            DataFrame with extracted entities as new columns
        """
        # Apply entity extraction to each listing
        entities_df = listings_df[text_col].apply(
            lambda x: pd.Series(self.extract_entities(x))
        )
        
        # Combine with original data
        result_df = pd.concat([listings_df, entities_df], axis=1)
        
        return result_df
    
    # Create visualizations of the extracted entities.
    def visualize_entities(self, entities_df: pd.DataFrame):
        """    
        Args:
            entities_df: DataFrame containing extracted entities
        """
        # Property Type Distribution
        prop_counts = entities_df['property_types'].explode().apply(
            lambda x: x[1] if isinstance(x, tuple) else None
        ).value_counts()
        
        plt.figure()
        sns.barplot(x=prop_counts.values, y=prop_counts.index, palette="Blues_d")
        plt.title("Property Type Distribution")
        plt.xlabel("Count")
        plt.tight_layout()
        plt.show()
        
        # Amenities Distribution
        amenity_counts = entities_df['amenities'].explode().apply(
            lambda x: x[1] if isinstance(x, tuple) else None
        ).value_counts()
        
        plt.figure()
        sns.barplot(x=amenity_counts.values, y=amenity_counts.index, palette="Greens_d")
        plt.title("Amenities Distribution")
        plt.xlabel("Count")
        plt.tight_layout()
        plt.show()
        
        # Neighborhood Distribution
        neighborhood_counts = entities_df['neighborhoods'].explode().apply(
            lambda x: x[1] if isinstance(x, tuple) else None
        ).value_counts()
        
        if not neighborhood_counts.empty:
            plt.figure()
            sns.barplot(x=neighborhood_counts.values, y=neighborhood_counts.index, palette="Reds_d")
            plt.title("Neighborhood Distribution")
            plt.xlabel("Count")
            plt.tight_layout()
            plt.show()


# Example Usage
if __name__ == "__main__":
    # Sample real estate listings data
    sample_data = {
        'id': [1, 2, 3],
        'description': [
            "Luxury penthouse in Tribeca with gourmet kitchen and terrace",
            "Beautiful loft in the Upper East Side with doorman and fitness center",
            "Modern condo in Chelsea with smart home features and concierge service"
        ],
        'price': [2500000, 1800000, 2200000]
    }
    
    listings_df = pd.DataFrame(sample_data)
    
    # Initialize NER system
    ner = RealEstateNER()
    
    # Analyze listings
    analyzed_df = ner.analyze_listings(listings_df)
    
    print("\nAnalyzed Data:")
    print(analyzed_df[['id', 'property_types', 'amenities', 'neighborhoods']])
    
    # Visualize entities
    ner.visualize_entities(analyzed_df)