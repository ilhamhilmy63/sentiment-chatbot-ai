# 🤖 AI Sentiment Analysis Chatbot

A simple yet powerful AI-powered chatbot that performs real-time sentiment analysis on user input using NLP (VADER Sentiment Analysis) and responds intelligently based on detected sentiment.

---

## 🚀 Features

- 🔍 Real-time sentiment detection (Positive, Negative, Neutral)
- 📊 Confidence score for predictions
- 💬 Interactive chatbot interface (Streamlit)
- 🧠 Intelligent AI-based responses
- 🗂️ Chat history tracking
- 🗑️ Delete individual chat messages
- 🧹 Clear all chat history
- ⚡ Lightweight and fast NLP model (VADER)

---

## 🧠 Tech Stack

- Python 🐍
- Streamlit 🎈
- VADER Sentiment Analysis (NLTK)
- Logging System
- Session State Management

---

## 📁 Project Structure
sentiment-chatbot-ai/
│── app.py
│── requirements.txt
│── README.md
│── assets/
│ └── (screenshots / UI images)
│── src/
│ ├── analyzer.py
│ ├── responder.py
│ ├── utils.py
│ ├── config.py
│ └── logger.py

The confidence score represents the strength of the sentiment detected in the input text.

It is derived from the VADER sentiment analyzer's **compound score**, which ranges from -1 (very negative) to +1 (very positive).

---

### ⚙️ Calculation Logic:

The confidence score is calculated using the formula:

```python id="conf_formula"
confidence = abs(compound_score) * 100
