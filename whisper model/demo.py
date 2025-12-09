import openai
import os
from dotenv import load_dotenv
from openai import OpenAI 
from flask import Flask, request, jsonify, render_template 


# Load environment variables from .env file
load_dotenv()
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

# to open audio file
with open("Recording.mp3", "rb") as audio:
    # Translate audio using OpenAI Whisper
    output = client.audio.translations.create(
        model = "whisper-1",
        file = audio,
        response_format = "text",)
    
    
print("translated text:", output)
