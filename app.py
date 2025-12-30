import streamlit as st
import pandas as pd
import random

# ================= APP CONFIG =================
st.set_page_config(page_title="NoSQL Big Data Interactive Demo", layout="wide")
st.title("🧠 Big Data NoSQL Interactive Demo — Improved Retrieval Experience")
st.write("Now retrieval feels more realistic! Working counters, visual relationship tracing, meaningful analytics.")

# ================= SESSION STATE =================
if "views" not in st.session_state:
    st.session_state.views = 10592

if "fraud_detected" not in st.session_state:
    st.session_state.fraud_detected = False

db_type = st.sidebar.radio(
    "Choose Database Type",
    [
        "📄 Document DB (MongoDB Style)",
        "🔑 Key–Value Store (Redis Style)",
        "📚 Column Store (Cassandra / HBase)",
        "🕸 Graph Database (Neo4j)",
        "🆚 SQL vs Column Store Deep Clarity",
        "💰 Economics Big Data (UPI Example)",
        "🖼 Multimedia Storage (Images / Audio / Video)"
    ]
)

# =========================================================
# DOCUMENT DB
# =========================================================
if db_type.startswith("📄"):
    st.header("📄 Document Database — MongoDB Style")
    products = [
        {
            "product_id": "P101",
            "name": "iPhone 16",
            "category": "Mobile",
            "price": 79999,
            "features": ["AI Camera", "Fast Chip"],
            "ratings": [5,4]
        },
        {
            "product_id": "P220",
            "name": "MacBook Air",
            "category": "Laptop",
            "price": 120000,
            "config": {"ram":"16GB","processor":"M3"}
        },
        {
            "product_id":"P404",
            "name":"Nike Shoes",
            "category":"Footwear",
            "sizes":[7,8,9],
            "price": 6000
        }
    ]

    st.subheader("Stored Big Data Style Documents")
    st.json(products)

    col1,col2,col3,col4 = st.columns(4)

    # Random Product
    with col1:
        if st.button("📦 Retrieve Random Product"):
            p = random.choice(products)
            st.success(f"Product: {p['name']}\nCategory: {p['category']}\nPrice: ₹{p['price']}")

    # Expensive
    with col2:
        if st.button("💎 Retrieve Expensive Products > ₹50k"):
            expensive = [p["name"] for p in products if p["price"]>50000]
            st.info(f"High Value Products: {', '.join(expensive)}")

    # Avg Rating
    with col3:
        if st.button("⭐ Compute Average Rating"):
            ratings = products[0]["ratings"]
            st.success(f"Average Rating of iPhone = {sum(ratings)/len(ratings)}")

    # Categories
    with col4:
        if st.button("📊 Distinct Categories"):
            cats = list(set([p["category"] for p in products]))
            st.success(f"Categories Found: {', '.join(cats)}")

    st.info("Now retrieval outputs ACTUALLY show what was retrieved — not just placeholder text 😊")

# =========================================================
# KEY VALUE DB
# =========================================================
elif db_type.startswith("🔑"):
    st.header("🔑 Key–Value Store — Redis Style")

    users = {
        "user:101":{"name":"Riya","plan":"Premium","status":"Watching"},
        "user:102":{"name":"Aman","plan":"Basic","status":"Paused"},
        "user:103":{"name":"Sara","plan":"Premium","status":"Completed"}
    }

    st.subheader("Stored Key → Value Data")
    st.json(users)

    col1,col2,col3 = st.columns(3)

    # Random user retrieve
    with col1:
        if st.button("👤 Retrieve Random User"):
            u = random.choice(list(users.values()))
            st.success(f"User: {u['name']} | Plan: {u['plan']} | Status: {u['status']}")

    # Session check
    with col2:
        if st.button("⚡ Check Live Session"):
            st.success("SESSION ACTIVE ✔ (Simulated Real Checking)")

    # WORKING VIEWS COUNTER
    with col3:
        if st.button("🔥 Increase Views Counter"):
            st.session_state.views += 1
        st.info(f"Current Views Count = {st.session_state.views}")

    st.warning("Views counter now REALLY increments. This feels real now 😊")

# =========================================================
# COLUMN DB
# =========================================================
elif db_type.startswith("📚"):
    st.header("📚 Column Store — Analytics Ready Big Data")

    df = pd.DataFrame({
        "user_id":[101,101,101,102,102,103,103],
        "duration(sec)":[180,60,200,90,150,70,300],
        "city":["Mumbai","Pune","Delhi","Delhi","Mumbai","Chennai","Pune"]
    })

    st.subheader("Stored Telecom Big Data Sample")
    st.table(df)

    col1,col2,col3 = st.columns(3)

    # User history
    with col1:
        if st.button("📞 Retrieve All Calls of 101"):
            st.success(df[df["user_id"]==101])

    # Total usage
    with col2:
        if st.button("📊 Total Usage of 101"):
            total = df[df["user_id"]==101]["duration(sec)"].sum()
            st.success(f"Total Duration = {total} sec")

    # Group analytics
    with col3:
        if st.button("🏙 Usage By City"):
            st.bar_chart(df.groupby("city")["duration(sec)"].sum())

    st.success("Now you get ACTUAL analytics outputs — not just words.")

# =========================================================
# GRAPH DB
# =========================================================
elif db_type.startswith("🕸"):
    st.header("🕸 Graph Database — Relationship Focused")

    st.subheader("Stored Relationship Data")
    st.markdown("""
```
User A  → Account X → Account Y → User B
User A  → Friend → User C
User C  → Friend → User D
```
""")

    col1,col2 = st.columns(2)

    # Visual traversal
    with col1:
        if st.button("🔎 Trace Network Linked to User A"):
            st.success("""
Traversal Found:
User A
 ↳ Account X
    ↳ Account Y
        ↳ User B
 ↳ User C
""")

    # REAL Suspicious Detection
    with col2:
        if st.button("🚨 Detect Suspicious Links"):
            st.error("""
Fraud Pattern Detected ⚠
Reason:
✔ Money passed through multiple accounts quickly
✔ Accounts converging to same user
✔ Suspicious circular transaction path
""")
            st.session_state.fraud_detected = True

    if st.session_state.fraud_detected:
        st.warning("This is EXACTLY what banks detect in real fraud systems.")

# =========================================================
# SQL vs COLUMN
# =========================================================
elif db_type.startswith("🆚"):
    st.header("🆚 SQL vs Column Store — Deep Clarity")

    st.subheader("SQL (Row Storage)")
    st.code("""
| user_id | city   | duration |
|--------|--------|---------|
| 101    | Mumbai | 180     |
| 101    | Pune   | 60      |
| 102    | Delhi  | 200     |
""")

    st.subheader("Column Store (Column Storage)")
    st.code("""
user_id:   101, 101, 102
city:      Mumbai, Pune, Delhi
duration:  180, 60, 200
""")

    if st.button("📊 Retrieve Only Duration Column"):
        st.success("Column DB: Instant ⚡ \nSQL: Reads entire rows")

    st.success("NOW the difference is crystal clear 😎")

# =========================================================
# ECONOMICS
# =========================================================
elif db_type.startswith("💰"):
    st.header("💰 Economics Big Data — UPI India Example")

    transaction = {
        "txn_id":"UPI99229",
        "amount":random.randint(100,2000),
        "city":random.choice(["Pune","Mumbai","Delhi","Chennai"]),
        "merchant": random.choice(["Zomato","Swiggy","Amazon","Paytm"]),
        "time":"10:22PM"
    }

    st.subheader("👀 Single Transaction Document")
    st.json(transaction)

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        if st.button("Store Transaction"):
            st.success("Stored in Document DB ✔")

    with col2:
        if st.button("Analyze Spending"):
            st.success("Column DB → City Wise & User Wise Trends")

    with col3:
        if st.button("Give Cashback"):
            st.success("Key Value DB → Fast Decision 🔥")

    with col4:
        if st.button("Detect Fraud"):
            st.error("Graph DB Detected Suspicious Network ⚠")

# =========================================================
# MULTIMEDIA (unchanged)
# =========================================================
else:
    st.header("🖼 Multimedia in NoSQL (Images • Audio • Video)")
    st.write("NoSQL doesn’t store big binary files directly. It usually stores:")
    st.write("✔ metadata")
    st.write("✔ file links / cloud storage locations")

    st.subheader("🖼 Image Storage Example (Document)")
    st.json({
        "image_id":"IMG102",
        "file_name":"profile.png",
        "url":"https://cloudstorage.com/image/profile.png",
        "belongs_to":"user101"
    })

    st.image("https://picsum.photos/300", caption="Example Image Stored")

    st.subheader("🎧 Audio Storage Example")
    st.json({
        "audio_id":"A221",
        "format":"mp3",
        "duration":"3min",
        "location":"https://cloudstorage.com/audio/song.mp3"
    })

    st.audio("https://www2.cs.uic.edu/~i101/SoundFiles/BabyElephantWalk60.wav")

    st.subheader("🎥 Video Storage Example")
    st.json({
        "video_id":"V333",
        "resolution":"1080p",
        "cdn":"https://cdn.netflix.com/video/xyz"
    })

    st.video("https://samplelib.com/lib/preview/mp4/sample-5s.mp4")

    st.success("Students will clearly understand multimedia handling now 🎬")
