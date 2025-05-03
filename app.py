# app.py

import streamlit as st
import pandas as pd
import re
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer

st.set_page_config(page_title="Dark Pattern Review Analyzer", layout="wide")

st.title("Dark Pattern Detector in App Reviews")
st.write("Analyze mobile app reviews to identify potential dark patterns using keyword and sentiment analysis.")

# Upload CSV
uploaded_file = st.file_uploader(" Upload your combined reviews CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Keywords to detect dark patterns
    keywords = [
        "charged", "cancel", "unsub", "hidden fee", "mislead",
        "confusing", "accidental", "auto-renew", "hard to", "trick", 
        "unauthorized", "subscribe", "scam", "deceptive", "refund", 
        "difficult", "sneaky", "cancelled", "canceling", "misleading"
    ]
    pattern = re.compile(r'\b(?:' + '|'.join(map(re.escape, keywords)) + r')\b', flags=re.IGNORECASE)

    # Flag dark pattern reviews
    df['dark_pattern_flag'] = df['content'].apply(lambda x: bool(pattern.search(str(x))))
    flagged = df[df['dark_pattern_flag']].copy()

    # Sentiment analysis
    flagged['polarity'] = flagged['content'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
    flagged['subjectivity'] = flagged['content'].apply(lambda x: TextBlob(str(x)).sentiment.subjectivity)

    st.subheader("📌 Summary")
    st.write(f"Total Reviews: {len(df)}")
    st.write(f"Flagged Reviews (Possible Dark Patterns): {len(flagged)}")

    st.subheader(" Sentiment by App")
    sentiment_summary = flagged.groupby("appId")[["polarity", "subjectivity"]].mean().reset_index()
    st.dataframe(sentiment_summary)

    st.subheader(" Word Cloud of Flagged Reviews")
    wc_text = " ".join(flagged["content"].dropna().astype(str).str.lower())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(wc_text)

    fig_wc, ax_wc = plt.subplots(figsize=(10, 5))
    ax_wc.imshow(wordcloud, interpolation='bilinear')
    ax_wc.axis("off")
    st.pyplot(fig_wc)

    st.subheader(" Top 20 Most Common Complaint Words")
    vectorizer = CountVectorizer(stop_words='english', token_pattern=r'\b[a-zA-Z]{4,}\b')
    X = vectorizer.fit_transform(flagged['content'].dropna().astype(str).str.lower())
    word_freq = X.sum(axis=0).A1
    words = vectorizer.get_feature_names_out()
    word_counts = pd.DataFrame({'Word': words, 'Frequency': word_freq})
    filtered = word_counts[~word_counts['Word'].isin(keywords)].sort_values(by='Frequency', ascending=False).head(20)

    st.bar_chart(data=filtered.set_index("Word"))

    st.subheader(" Flagged Reviews")
    st.dataframe(flagged[['appId', 'content', 'score', 'polarity']].reset_index(drop=True))

else:
    st.info(" Upload your CSV to begin the analysis.")
