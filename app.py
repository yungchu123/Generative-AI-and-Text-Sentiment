from flask import Flask, request, jsonify, render_template
from textblob import TextBlob
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

# Helper function to generate an image URL based on user text
def generate_image_url(text):
    response = client.images.generate(
        model="dall-e-3",
        prompt=text,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    return image_url

# Helper function for sentiment analysis
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_polarity = blob.sentiment.polarity
    if sentiment_polarity > 0:
        return "Positive"
    elif sentiment_polarity < 0:
        return "Negative"
    else:
        return "Neutral"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    text = data.get('text')

    # Generate image (placeholder in this case)
    image_url = generate_image_url(text)

    # Analyze sentiment
    sentiment = analyze_sentiment(text)

    # Return both image URL and sentiment as a JSON response
    return jsonify({
        'image_url': image_url,
        'sentiment': sentiment
    })

if __name__ == '__main__':
    app.run(debug=True)
