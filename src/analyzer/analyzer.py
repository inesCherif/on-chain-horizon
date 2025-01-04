import re
from nltk.sentiment import SentimentIntensityAnalyzer
from collections import Counter
from config.settings import FOCUS_AREAS
import streamlit as st


class CompetitorAnalysis:
    def __init__(self):
        # Only download vader_lexicon for sentiment analysis
        try:
            import nltk
            nltk.download('vader_lexicon', quiet=True)
        except Exception as e:
            st.error(f"Error initializing sentiment analyzer: {str(e)}")

        self.sia = SentimentIntensityAnalyzer()
        self.common_words = set(['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that',
                                 'have', 'i', 'it', 'for', 'not', 'on', 'with', 'he',
                                 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by',
                                 'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an',
                                 'will', 'my', 'one', 'all', 'would', 'there', 'their',
                                 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get',
                                 'which', 'go', 'me'])

    def analyze_sentiment(self, text):
        try:
            return self.sia.polarity_scores(text)['compound']
        except Exception as e:
            st.error(f"Error in sentiment analysis: {str(e)}")
            return 0

    def extract_key_features(self, text):
        try:
            # Simple word extraction using regex
            words = re.findall(r'\b\w+\b', text.lower())

            # Filter out common words and short words
            words = [w for w in words if w not in self.common_words and len(w) > 2]

            # Get word frequency
            return Counter(words).most_common(10)
        except Exception as e:
            st.error(f"Error in feature extraction: {str(e)}")
            return [("error", 0)]

    def identify_competitors_focus(self, text):
        try:
            text_lower = text.lower()
            focus_areas = {k: 0 for k in FOCUS_AREAS.keys()}

            # Simple string matching for focus areas
            for area, terms in FOCUS_AREAS.items():
                for term in terms:
                    focus_areas[area] += text_lower.count(term)

            return focus_areas
        except Exception as e:
            st.error(f"Error in focus area analysis: {str(e)}")
            return {k: 0 for k in FOCUS_AREAS.keys()}

    def split_sentences(self, text):
        """Simple sentence splitting without NLTK"""
        return re.split(r'[.!?]+', text)