import os
from dotenv import load_dotenv

load_dotenv()

# Bright Data Configuration
AUTH = 'brd-customer-hl_02b8ed4b-zone-scraping_browser4:1hmta0fde5t7'
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'

# Analysis Configuration
MAX_CONTENT_LENGTH = 6000
SENTIMENT_THRESHOLD = 0.1
FOCUS_AREAS = {
    'technology': ['ai', 'machine learning', 'automation', 'digital'],
    'service': ['support', 'customer service', 'help', 'assistance'],
    'pricing': ['price', 'cost', 'subscription', 'payment'],
    'features': ['feature', 'capability', 'functionality', 'tool']
}
