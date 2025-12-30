import streamlit as st
import pandas as pd
import numpy as np
import random
import time
import altair as alt

# -------------------------------------------------------
# APP HEADER
# -------------------------------------------------------
st.set_page_config(page_title="Big Data – Text & Audio NoSQL Demo", layout="wide")
st.title("🧠 Big Data Demo — Text & Audio in NoSQL Databases")
st.write("Realistic simulation of how text reviews, tweets, economics data & audio are stored, retrieved & analyzed.")


# -------------------------------------------------------
# SIDEBAR
# -------------------------------------------------------
mode = st.sidebar.radio(
    "Choose Demo",
    ["📝 Text Data (Tweets / Reviews)",
     "💰 Economics Text Big Data",
     "🎧 Audio Big Data Use Case"]
)


# ======================================================
# 📝 TEXT DATA — SOCIAL + REVIEWS
# ======================================================
if mode.startswith("📝"):
    st.header("📝 Text Big Data — Social Media & Customer Reviews")

    # ----------- CREATE BIG TEXT DATASET -----------
    customers = ["Riya","Aman","Ali","Sarah","John","Neha","Kiran","Priya","David"]
    cities = ["Mumbai","Delhi","Pune","Chennai","Hyderabad","Bangalore"]
    sentiments = ["Positive","Neutral","Negative"]

    text_data = []

    sample_reviews = [
        "Absolutely loved the product 😍",
        "Worst experience ever 👎",
        "Service could be better but okay",
        "Amazing speed and great interface!",
        "Highly disappointed 😡",
        "Good value for money 👍",
        "Not worth the price",
        "Pretty decent overall",
        "Customer support was fantastic!"
    ]

    for i in range(5000):
        text_data.append({
            "user": random.choice(customers),
            "city": random.choice(cities),
            "review": random.choice(sample_reviews),
            "rating": random.randint(1,5),
            "sentiment": random.choice(sentiments)
        })

    df = pd.DataFrame(text_data)

    st.subheader("📂 Example Stored Reviews (Document DB Style — MongoDB)")
    st.json(df.sample(3).to_dict(orient="records"))

    st.info("In **Document Databases (MongoDB)** each review is stored as a JSON-like document — flexible, scalable, perfect for text 🎯")

    # ----------- ANALYTICS SECTION -----------
    st.subheader("📊 Real Analytics on Text Big Data")

    col1,col2,col3 = st.columns(3)

    with col1:
        st.write("### 🌎 Reviews by City")
        chart = df.groupby("city")["review"].count().reset_index()
        st.bar_chart(chart.set_index("city"))

    with col2:
        st.write("### ⭐ Rating Distribution")
        st.bar_chart(df["rating"].value_counts().sort_index())

    with col3:
        st.write("### 🙂 Sentiment Spread")
        st.bar_chart(df["sentiment"].value_counts())

    # ----------- SEARCH LIKE A NO-SQL QUERY -----------
    st.subheader("🔎 Search Like NoSQL Querying")

    search_city = st.selectbox("Filter by City", ["All"] + cities)

    if search_city != "All":
        st.write(df[df["city"]==search_city].head(10))
    else:
        st.write(df.head(10))

    st.success("""
NoSQL Power:
✔ Flexible text storage  
✔ Handles unstructured big data  
✔ Fast search + analytics  
✔ Great for social platforms like Twitter, Instagram
""")


# ======================================================
# 💰 ECONOMICS — TEXT UPI & POLICY FEEDBACK
# ======================================================
elif mode.startswith("💰"):
    st.header("💰 Economics — Text Big Data Example")

    st.write("Consider **UPI feedback, RBI opinions, policy reactions, spending behaviour comments** collected at scale.")

    # Create Big Fake UPI Economics Opinion Data
    economics_text = []
    policy_comments = [
        "UPI is boosting digital economy massively",
        "Charges on transactions are worrying",
        "Digital payments are convenient",
        "Security concerns exist but improving",
        "Government policies are encouraging cashless economy",
        "Banks need to improve success rate",
    ]

    cities = ["Mumbai","Delhi","Pune","Chennai","Hyderabad","Bangalore"]

    for i in range(4000):
        economics_text.append({
            "user": random.choice(["Economist","Student","Citizen","Trader","Shopkeeper"]),
            "comment": random.choice(policy_comments),
            "city": random.choice(cities),
            "sentiment": random.choice(["Positive","Neutral","Negative"])
        })

    eco_df = pd.DataFrame(economics_text)

    st.subheader("📄 Stored Economics Documents (Document DB)")
    st.json(eco_df.sample(3).to_dict(orient="records"))

    st.subheader("📊 Policy Analytics")

    col1,col2 = st.columns(2)

    with col1:
        st.write("### City Contribution to Digital Economy Conversation")
        st.bar_chart(eco_df["city"].value_counts())

    with col2:
        st.write("### Sentiment Towards Digital Payments")
        st.bar_chart(eco_df["sentiment"].value_counts())

    st.success("""
Economics + NoSQL:
✔ Collect public policy opinions  
✔ Analyze sentiment  
✔ Help RBI / Govt shape policies  
✔ Understand digital economy adoption  
""")


# ======================================================
# 🎧 AUDIO BIG DATA
# ======================================================
elif mode.startswith("🎧"):
    st.header("🎧 Audio Big Data — Stored in NoSQL")

    st.write("Think of **Call Center recordings, Spotify streaming, Voice Assistants, Speech Analytics** 🎤")

    # ---------- AUDIO METADATA (Stored in NoSQL) ----------
    st.subheader("📀 How Audio is Stored in NoSQL")

    audio_records = [
        {
            "audio_id": "A1001",
            "user": "Customer_1",
            "duration_sec": random.randint(30,600),
            "sentiment": random.choice(["Calm","Angry","Frustrated","Happy"]),
            "category":"Customer Support",
            "storage":"Object Storage + Metadata in Document DB"
        }
        for i in range(500)
    ]

    audio_df = pd.DataFrame(audio_records)

    st.json(audio_df.sample(2).to_dict(orient="records"))

    st.info("""
Audio is NOT stored in traditional DB tables.
Instead:
🎵 Audio File → Stored in Object Storage (S3 / GCS / Azure Blob)  
📄 Metadata → Stored in NoSQL (MongoDB / Cassandra / Elastic)
""")

    # ---------- AUDIO ANALYTICS ----------
    st.subheader("📊 Audio Analytics")

    col1,col2 = st.columns(2)

    with col1:
        st.write("### Sentiment From Voice Tone")
        st.bar_chart(audio_df["sentiment"].value_counts())

    with col2:
        st.write("### Duration Distribution")
        duration_data = (
            audio_df["duration_sec"]
            .value_counts(bins=5)
            .sort_index()
        )
        st.bar_chart(duration_data)

    st.audio("https://www2.cs.uic.edu/~i101/SoundFiles/BabyElephantWalk60.wav")

    st.success("""
Audio + NoSQL:
✔ Store millions of recordings  
✔ Fast metadata search  
✔ Run AI / NLP / Speech analysis  
✔ Perfect for Call Centers, Spotify, Alexa  
""")

# END
