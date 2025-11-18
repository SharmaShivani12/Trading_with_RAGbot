import streamlit as st
import src.chat  # this loads chat.py directly

from src.market import get_latest_price, COIN_MAP
from controller import route_query


st.set_page_config(page_title="Trading Assistant", page_icon="📊", layout="wide")

st.title("📊 Crypto Trading Assistant")

# ------------------------
# Sidebar: Quick Market Check
# ------------------------
st.sidebar.subheader("⚡ Quick Check")

coin = st.sidebar.selectbox("Select a coin", list(COIN_MAP.keys()), index=0)

if st.sidebar.button("Get Latest Price"):
    try:
        price = get_latest_price(coin)
        st.sidebar.success(f"Latest {coin.upper()} price: ${price:.2f}")
    except Exception as e:
        st.sidebar.error(f"⚠️ Could not fetch price for {coin.upper()}. Error: {e}")

# ------------------------
# Chat Interface
# ------------------------
st.subheader("💬 Ask the Trading Assistant")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])
# Input box
if user_input := st.chat_input("Type your crypto question..."):
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # -----------------------------------------
    # 0. Controller handles bucket / portfolio queries FIRST
    # -----------------------------------------
    route, result = route_query(user_input)

    if route == "bucket":
        st.subheader("🧺 Portfolio Bucket Recommendation")
        st.json(result)

        # Save assistant message
        st.session_state["messages"].append({
            "role": "assistant",
            "content": "Generated a portfolio bucket recommendation (see output above)."
        })
        st.chat_message("assistant").write(
            "Generated a portfolio bucket recommendation (see output above)."
        )

    else:
        # -----------------------------------------
        # FALL BACK to your existing agent pipeline
        # (intent model → RAG → live market tools etc.)
        # -----------------------------------------

        response = master_chatbot(user_input)

        st.session_state["messages"].append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)

# Input box
if user_input := st.chat_input("Type your crypto question..."):
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Always use master_chatbot (intent + RAG + live market)
    response = master_chatbot(user_input)

    st.session_state["messages"].append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
