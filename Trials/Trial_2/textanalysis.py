import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize, sent_tokenize
from textblob import TextBlob
import ssl
import certifi
import nltk

# Set the default SSL certificate path to use certifi's bundle to handle error
#ssl._create_default_https_context = ssl.create_default_context(cafile=certifi.where())
# Correctly set the default SSL context to use certifi's bundle
def default_https_context():
    return ssl.create_default_context(cafile=certifi.where())

ssl._create_default_https_context = default_https_context
# Ensure the 'punkt' tokenizer is downloaded
nltk.download('punkt')

# Load data from Excel
df = pd.read_excel('') # Insert path for feedback
#print(df.columns)

# Function to perform text analysis
def analyze_text(text):
    if pd.isna(text):
        return np.nan  # Return NaN if the text is missing
    words = word_tokenize(text)
    sentences = sent_tokenize(text)
    num_words = len(words)
    num_sentences = len(sentences)
    avg_sentence_length = num_words / num_sentences if num_sentences else 0
    lexical_diversity = len(set(words)) / num_words if num_words else 0
    sentiment = TextBlob(text).sentiment.polarity
    subjectivity = TextBlob(text).sentiment.subjectivity

    return {
        "Total Words": num_words,
        "Average Sentence Length": avg_sentence_length,
        "Lexical Diversity": lexical_diversity,
        "Sentiment": sentiment,
        "Subjectivity": subjectivity
    }

# Names of feedback columns
feedback_columns = ['Unedited GPT 1', 'Unedited GPT 2', 'Unedited GPT 3']

# Apply text analysis to each feedback column and store in new columns
for column in feedback_columns:
    df[column + '_Analysis'] = df[column].apply(analyze_text)

# File to save results
with open('', 'w') as file: # Insert file path to save results
    for column in feedback_columns:
        # Aggregate results for each column
        aggregated_results = df[column + '_Analysis'].dropna().apply(pd.Series).mean()
        print(f'Aggregated Results for {column}:', file=file)
        print(aggregated_results, file=file)
        print('\n', file=file)