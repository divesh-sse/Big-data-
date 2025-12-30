import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="NoSQL Big Data Interactive Demo", layout="wide")

st.title("🧠 Big Data NoSQL Interactive Demo")
st.write("Experience how different NoSQL databases store data, retrieve data, and support real-world Big Data use cases — visually and interactively.")

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

# ==============================================
# DOCUMENT DB
# ==============================================
if db_type.startswith("📄"):
    st.header("📄 Document Database — MongoDB Style")
    st.write("Stores Big Data as flexible JSON-like documents. Every record may look different.")

    products = [
        {
            "product_id": "P101",
            "name": "iPhone 16",
            "price": 79999,
            "category": "Mobile",
            "features": ["AI Camera", "Fast Chip"],
            "ratings": [{"user":"Riya","rating":5},{"user":"Amit","rating":4}],
            "stock": True
        },
        {
            "product_id": "P220",
            "name": "MacBook Air",
            "price": 120000,
            "category": "Laptop",
            "config": {"ram":"16GB","processor":"M3"},
            "colors": ["Silver","Black"]
        },
        {
            "product_id": "P330",
            "name": "Sony Headphones",
            "category": "Audio",
            "price": 7999,
            "wireless": True
        },
        {
            "product_id":"P404",
            "name":"Nike Shoes",
            "category":"Footwear",
            "sizes":[7,8,9],
            "price": 6000
        }
    ]

    st.subheader("👀 Large Style Data (Sample)")
    st.json(products)

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        if st.button("📦 Get Random Product"):
            st.success(products[random.randint(0,len(products)-1)])

    with col2:
        if st.button("💎 Get Expensive Products"):
            st.success("MacBook Air (₹120000)")

    with col3:
        if st.button("⭐ Get Average Rating (Demo)"):
            st.success("iPhone 16 Avg Rating = 4.5")

    with col4:
        if st.button("📊 Get All Categories"):
            st.success("Mobile, Laptop, Audio, Footwear")

    st.info("""
### Why This Feels Like Big Data?
✔ Millions of such JSON documents can exist  
✔ Every product can have DIFFERENT FIELDS  
✔ Super flexible for evolving business data  
""")


# ==============================================
# KEY VALUE DB
# ==============================================
elif db_type.startswith("🔑"):
    st.header("🔑 Key–Value Store — Redis/DynamoDB Style")
    st.write("Stores Big Data as blazing fast Key → Value pairs.")

    users = {
        "user:101":{"name":"Riya","plan":"Premium","status":"Watching"},
        "user:102":{"name":"Aman","plan":"Basic","status":"Paused"},
        "user:103":{"name":"Sara","plan":"Premium","status":"Completed"},
        "user:104":{"name":"John","plan":"Standard","status":"Watching"}
    }

    st.subheader("👀 Stored Large Style Data")
    st.json(users)

    col1,col2,col3 = st.columns(3)

    with col1:
        if st.button("👤 Get Random User"):
            st.success(random.choice(list(users.values())))

    with col2:
        if st.button("⚡ Live Session Check"):
            st.success("Session Active")

    with col3:
        if st.button("🔥 Increase Views (Simulated Counter)"):
            st.success("Views Updated ✔")

    st.info("""
### Why This is Big Data?
✔ Millions of active users  
✔ Instant fetching needed  
✔ Used in Netflix, Hotstar, Banking Sessions  
""")


# ==============================================
# COLUMN STORE
# ==============================================
elif db_type.startswith("📚"):
    st.header("📚 Column Store — Cassandra / HBase")
    st.write("Stores data column-wise. Perfect for analytics and time series Big Data.")

    df = pd.DataFrame({
        "user_id":[101,101,101,102,102,103,103,103],
        "date_time":[
            "2025-01-10 10:20PM","2025-01-10 11:10PM","2025-01-11 09:00AM",
            "2025-01-09 02:00PM","2025-01-10 08:00PM",
            "2025-01-10 07:00PM","2025-01-10 08:00PM","2025-01-10 09:30PM"
        ],
        "duration(sec)":[180,60,200,90,150,70,200,300],
        "tower_city":["Mumbai","Pune","Delhi","Delhi","Mumbai","Chennai","Pune","Delhi"]
    })

    st.subheader("👀 Big Data Like Logs")
    st.table(df)

    col1,col2,col3 = st.columns(3)

    with col1:
        if st.button("📞 Get All Calls of User 101"):
            st.success(df[df["user_id"]==101])

    with col2:
        if st.button("📊 Total Usage of 101"):
            total = df[df["user_id"]==101]["duration(sec)"].sum()
            st.success(f"Total Duration = {total} sec")

    with col3:
        if st.button("🏙 Usage by City"):
            st.success(df.groupby("tower_city")["duration(sec)"].sum())

    st.warning("""
### KEY CONCEPT
SQL reads **row by row**
Column DB reads **column by column**
So analytics becomes extremely FAST
""")


# ==============================================
# GRAPH DB
# ==============================================
elif db_type.startswith("🕸"):
    st.header("🕸 Graph Database — Neo4j Style")
    st.write("Stores Big Data as Nodes + Relationships. Perfect for fraud + social networks.")

    st.subheader("👀 Stored Relationship Data")
    st.markdown("""
```
(User A) ---- TRANSFERRED ----> (Account X)
(Account X) ---- TRANSFERRED ----> (Account Y)
(Account Y) ---- OWNS ----> (User B)

(User C) ---- FRIEND ----> (User A)
(User A) ---- FRIEND ----> (User D)
```
""")

    col1,col2 = st.columns(2)

    with col1:
        if st.button("🔎 See Network Linked to User A"):
            st.success("User A → Account X → Account Y → User B")

    with col2:
        if st.button("🚨 Detect Fraud Pattern"):
            st.error("Suspicious Money Flow Detected ⚠")

    st.info("""
### Why Graph DB?
✔ Handles billions of relationships  
✔ Perfect for fraud detection  
✔ Social network analysis  
✔ Recommendation engines  
""")


# ==============================================
# SQL VS COLUMN
# ==============================================
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


# ==============================================
# ECONOMICS BIG DATA
# ==============================================
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


# ==============================================
# MULTIMEDIA STORAGE
# ==============================================
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
