import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
from datetime import datetime

# Database setup
conn = sqlite3.connect("database.db", check_same_thread=False)
c = conn.cursor()

# Create tables
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS expenses (
    username TEXT,
    date TEXT,
    category TEXT,
    amount REAL,
    description TEXT
)
''')

conn.commit()

# -----------------------
# Authentication Functions
# -----------------------

def register_user(username, password):
    try:
        c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except:
        return False

def login_user(username, password):
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    return c.fetchone()

# -----------------------
# App UI
# -----------------------

st.title("💰 Expense Tracker Dashboard")

menu = ["Login", "Register"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Register":
    st.subheader("Create Account")
    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type='password')

    if st.button("Register"):
        if register_user(new_user, new_pass):
            st.success("Account Created Successfully!")
        else:
            st.error("Username already exists")

elif choice == "Login":
    st.subheader("Login to Your Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        if login_user(username, password):
            st.session_state["user"] = username
            st.success("Login Successful")
        else:
            st.error("Invalid Credentials")

# -----------------------
# Dashboard
# -----------------------

if "user" in st.session_state:

    st.sidebar.success(f"Logged in as {st.session_state['user']}")

    st.header("Add Expense")
    date = st.date_input("Date")
    category = st.selectbox("Category", ["Food", "Travel", "Shopping", "Bills", "Other"])
    amount = st.number_input("Amount", min_value=0.0)
    description = st.text_input("Description")

    if st.button("Add Expense"):
        c.execute("INSERT INTO expenses VALUES (?, ?, ?, ?, ?)",
                  (st.session_state["user"], str(date), category, amount, description))
        conn.commit()
        st.success("Expense Added")

    st.header("Your Dashboard")

    df = pd.read_sql_query(
        "SELECT * FROM expenses WHERE username=?",
        conn,
        params=(st.session_state["user"],)
    )

    if not df.empty:
        df["date"] = pd.to_datetime(df["date"])

        total_spent = df["amount"].sum()
        st.metric("Total Spending", f"₹ {total_spent}")

        # Category Pie Chart
        cat_summary = df.groupby("category")["amount"].sum().reset_index()
        fig1 = px.pie(cat_summary, names="category", values="amount", title="Spending by Category")
        st.plotly_chart(fig1)

        # Monthly Trend
        df["month"] = df["date"].dt.to_period("M").astype(str)
        month_summary = df.groupby("month")["amount"].sum().reset_index()
        fig2 = px.line(month_summary, x="month", y="amount", title="Monthly Spending Trend")
        st.plotly_chart(fig2)
    else:
        st.info("No expenses added yet.")
