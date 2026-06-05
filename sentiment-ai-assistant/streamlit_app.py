import streamlit as st

from src.analyzer import analyze_sentiment
from src.responder import generate_response
from src.utils import validate_input
from src.logger import setup_logger
from src.config import APP_TITLE

logger = setup_logger()

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🤖",
    layout="centered"
)

# ---------------- SESSION STATE ----------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- TITLE ----------------
st.title("🤖 AI Sentiment Analysis Assistant")

st.markdown(
    """
    Welcome to the AI-powered sentiment assistant.

    Enter any message and the AI will:

    - Detect sentiment
    - Calculate confidence score
    - Generate intelligent responses
    """
)

# ================= SIDEBAR (IMPROVED) =================
st.sidebar.title("🤖 AI Assistant Panel")

st.sidebar.markdown("---")

# 📊 CHAT STATISTICS
st.sidebar.subheader("📊 Chat Statistics")

total_chats = len(st.session_state.chat_history)
st.sidebar.metric("Total Messages", total_chats)

if total_chats > 0:
    positive = sum(1 for c in st.session_state.chat_history if c["sentiment"] == "Positive")
    negative = sum(1 for c in st.session_state.chat_history if c["sentiment"] == "Negative")
    neutral = sum(1 for c in st.session_state.chat_history if c["sentiment"] == "Neutral")

    st.sidebar.write("Sentiment Breakdown:")
    st.sidebar.write(f"🟢 Positive: {positive}")
    st.sidebar.write(f"🔴 Negative: {negative}")
    st.sidebar.write(f"⚪ Neutral: {neutral}")

st.sidebar.markdown("---")

# 🎛 CONTROLS
st.sidebar.subheader("🎛 Controls")

if st.sidebar.button("🧹 Clear All Chats"):
    st.session_state.chat_history = []
    st.success("Chat history cleared!")

show_confidence = st.sidebar.toggle("📊 Show Confidence Score", value=True)

st.sidebar.markdown("---")

# ℹ️ ABOUT
st.sidebar.subheader("ℹ️ About This App")

st.sidebar.info(
    """
    🤖 AI Sentiment Chatbot  
    🧠 VADER NLP Model  
    💬 Real-time sentiment analysis  
    """
)

st.sidebar.markdown("---")

# 👨‍💻 DEVELOPER
st.sidebar.subheader("👨‍💻 Developer")

st.sidebar.success("Built by Ilham")
st.sidebar.caption("Internship Project • AI Engineering Task")

# ---------------- USER INPUT ----------------
user_input = st.text_area(
    "Enter your message:",
    height=120
)

# ---------------- ANALYZE BUTTON ----------------
if st.button("Analyze Sentiment"):

    if not validate_input(user_input):
        st.warning("⚠ Please enter a valid message.")

    else:

        try:
            result = analyze_sentiment(user_input)

            sentiment = result["sentiment"]
            confidence = result["confidence"]

            bot_response = generate_response(sentiment)

            logger.info(
                f"Input: {user_input} | Sentiment: {sentiment}"
            )

            st.success(f"Detected Sentiment: {sentiment}")

            st.progress(int(confidence))

            if show_confidence:
                st.metric("Confidence Score", f"{confidence}%")

            st.write("### 🤖 AI Response")
            st.write(bot_response)

            st.session_state.chat_history.append({
                "message": user_input,
                "sentiment": sentiment,
                "confidence": confidence,
                "response": bot_response
            })

        except Exception as error:
            logger.error(str(error))
            st.error("An unexpected error occurred.")

# ---------------- CHAT HISTORY ----------------
if st.session_state.chat_history:

    st.write("---")
    st.write("## 💬 Conversation History")

    for i, chat in enumerate(reversed(st.session_state.chat_history)):

        st.write(f"👤 {chat['message']}")
        st.write(
            f"📊 {chat['sentiment']} ({chat['confidence']}%)"
        )
        st.write(f"🤖 {chat['response']}")

        # DELETE SINGLE CHAT
        if st.button(f"🗑️ Delete Chat {i}", key=f"del_{i}"):

            st.session_state.chat_history.pop(
                len(st.session_state.chat_history) - 1 - i
            )
            st.rerun()

        st.write("---")

st.caption("Built by Ilham")