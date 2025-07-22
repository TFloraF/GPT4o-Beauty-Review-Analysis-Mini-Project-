import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter


df = pd.read_excel("Annotated_Reviews.xlsx")

# --- Extract Sentiment and Emotions ---
df['Sentiment'] = df['gpt_analysis'].str.extract(r'Sentiment:\s*(\w+)', expand=False)
df['Emotions'] = df['gpt_analysis'].str.extract(r'Emotions:\s*([^\n]+)', expand=False)


pastel_palette = {
    'positive': '#a4a2e5',     # lavender
    'neutral':  '#56c5c0',     # mint
    'negative': '#f4a6b6',     # soft pink
    'joy': '#a4a2e5',
    'trust': '#50a9da',
    'sadness': '#57b76b',
    'anger': '#ec92b7',
    'fear': '#56c5c0',
    'surprise': '#c2a94c',
    'disgust': '#f4a6b6',
    'anticipation': '#df924b'
}

# ================================
# 1. Pie Chart  Sentiment
# ================================
sentiment_counts = df['Sentiment'].dropna().str.lower().value_counts()
sent_colors = [pastel_palette.get(sent, "#cccccc") for sent in sentiment_counts.index]

plt.figure(figsize=(6,6))
plt.pie(
    sentiment_counts,
    labels=[s.capitalize() for s in sentiment_counts.index],
    colors=sent_colors,
    autopct='%1.1f%%',
    startangle=140
)
plt.title("Sentiment Distribution", fontsize=14)
plt.tight_layout()
plt.show()

# ================================
# 2. Bar Chart  Emotions
# ================================
all_emotions = df['Emotions'].dropna().str.lower().str.split(', ')
emotion_flat = [e.strip() for sublist in all_emotions for e in sublist]
emotion_counts = Counter(emotion_flat)
emotion_labels = list(emotion_counts.keys())
emotion_values = list(emotion_counts.values())
emotion_colors = [pastel_palette.get(e, "#cccccc") for e in emotion_labels]

plt.figure(figsize=(10,5))
plt.bar(emotion_labels, emotion_values, color=emotion_colors)
plt.title("Emotion Frequency", fontsize=14)
plt.xlabel("Emotion")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ================================
# 3. Word Cloud  Review Text
# ================================
from wordcloud import STOPWORDS
import random

# Custom pastel color palette (from your charts)
custom_colors = ['#a4a2e5', '#50a9da', '#57b76b', '#ec92b7', '#56c5c0', '#c2a94c', '#f4a6b6', '#df924b']

# Function to randomly choose a color from your pastel list
def pastel_color_func(*args, **kwargs):
    return random.choice(custom_colors)

# Combine all review text
text = " ".join(df["review text"].dropna().astype(str).tolist())

# Generate Word Cloud
wordcloud = WordCloud(
    width=1000,
    height=500,
    background_color='white',
    max_words=100,
    stopwords=STOPWORDS,
    color_func=pastel_color_func
).generate(text)

# Plot
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud of Review Texts", fontsize=16)
plt.tight_layout()
plt.show()

