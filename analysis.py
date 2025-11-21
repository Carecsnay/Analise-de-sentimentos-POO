from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(text)
    compound_score = scores['compound']
    
    if compound_score >= 0.05:
        category = 'Positive'
    elif compound_score <= -0.05:
        category = 'Negative'
    else:
        category = 'Neutral'
        
    return category, compound_score