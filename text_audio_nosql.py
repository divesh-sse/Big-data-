import streamlit as st
import random
import pandas as pd
import numpy as np
import time
from collections import Counter

# ---------------- APP CONFIG ----------------
st.set_page_config(page_title="Text Big Data + NoSQL Demo", layout="wide")
st.title("🧠 Text Big Data + NoSQL Interactive Demo")
st.write("""
This app demonstrates how **text data** is stored in different NoSQL databases,
how analytics are done, and how large-scale text datasets feel in real life.
""")

# ---------------- GENERATE DATA ----------------
def generate_reviews(n=1000):
    customers = ["Riya","Arjun","Sam","Pooja","Kunal","Aisha","Rohan","Mira"]
    sentiments = ["good","excellent","bad","worst","amazing","poor","satisfying","awesome"]
    items = ["iPhone","Laptop","Headphones","Shoes","Smartwatch","Camera"]

    data=[]
    for i in range(n):
        data.append({
            "user": random.choice(customers),
            "review": f"{random.choice(items)} is {random.choice(sentiments)} and I feel {random.choice(sentiments)} using it!",
            "rating": random.randint(1,5)
        })
    return pd.DataFrame(data)

def generate_tweets(n=1000):
    topics=["#BigData","#UPI","#India","#Budget2025","#Tech","#Startups"]
    moods=["love","hate","confused about","excited for","worried about","happy with"]
    entities=["economy","government","banks","technology","students","jobs"]

    tweets=[]
    for i in range(n):
        tweets.append({
            "user":"user"+str(random.randint(101,999)),
            "tweet":f"I {random.choice(moods)} {random.choice(entities)} {random.choice(topics)}",
            "likes": random.randint(0,5000)
        })
    return pd.DataFrame(tweets)

def generate_economics_text(n=1000):
    cities=["Mumbai","Delhi","Pune","Chennai","Bangalore"]
    actions=["spending increased","inflation rising","prices stable","strong demand","GDP growth improving"]
    sectors=["food","fuel","housing","education","health"]

    eco=[]
    for i in range(n):
        eco.append({
            "city": random.choice(cities),
            "report": f"In {random.choice(cities)}, {random.choice(actions)} especially in {random.choice(sectors)} sector.",
            "impact_score": random.randint(1,10)
        })
    return pd.DataFrame(eco)

# ---------------- CREATE BIG DATA ----------------
reviews_df = generate_reviews()
tweets_df = generate_tweets()
eco_df = generate_economics_text()

db_type = st.sidebar.radio(
    "Choose Dataset",
    ["⭐ Customer Reviews (NLP + NoSQL)",
     "🐦 Tweets & Social Media Analytics",
     "💰 Economics Text Data Analytics"]
)

# ==================================================
# ⭐ CUSTOMER REVIEWS
# ==================================================
if db_type.startswith("⭐"):
    st.header("⭐ Customer Reviews — Text Big Data + NoSQL")

    st.write("### Sample of Stored Reviews (1000 real-like records generated)")
    st.dataframe(reviews_df.head(10))

    # ---------- How Stored in NoSQL ----------
    st.subheader("📦 How This Looks in a Document Database (MongoDB Style)")
    st.json(reviews_df.head(3).to_dict(orient="records"))

    st.subheader("🔑 How Looks in Key-Value (Redis Style)")
    st.code("""
key: review:101
value: {
 "user":"Riya",
 "review":"iPhone is excellent...",
 "rating":5
}
""")

    st.subheader("📚 Column Store Representation (Analytics Focused)")
    st.code("""
user: Riya, Arjun, Sam...
review: text...
rating: 4, 5, 3, 2...
""")

    st.markdown("---")
    st.subheader("📊 NLP Style Analytics")

    col1,col2 = st.columns(2)

    with col1:
        if st.button("Compute Average Rating"):
            avg = round(reviews_df["rating"].mean(),2)
            st.success(f"Average Rating = {avg}")

    with col2:
        if st.button("Most Common Sentiment Word"):
            words = " ".join(reviews_df["review"]).lower().split()
            counter = Counter(words)
            common = counter.most_common(5)
            st.info(common)

    st.bar_chart(reviews_df["rating"].value_counts())

    st.success("This is how e-commerce platforms analyze customer text at scale.")

# ==================================================
# 🐦 TWEETS
# ==================================================
elif db_type.startswith("🐦"):
    st.header("🐦 Social Media Text — Tweet Big Data Analytics")

    st.write("### Live-Like Twitter Data (1000 Records)")
    st.dataframe(tweets_df.head(10))

    st.subheader("📦 Stored in Document DB (JSON Style)")
    st.json(tweets_df.head(3).to_dict(orient="records"))

    st.subheader("📚 Column Store View")
    st.code("""
user: user222, user431...
tweet: text...
likes: 120, 344, 20...
""")

    st.subheader("📊 Trending Analytics")

    col1,col2 = st.columns(2)

    with col1:
        if st.button("Find Trending Hashtags"):
            hashtags = " ".join(tweets_df["tweet"]).split()
            tags=[t for t in hashtags if "#" in t]
            st.success(Counter(tags).most_common(5))

    with col2:
        if st.button("Popular Users Simulation"):
            popular = tweets_df.sort_values(by="likes",ascending=False).head(5)
            st.table(popular)

    st.bar_chart(tweets_df["likes"])

    st.warning("This is how Twitter/Meta analyze posts at scale.")

# ==================================================
# 💰 ECONOMICS
# ==================================================
else:
    st.header("💰 Economics Text Big Data — Real Feel Example")

    st.write("### Thousands of Economic Sentences")
    st.dataframe(eco_df.head(10))

    st.subheader("📦 Stored as Documents in NoSQL")
    st.json(eco_df.head(3).to_dict(orient="records"))

    st.subheader("📊 Analytics (Like RBI / Govt Systems)")
    col1,col2 = st.columns(2)

    with col1:
        if st.button("Find Most Reported City"):
            city = eco_df["city"].value_counts().idxmax()
            st.success(f"Most Economic Mentions: {city}")

    with col2:
        if st.button("Avg Impact Score"):
            st.success(f"Impact Score = {eco_df['impact_score'].mean()}")

    st.bar_chart(eco_df.groupby("city")["impact_score"].mean())

    st.info("Shows how economics institutions analyze public sentiment & text data using NoSQL.")

