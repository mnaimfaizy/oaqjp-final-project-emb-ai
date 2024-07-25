"""
Emotion Detection Flask App
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_detection():
    """
    Endpoint for emotion detection.
    
    Retrieves text from the query parameters, analyzes the text for emotions,
    and returns a formatted string with the emotions and the dominant emotion.
    """
    text = request.args.get('textToAnalyze')
    print(text)

    response = emotion_detector(text)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} "
        f"and 'sadness': {response['sadness']}. " 
        f"The dominant emotion is {response['dominant_emotion']}"
    )

@app.route("/")
def render_index_page():
    """
    Renders the index page.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
