"""Flask app for emotion detection using IBM NLP API."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")


@app.route("/emotionDetector")
def sent_detector():
    """API endpoint that processes the text and returns emotion analysis."""
    text_to_analyze = request.args.get('textToAnalyze', '').strip()
    if not text_to_analyze:
        return "No input provided. Please enter some text."

    response = emotion_detector(text_to_analyze)

    # Handle possible errors returned by the emotion_detector
    if 'error' in response or response.get('dominant_emotion') is None:
        return "Invalid input or failed to analyze emotions. Try again."

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    return (
    f"For the given statement, the system response is "
    f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
    f"'joy': {joy}, 'sadness': {sadness}. "
    f"The dominant emotion is {dominant_emotion}."
)


@app.route("/")
def render_index_page():
    """Render the main HTML page."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
