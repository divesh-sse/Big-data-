import streamlit as st
import pandas as pd

st.set_page_config(page_title="NoSQL Interactive Demo", layout="wide")
st.title("🧠 Interactive NoSQL Databases Demo")
st.write("Press buttons, retrieve data, and visually understand how each NoSQL database works — including SQL comparison & economics example!")

db_type = st.sidebar.radio(
    "Choose Database Type",
    [
        "📄 Document DB (MongoDB Style)",
        "🔑 Key–Value Store (Redis Style)",
        "📚 Column Store (Cassandra / HBase)",
        "🕸 Graph Database (Neo4j)",
        "🆚 SQL vs Column Store Comparison",
        "💰 Economics Big Data (UPI Example)"
    ]
)

# --------------------- DOCUMENT DB ----------------------
if db_type.startswith("📄"):
    st.header("📄 Document Database — MongoDB Style")
    st.write("Stores data as **JSON-like documents**, flexible structure, no fixed columns.")

    sample_doc = {
        "product_id": "P101",
        "name": "iPhone 16",
        "price": 79999,
        "category": "Mobile",
        "features": ["AI Camera", "Fast Chip"],
        "ratings": [
            {"user": "Riya", "rating": 5},
            {"user": "Amit", "rating": 4}
        ]
    }

    st.subheader("👀 Stored Document")
    st.json(sample_doc)

    st.subheader("🎯 Try Retrieving Data")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Get Mobile Products"):
            st.success("📦 Found: iPhone 16 — Category: Mobile")

    with col2:
        if st.button("Get Products Above ₹50,000"):
            st.success("💎 iPhone 16 — ₹79,999")

    with col3:
        if st.button("Get Average Rating"):
            st.success("⭐ Average Rating = 4.5")


    st.info("""
### Why Document DB?
- Looks like JSON
- Different records can have different fields
- Super flexible
""")

# --------------------- KEY VALUE ----------------------
elif db_type.startswith("🔑"):
    st.header("🔑 Key–Value Store — Redis Style")
    st.write("Stores data as **Key → Value**. Extremely fast. Perfect for real-time.")

    st.subheader("👀 How Data is Stored")
    st.code("""
"user:101"  →  { name: "Riya", plan: "Premium", status: "Watching" }
"session:77" → Active
"video:views" → 10592
""")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Get User 101"):
            st.success("{ name:'Riya', plan:'Premium'}")

    with col2:
        if st.button("Check Session"):
            st.success("Session Active")

    with col3:
        if st.button("Increase Views"):
            st.success("Views Updated ✔")

    st.info("""
### Why Key–Value?
- Blazing fast
- Perfect for cache, sessions, live events
- Used by Netflix, Gaming, Banking OTP
""")

# --------------------- COLUMN STORE ----------------------
elif db_type.startswith("📚"):
    st.header("📚 Column Store — Cassandra / HBase")
    st.write("Stores data **column-wise**, perfect for analytics & big data")

    st.subheader("👀 Example Telecom Call Logs (Stored Data)")
    df = pd.DataFrame({
        "user_id": [101,101,102],
        "date_time": ["2025-01-10 10:20PM","2025-01-10 11:10PM","2025-01-10 09:00PM"],
        "duration(sec)": [180,60,200],
        "tower_city": ["Mumbai","Pune","Delhi"]
    })
    st.table(df)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Get All Calls of User 101"):
            st.success("""
101 | 2025-01-10 10:20PM | 180 sec | Mumbai
101 | 2025-01-10 11:10PM | 60 sec | Pune
""")

    with col2:
        if st.button("Get Last 1 Call"):
            st.success("101 → 60 sec | Pune")

    with col3:
        if st.button("Get Total Usage of 101"):
            st.success("Total = 240 sec")

    st.warning("""
### Clear Understanding
SQL reads **row by row**
Column DB reads **column by column**
So analytics becomes SUPER FAST
""")

# --------------------- GRAPH DB ----------------------
elif db_type.startswith("🕸"):
    st.header("🕸 Graph Database — Neo4j Style")
    st.write("Focus on **relationships**. Stores data as Nodes + Connections.")

    st.subheader("👀 Conceptual Stored Data")
    st.markdown("""
```
(User A) ---- TRANSFERRED ----> (Account X)
(Account X) ---- TRANSFERRED ----> (Account Y)
(Account Y) ---- OWNED BY ----> (User B)
```
""")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Find Connections of User A"):
            st.success("User A → Account X → Account Y → User B")

    with col2:
        if st.button("Detect Fraud Ring"):
            st.error("⚠ Suspicious Loop Detected")

    st.info("""
### Why Graph DB?
- Best for fraud detection
- Best for social networks
- Best for recommendations
""")

# --------------------- SQL VS COLUMN STORE ----------------------
elif db_type.startswith("🆚"):
    st.header("🆚 SQL vs Column Store — Visual Clarity")

    st.subheader("SQL (Row Based)")
    st.code("""
| user_id | city   | duration |
|--------|--------|---------|
| 101    | Mumbai | 180     |
| 101    | Pune   | 60      |
| 102    | Delhi  | 200     |
""")

    st.subheader("Column Store (Column Based)")
    st.code("""
user_id:   101, 101, 102
city:      Mumbai, Pune, Delhi
duration:  180, 60, 200
""")

    if st.button("Retrieve Duration for Analytics"):
        st.success("Column DB retrieves duration instantly ⚡")

    st.info("""
SQL = best for transactions  
Column Store = best for analytics
""")

# --------------------- ECONOMICS EXAMPLE ----------------------
else:
    st.header("💰 Economics Big Data — UPI Example")
    st.write("Millions of UPI transactions per minute. NoSQL powers this.")

    st.subheader("👀 Transaction as Document")
    st.json({
        "txn_id":"UPI99229",
        "amount":280,
        "city":"Pune",
        "merchant":"Zomato",
        "time":"10:22PM"
    })

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("Store Transaction"):
            st.success("Stored in Document DB")

    with col2:
        if st.button("Analyze Spending"):
            st.success("Column DB → City spending trends")

    with col3:
        if st.button("Apply Cashback"):
            st.success("Key-Value DB → Fast decision")

    with col4:
        if st.button("Detect Fraud Network"):
            st.error("Graph DB Found Suspicious Links")

    st.success("This is real Big Data happening in our economy every second 🚀")
