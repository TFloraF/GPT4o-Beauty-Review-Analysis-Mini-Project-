
# Affective Discourse Analysis in Beauty Product Reviews using GPT-4o

This mini-project explores how GPT-4o can classify sentiment and detect emotions in user-generated beauty product reviews. It was developed for the course **LLMs, GPT and the Humanities** at TU Darmstadt (SoSe 2025).

## Project Overview

- **Objective**: Understand how GPT-4o interprets affective signals in consumer reviews from the skincare and makeup domains.
- **Methodology**: Prompt-based zero-shot classification of sentiment and emotions using GPT-4o.
- **Dataset**: 3 beauty products — *Kiehl’s Lip Balm*, *Beauty of Joseon Sunscreen*, *Lancôme Hypnôse Mascara*.
- **Tools**: Python scripts using `pandas`, `matplotlib`, `wordcloud` for data analysis and visualization.

## Files in this Repository                           

| `Annotated_Reviews.xlsx`  | Dataset + GPT-4o extracted sentiment/emotions   |
| `gpt_sentiment_analysis4.py` | Python script for GPT-4o emotion analysis     |
| `VISUAL.py`               | Python script to generate all three charts      |
| `README.md`               | Project documentation (you’re reading it)       |

## Output Visualizations

- **Sentiment Pie Chart**
- **Emotion Frequency Bar Chart**
- **Word Cloud**

All visuals use a pastel color palette optimized for academic posters.

## How to Run

1. **Install dependencies**  
```bash
pip install openai pandas matplotlib wordcloud
Set your OpenAI API Key
openai.api_key = "your-key-here"
Run the analysis script
python gpt_sentiment_analysis4.py
Generate the visualizations
python VISUAL.py




Use Case
This project was used in an academic poster presentation, with a [QR code linked to this repository]. It demonstrates how LLMs like GPT-4o can serve as discourse-aware tools in affective computing.


License & Attribution
Open-source, educational use only. 