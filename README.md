🚀 Features
🔹 Core Features (CLI Version)
➕ Add new expenses

📄 View all expenses

🔍 Filter expenses by category

📅 Filter expenses by month

💰 View total spending

🗑 Delete an expense

💾 Persistent storage using SQLite database

🔹 Dashboard Features (Web App Version)
🔐 User Login & Registration System

👤 User-specific expense tracking

📊 Category-wise spending visualization

📈 Monthly expense trend analysis

💰 Total spending metrics

📂 Interactive financial dashboard

🗄 Secure data storage using SQLite

🛠 Tech Stack
Backend
Python 3

SQLite (Built-in lightweight database)

Data Processing
Pandas (Data analysis & aggregation)

Visualization
Matplotlib (CLI version)

Plotly (Web dashboard interactive graphs)

Web Framework
Streamlit (Frontend + Backend for web app)

expense-tracker/
│
├── app.py                # Streamlit Web Application
├── cli_version.py        # CLI Version
├── database.db           # SQLite Database (auto-generated)
├── requirements.txt
└── README.md

📊 Dashboard Analytics
The web dashboard includes:

🥧 Category-wise Spending (Pie Chart)

📈 Monthly Expense Trend (Line Chart)

📌 Total Spending KPI

👤 User-specific Financial Data

🔒 Data Storage
All user credentials and expense records are stored in a SQLite database.

Each user can only view their own expenses.

Future upgrade includes secure password hashing.

🌍 Future Scope
🔐 Implement encrypted password storage (bcrypt)

📊 Budget limit tracking & alert system

📈 AI-based spending prediction (Machine Learning integration)

📱 Responsive mobile-friendly UI

☁️ Cloud deployment (Streamlit Cloud / Render / AWS)

📥 Export data as CSV / Excel

💳 Expense categorization using NLP

📊 Advanced analytics (Savings rate, anomaly detection)



