import openai
import os
from openai import OpenAI 
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Intialize Flask app
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index1.html')


@app.route('/generateimages/<prompt>')
def generate(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_data = response.data[0] 
    return jsonify({"url": image_data.url,
        "revised_prompt": image_data.revised_prompt})


# to run the application:
app.run(host="0.0.0.0",debug=True,port=8080)
    
