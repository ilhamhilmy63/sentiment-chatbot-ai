from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from src.config import (
    POSITIVE_THRESHOLD,
    NEGATIVE_THRESHOLD
)

analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment(text: str) -> dict:

    scores = analyzer.polarity_scores(text)

    compound_score = scores["compound"]

    if compound_score >= POSITIVE_THRESHOLD:
        sentiment = "Positive"

    elif compound_score <= NEGATIVE_THRESHOLD:
        sentiment = "Negative"

    else:
        sentiment = "Neutral"

    confidence = max(
        scores["pos"],
        scores["neg"],
        scores["neu"]
    ) * 100

    confidence = round(confidence, 2)

    return {
        "sentiment": sentiment,
        "confidence": confidence,
        "scores": scores
    }