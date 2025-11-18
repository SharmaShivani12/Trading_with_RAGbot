# 📊 Crypto Trading Assistant — Multi-Agent LLM System  
_A Kaggle Agents Intensive Capstone Project — Freestyle Track_

This project is an **AI-powered Crypto Trading Assistant** that combines:

- **Real-time market data**
- **Rule-based trading signals**
- **Multi-agent portfolio construction**
- **RAG-based question answering**
- **Streamlit interactive UI**

It is designed for the Google x Kaggle **5-Day AI Agents Intensive Capstone**, Freestyle Track.

---

## 🚀 Features

### 🔹 1. Real-Time Market Tools (CoinGecko API)
- Live price lookups  
- 7-day trend analysis  
- Automatic chart generation  
- Rule-based Buy/Sell signals  

### 🔹 2. RAG-Powered Q&A  
Using a retrieval-augmented generation pipeline, the assistant can answer:

- General crypto questions  
- Blockchain terminology queries  
- Market concept explanations  

### 🔹 3. **NEW: Multi-Agent Portfolio Bucket System**
This upgrade introduces a full **multi-agent crypto portfolio constructor**:

**Agents included:**
1. **Preference Agent** — extracts user intents (risk level, #coins, time horizon)  
2. **Universe Agent** — selects candidate coins  
3. **Bucket Construction Agent** — builds Conservative / Balanced / Aggressive portfolios  
4. **Backtest Agent** — evaluates returns based on historical market data  
5. **Controller Agent** — routes user queries to the correct agent pipeline  

This satisfies the **Multi-Agent** and **Tools** requirements for the Capstone.

### 🔹 4. Interactive Streamlit UI
Users can:
- Ask natural-language questions  
- Request bucket portfolios  
- Trigger trend or price charts  
- View RAG explanations  
- Retrieve market data instantly  

---

## 🧠 System Architecture

                ┌───────────────────────────┐
                │       Streamlit UI        │
                │  (User chat & dashboard)  │
                └──────────────┬────────────┘
                               │
                               ▼
                ┌───────────────────────────┐
                │     Controller Agent      │
                │  (Intent Routing Engine)  │
                └───────────┬─────┬─────────┘
                            │     │
      ┌─────────────────────┘     └────────────────────────────┐
      ▼                                                         ▼
┌───────────────┐                                    ┌───────────────────────┐
│ Portfolio Path│                                    │  Trading / RAG Path   │
└───────┬───────┘                                    └──────────┬────────────┘
        │                                                       │
        ▼                                                       ▼
┌────────────────────┐                                ┌───────────────────────┐
│ 1.Preferences Agent│                                │ Market Data Agent     │
│ Extract risk, size │                                │ - Price, Trend, Signal│
└─────────┬──────────┘                                └──────────┬────────────┘
          │                                                      │
          ▼                                                      ▼
┌────────────────────────┐                             ┌─────────────────────────┐
│ 2. Universe Agent      │                            │ RAG Knowledge Agent     │
│ Select candidate coins │                            │ Explain concepts        │
└───────────┬────────────┘                             └──────────┬───────────--─┘
            │                                                     │
            ▼                                                     ▼
┌────────────────────────┐                             ┌─────────────────────────┐
│ 3. Bucket Builder Agent│                             │ Response Generator      │
│ Create Conservative /  │                             │ Final formatted answer  │
│ Balanced / Aggressive  │                             │                         │
└──────────┬─────────────┘                             └─────────────────────────┘
           │
           ▼
┌──────────────────────────┐
│ 4. Backtest Agent        │
│ Evaluate portfolio return│
└──────────────────────────┘
---

## 🧩 How the Bucket Pipeline Works

### **1️⃣ User Preference Extraction**
Example query:

> “Create a low-risk portfolio with 5 coins for the next 30 days”

Parsed preferences:

```json
{
  "risk": "conservative",
  "num_coins": 5,
  "horizon_days": 30
}
2️⃣ Universe Selection
Based on COIN_MAP in market.py.

Example:

css
Copy code
["btc", "eth", "ada", "dot", "xrp", "sol", ...]
3️⃣ Bucket Construction
Builds three portfolios:

Conservative

Balanced

Aggressive

Each with equal weights.

4️⃣ Backtesting
Uses historical price data to estimate:

Per-coin return

Portfolio return

Example:

json
Copy code
{
  "name": "Balanced",
  "total_return_pct": 12.4,
  "coins": [
    {"symbol": "eth", "weight": 0.25, "return_pct": 10.2},
    {"symbol": "dot", "weight": 0.25, "return_pct": 15.0},
    ...
  ]
}
🖥 Running the App
Install dependencies
bash
Copy code
pip install -r requirements.txt
Run Streamlit
bash
Copy code
streamlit run app.py
🎯 Example Queries to Try
Portfolio / Bucket Queries
“Build a conservative crypto bucket.”

“Create a 5-coin aggressive portfolio.”

“I want a balanced portfolio for the next 90 days.”

Trading Queries
“Show me the 7-day trend of ETH.”

“What is the price of BTC?”

“Should I buy SOL today?”

RAG Queries
“Explain proof-of-stake.”

“What is Bitcoin halving?”

“What is a liquidity pool?”


If the query is about definitions, concepts, risks, or general knowledge → it’s answered with RAG.
If the query is about prices, trends, buy/sell signals → it’s answered with API + charts.

📝 License

This project is licensed under CC-BY-SA 4.0, as required for Kaggle Capstone winners.

🙌 Acknowledgements

Google & Kaggle — Agents Intensive Course

CoinGecko API — Market Data

Streamlit — UI Framework

Open-source LLM community

Screenshots:

<img width="940" height="488" alt="image" src="https://github.com/user-attachments/assets/71803801-9122-4e47-ae66-8c26714502bd" />
<img width="940" height="462" alt="image" src="https://github.com/user-attachments/assets/76c1f4b1-b6a3-4774-8796-65d80abb442e" />
<img width="940" height="459" alt="image" src="https://github.com/user-attachments/assets/c18daf15-3062-4d86-8211-058f7d7c25c4" />




