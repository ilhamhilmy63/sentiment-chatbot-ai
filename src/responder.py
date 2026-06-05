from src.config import (
    POSITIVE_RESPONSE,
    NEGATIVE_RESPONSE,
    NEUTRAL_RESPONSE
)


def generate_response(sentiment: str) -> str:

    responses = {
        "Positive": POSITIVE_RESPONSE,
        "Negative": NEGATIVE_RESPONSE,
        "Neutral": NEUTRAL_RESPONSE
    }

    return responses.get(
        sentiment,
        "Thank you for your feedback."
    )