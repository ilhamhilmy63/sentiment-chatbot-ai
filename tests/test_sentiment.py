from src.analyzer import analyze_sentiment


def test_positive_sentiment():

    result = analyze_sentiment(
        "I love this product"
    )

    assert result["sentiment"] == "Positive"


def test_negative_sentiment():

    result = analyze_sentiment(
        "This is terrible"
    )

    assert result["sentiment"] == "Negative"