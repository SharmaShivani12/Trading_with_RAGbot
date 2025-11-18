✅ FULLY CORRECTED README SECTION (Copy–Paste This)
# 📊 Crypto Trading Assistant — Multi-Agent LLM System
### _A Kaggle Agents Intensive Capstone Project — Freestyle Track_

This project is an **AI-powered Crypto Trading Assistant** that combines:

- Real-time market data  
- Rule-based trading signals  
- Multi-agent portfolio construction  
- RAG-based question answering  
- Streamlit interactive UI  

Designed for the **Google x Kaggle 5-Day AI Agents Intensive Capstone**, Freestyle Track.

---

# 🚀 Features

## 🔹 1. Real-Time Market Tools (CoinGecko API)
- Live price lookups  
- 7-day trend analysis  
- Automatic chart generation  
- Rule-based Buy/Sell signals  

## 🔹 2. RAG-Powered Q&A
The system can intelligently answer:
- General crypto questions  
- Blockchain terminology  
- Market explanations  

Using retrieval-augmented generation.

---

# 🔹 3. NEW: Multi-Agent Portfolio Bucket System

### Included Agents:
- **Preference Agent**  
- **Universe Agent**  
- **Bucket Builder Agent**  
- **Backtest Agent**  
- **Controller Agent**  

---

# 🧩 How the Bucket Pipeline Works

## **1️⃣ User Preference Extraction**

Query:
> “Create a low-risk portfolio with 5 coins for 30 days”

Extracted:

```json
{
  "risk": "conservative",
  "num_coins": 5,
  "horizon_days": 30
}

2️⃣ Universe Selection
["btc", "eth", "ada", "dot", "xrp", "sol"]

3️⃣ Bucket Construction

Portfolios generated:

Conservative
Balanced
Aggressive


All with equal weighting.

4️⃣ Backtesting Example Output
{
  "name": "Balanced",
  "total_return_pct": 12.4,
  "coins": [
    {"symbol": "eth", "weight": 0.25, "return_pct": 10.2},
    {"symbol": "dot", "weight": 0.25, "return_pct": 15.0}
  ]
}

🔍 Query Routing Logic

If the query is:

Definitions / concepts / risks → RAG

Prices / trends / signals → API + charts

Portfolio request → Multi-Agent Pipeline

🖥 Running the App

Install dependencies:

pip install -r requirements.txt


Run Streamlit:

streamlit run app.py

📸 Screenshots
Dashboard
<img width="940" src="https://github.com/user-attachments/assets/71803801-9122-4e47-ae66-8c26714502bd" />
Portfolio Bucket Output
<img width="940" src="https://github.com/user-attachments/assets/76c1f4b1-b6a3-4774-8796-65d80abb442e" />
RAG Explanation
<img width="940" src="https://github.com/user-attachments/assets/c18daf15-3062-4d86-8211-058f7d7c25c4" />
📝 License

CC-BY-SA 4.0

🙌 Acknowledgements

Google & Kaggle

CoinGecko API

Streamlit

Open-source LLM community

If the query is about definitions, concepts, risks, or general knowledge → it’s answered with RAG.

If the query is about prices, trends, buy/sell signals → it’s answered with API + charts.

🖥 Running the App
Install dependencies : pip install -r requirements.txt
Run Streamlit : streamlit run app.py


📝 License

This project is licensed under CC-BY-SA 4.0, as required for Kaggle Capstone winners.

🙌 Acknowledgements

Google & Kaggle — Agents Intensive Course

CoinGecko API — Market Data

Streamlit — UI Framework

Open-source LLM community

📸 Screenshots:

Dashboard

<img width="940" alt="image" src="https://github.com/user-attachments/assets/71803801-9122-4e47-ae66-8c26714502bd" />

Portfolio Bucket Output

<img width="940" alt="image" src="https://github.com/user-attachments/assets/76c1f4b1-b6a3-4774-8796-65d80abb442e" />

RAG Explanation

<img width="940" alt="image" src="https://github.com/user-attachments/assets/c18daf15-3062-4d86-8211-058f7d7c25c4" />



<img width="940" height="488" alt="image" src="https://github.com/user-attachments/assets/71803801-9122-4e47-ae66-8c26714502bd" />

<img width="940" height="462" alt="image" src="https://github.com/user-attachments/assets/76c1f4b1-b6a3-4774-8796-65d80abb442e" />

<img width="940" height="459" alt="image" src="https://github.com/user-attachments/assets/c18daf15-3062-4d86-8211-058f7d7c25c4" />




