import nltk
import sys

def setup_nltk():
    """
    Download only the required VADER lexicon for sentiment analysis
    """
    print("Setting up NLTK sentiment analyzer...")
    try:
        nltk.download('vader_lexicon', quiet=True)
        print("✓ Sentiment analyzer installed successfully!")
    except Exception as e:
        print(f"Error during setup: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    setup_nltk()