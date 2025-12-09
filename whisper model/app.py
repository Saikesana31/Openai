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
# whatever the user upload the file , it will be saved in this folder
app.config['UPLOAD_FOLDER'] = 'save_audio'


@app.route('/',methods = ['GET','POST'])
def main():
    if request.method == 'POST':
        language = request.form.get('language') # To get the language from the user
        audio_file = request.files['file']      # To get the audio file from the user 
        # To save the audio file in the UPLOAD_FOLDER
        audio_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_file.filename)
        audio_file.save(audio_path)
        
         # TO open audio file
        with open(audio_path, "rb") as audio:
            # Translate audio using OpenAI Whisper
            transricpt = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio,
                response_format="text",
            )
        # If the user has selected a language, translate the transricpt to that language
            response = client.chat.completions.create(
                model="gpt-4-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that translates text."},
                    {"role": "user", "content": f"Translate the following text to {language}: {transricpt}"}],
                    temperature=0.7,
                    max_tokens=256
                )
        
            return jsonify({"translated_text": response.choices[0].message.content})

    return render_template('index.html')  


# to run th application
if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=8080)
    
   