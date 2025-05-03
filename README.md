#  Dark Pattern Detector in App Reviews

This Streamlit app helps identify potential **dark patterns** in mobile app reviews using **keyword detection**, **sentiment analysis**, and **data visualization**. It's a data-driven tool for exploring UX concerns hidden in user feedback.

---

##  What Are Dark Patterns?

**Dark patterns** are deceptive UX/UI designs that trick users into actions they didn't intend — like accidental subscriptions, hidden fees, or hard-to-find cancel buttons.

This tool helps detect such patterns by analyzing real user reviews.

---

##  Features

-  Upload your own CSV of app reviews
-  Flag reviews containing keywords like "charged", "refund", "cancel", etc.
-  Perform sentiment analysis (polarity & subjectivity) on flagged reviews
-  Generate a word cloud of complaint language
-  Bar chart of top complaint words (excluding obvious flags)
-  View an interactive table of all flagged reviews by app

---

##  Sample Project Structure


dark-pattern-detector/
│
├── app.py # Streamlit dashboard
├── requirements.txt # Required packages
└── all_app_reviews_combined.csv (optional upload)


---

## 📦 Installation

1. Clone the repository

```bash
git clone https://github.com/tushuli396/dark-pattern-detector.git
cd dark-pattern-detector


2. Install dependencies

pip install -r requirements.txt

3. Run the app

streamlit run app.py

📤 How to Use
Upload a CSV with app reviews

Must include at least content (review text) and appId (app identifier) columns.

Explore flagged reviews and analyze complaints

Use insights to drive ethical UX improvements or report patterns

📈 Example Use Case
Analyzed reviews from apps like Spotify, Tinder, Duolingo, and Headspace.
Tinder and Headspace had the most dark-pattern flags — often involving billing confusion and cancelation friction.

📚 Technologies Used
Streamlit – UI dashboard

TextBlob – sentiment analysis

WordCloud – visualizing complaint text

Pandas – data manipulation

scikit-learn – keyword vectorization


Author
Built by Tushuli Amod Patil 
Feel free to connect on LinkedIn or Twitter for collaborations or feedback.


