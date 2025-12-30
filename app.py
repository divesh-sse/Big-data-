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
    st.header("🕸 Graph Database — Real Relationship Demo (Banking Fraud Style)")

    st.write("Graph DB stores **nodes + relationships**, not tables.")

    # ========= SAMPLE GRAPH DATA (Big Network) =========
    graph = {
        "UserA": ["AccX", "UserC"],
        "AccX": ["AccY"],
        "AccY": ["UserB"],
        "UserC": ["UserD", "AccZ"],
        "AccZ": ["UserB"],
        "UserD": ["UserE"],
        "UserB": [],
        "UserE": []
    }

    st.subheader("📌 Stored Graph Network")
    st.code("""
UserA ─→ AccX ─→ AccY ─→ UserB
   │
   └─→ UserC ─→ UserD ─→ UserE
               │
               └─→ AccZ ─→ UserB
""")

    # ========= UTIL FUNCTIONS =========
    import collections

    def bfs_path(graph, start, goal):
        """Breadth-first traversal to find relationship path (like Neo4j MATCH traversal)"""
        queue = collections.deque([[start]])
        visited = set()

        while queue:
            path = queue.popleft()
            node = path[-1]
            if node == goal:
                return path
            if node not in visited:
                visited.add(node)
                for neighbour in graph.get(node, []):
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
        return None

    def detect_suspicious_patterns(graph):
        """Detect risky graph behavior"""
        suspicious_reasons = []

        # Rule 1 — multiple routes leading to same user (like mule accounts)
        targets = collections.Counter()
        for node in graph:
            for n in graph[node]:
                targets[n] += 1

        for k,v in targets.items():
            if v >= 2:
                suspicious_reasons.append(f"Node '{k}' is receiving money via MULTIPLE paths ({v} sources)")

        # Rule 2 — long transaction chain
        for node in graph:
            path = bfs_path(graph, "UserA", node)
            if path and len(path) >= 5:
                suspicious_reasons.append(f"Very long transaction trail detected → {' → '.join(path)}")

        # Rule 3 — Cycles check
        visited = set()
        stack = set()

        def has_cycle(v):
            visited.add(v)
            stack.add(v)
            for n in graph.get(v, []):
                if n not in visited:
                    if has_cycle(n):
                        return True
                elif n in stack:
                    return True
            stack.remove(v)
            return False

        if has_cycle("UserA"):
            suspicious_reasons.append("Circular money movement detected (Cycle)")

        return suspicious_reasons


    col1, col2, col3 = st.columns(3)

    # ========= TRAVERSE NETWORK =========
    with col1:
        if st.button("🔎 Trace Network From UserA"):
            st.success("Traversal Order (BFS from UserA):")
            visited = []
            queue = ["UserA"]

            while queue:
                node = queue.pop(0)
                if node not in visited:
                    visited.append(node)
                    for n in graph.get(node, []):
                        queue.append(n)

            for v in visited:
                st.write("➡", v)

    # ========= FIND PATH BETWEEN ANY NODES =========
    with col2:
        st.subheader("Find Relationship Path")
        start = st.selectbox("From", list(graph.keys()))
        end = st.selectbox("To", list(graph.keys()))

        if st.button("📍 Find Path"):
            path = bfs_path(graph, start, end)
            if path:
                st.success(" → ".join(path))
            else:
                st.error("No relationship path found")

    # ========= FRAUD DETECTION =========
    with col3:
        if st.button("🚨 Detect Suspicious Behavior"):
            results = detect_suspicious_patterns(graph)

            if results:
                st.error("⚠ Suspicious Patterns Found:")
                for r in results:
                    st.write("•", r)
            else:
                st.success("No suspicious network patterns detected ✔")

    # ========= SHOW RAW GRAPH STORAGE =========
    st.subheader("🗂 How Graph is Actually Stored Internally")
    st.json(graph)

    st.info("""
Graph DB helps banks, social networks, fraud systems by:
✔ Understanding relationships
✔ Finding hidden connections
✔ Detecting money laundering chains
✔ Following paths between entities
""")


# =========================================================
# SQL vs COLUMN
# =========================================================
elif db_type.startswith("🆚"):
    import time
    st.header("🆚 SQL vs Column Store — Deep Clarity with REAL Demo")

    st.write("Below is the SAME DATA but accessed differently — Row Based vs Column Based.")

    # ---------- CREATE BIG DATASET ----------
    import numpy as np
    import pandas as pd

    if "sql_data" not in st.session_state:
        rows = 50000  # feel like big data 🙂
        st.session_state.sql_data = pd.DataFrame({
            "user_id": np.random.randint(100, 500, rows),
            "city": np.random.choice(["Mumbai","Delhi","Pune","Chennai","Bangalore"], rows),
            "duration": np.random.randint(30, 600, rows)
        })

    df = st.session_state.sql_data

    st.subheader("📂 Sample of Stored Data (Big Data Feel)")
    st.write(df.head(10))

    col1, col2 = st.columns(2)

    # ---------- SQL STYLE ROW RETRIEVAL ----------
    with col1:
        st.subheader("🧱 SQL (Row Based Retrieval)")
        if st.button("Retrieve Duration using SQL Style (Row Scan)"):
            start = time.perf_counter()

            durations_sql = []
            for _, row in df.iterrows():   # row by row scan
                durations_sql.append(row["duration"])

            end = time.perf_counter()

            st.write("Retrieved duration values (first 10):", durations_sql[:10])
            st.error(f"⏱ SQL Retrieval Time: {round((end-start)*1000, 2)} ms")
            st.caption("SQL scans each row → then extracts column → slower")

    # ---------- COLUMN STORE STYLE ----------
    with col2:
        st.subheader("📚 Column Store (Column Retrieval)")
        if st.button("Retrieve Duration using Column Store"):
            start = time.perf_counter()

            durations_column = df["duration"]  # direct column access

            end = time.perf_counter()

            st.write("Retrieved duration values (first 10):", durations_column.head(10).tolist())
            st.success(f"⚡ Column DB Retrieval Time: {round((end-start)*1000, 2)} ms")
            st.caption("Column DB reads ONLY needed column → super fast")

    # ---------- VISUAL EXPLANATION ----------
    st.markdown("---")
    st.subheader("🧠 Visual Understanding")

    st.code("""
SQL (Row Storage):
[ 101 | Mumbai | 120 ]
[ 102 | Pune   | 300 ]
Reads entire row → THEN picks duration

Column Store:
duration: 120, 300, 240, 500...
Reads ONLY duration column directly
""")

    st.success("NOW the performance and storage difference is TRULY visible 😎")


# =========================================================
# ECONOMICS
# =========================================================
elif db_type.startswith("💰"):
    st.header("💰 Economics Big Data — UPI India Example")

    # ---------- SESSION STATE FOR REAL STORAGE ----------
    if "transactions" not in st.session_state:
        st.session_state.transactions = []

    # ---------- CREATE RANDOM TRANSACTION ----------
    new_txn = {
        "txn_id":"UPI" + str(random.randint(10000,99999)),
        "amount":random.randint(100,5000),
        "city":random.choice(["Pune","Mumbai","Delhi","Chennai","Bangalore"]),
        "merchant": random.choice(["Zomato","Swiggy","Amazon","Paytm","Myntra"]),
        "payer": random.choice(["UserA","UserB","UserC","UserD","UserE"])
    }

    st.subheader("👀 Incoming UPI Transaction (like LIVE stream)")
    st.json(new_txn)

    col1,col2,col3,col4 = st.columns(4)

    # ---------- STORE ----------
    with col1:
        if st.button("💾 Store Transaction"):
            st.session_state.transactions.append(new_txn)
            st.success("Stored in Document DB ✔")

    # ---------- ANALYTICS ----------
    with col2:
        if st.button("📊 Analyze Spending Trends"):
            if len(st.session_state.transactions)==0:
                st.warning("Store some transactions first")
            else:
                df = pd.DataFrame(st.session_state.transactions)
                st.write("### City Wise Total Spend")
                st.bar_chart(df.groupby("city")["amount"].sum())

                st.write("### Merchant Popularity")
                st.bar_chart(df.groupby("merchant")["amount"].count())

    # ---------- CASHBACK ----------
    with col3:
        if st.button("🎁 Give Cashback Decision"):
            if len(st.session_state.transactions)==0:
                st.warning("Store some transactions first")
            else:
                last = st.session_state.transactions[-1]
                if last["amount"] > 2000:
                    st.success(f"Cashback Approved 🎉 High Value Transaction from {last['merchant']}")
                else:
                    st.info("No Cashback — Small Value Transaction")

    # ---------- FRAUD DETECTION ----------
    with col4:
        if st.button("🚨 Detect Fraud"):
            if len(st.session_state.transactions) < 3:
                st.warning("Need more transactions to analyze fraud")
            else:
                df = pd.DataFrame(st.session_state.transactions)

                suspicious = False
                message = ""

                # Rule 1 – Same payer too many quick transactions
                payer_counts = df["payer"].value_counts()
                if payer_counts.max() >= 3:
                    suspicious = True
                    message += "Same user making too many payments quickly.\n"

                # Rule 2 – Same merchant repeatedly
                merchant_counts = df["merchant"].value_counts()
                if merchant_counts.max() >= 3:
                    suspicious = True
                    message += "Suspicious transactions to same merchant repeatedly.\n"

                # Rule 3 – Too many high value payments
                high_value = len(df[df["amount"]>3000])
                if high_value >= 3:
                    suspicious = True
                    message += "Multiple high value transactions detected.\n"

                if suspicious:
                    st.error("⚠ Fraud Pattern Detected\n" + message)
                else:
                    st.success("No suspicious behavior detected ✔")

    # ---------- SHOW STORED DB ----------
    st.subheader("📂 Stored Transactions Database")
    if len(st.session_state.transactions)==0:
        st.info("No transactions stored yet — press Store Transaction")
    else:
        st.table(pd.DataFrame(st.session_state.transactions))


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
