import pandas as pd
from openai import OpenAI
import time


client = openai.api_key = "your-key-here"




df = pd.read_csv("senti.csv", encoding="latin1")
df = df.dropna(subset=["review text"]) 
print(f" Total valid reviews: {len(df)}")


def classify_review(review_text):
    prompt = f"""
You are an emotionally intelligent language model trained for qualitative text analysis.

Analyze the following beauty product review through the lens of affective discourse and consumer sentiment.

Provide:
1. **Sentiment Classification**: Positive, Neutral, or Negative — based on the reviewer’s overall judgment of the product experience.
2. **Dominant Emotion(s)**: Select up to two from [joy, trust, sadness, anger, fear, surprise, disgust, anticipation] that best reflect the emotional tone and intention of the review.
3. **Discourse Insight**: In 1–2 sentences, explain *why* this sentiment and emotion were detected. Focus on word choice, tone, implicit expectations, and any linguistic markers of subjectivity or affect.

Return in the following format:
Sentiment: <Positive/Neutral/Negative>  
Emotions: <emotion1, emotion2>  
Reason: <concise analysis, 1–2 sentences>

Keep your answer analytical yet concise. This is part of a humanities-centered study on how GPT-4o interprets affect in user-generated beauty product reviews.

Review: \"{review_text}\""""

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"ERROR: {e}"


results = []
for i, review in enumerate(df["review text"]):
    print(f"Processing review {i+1}/{len(df)}: {str(review)[:60]}...")
    result = classify_review(str(review))
    results.append(result)
    time.sleep(1.5)  


df["gpt_analysis"] = results
df.to_excel("Annotated_Reviews.xlsx", index=False)
print(" All done! Results saved to 'Annotated_Reviews.xlsx'")
