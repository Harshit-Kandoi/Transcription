import os
import whisper
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

model = whisper.load_model("small")  # Load Whisper model once

def transcribe_file(file_path):
    """Transcribe the uploaded file and return the text."""
    try:
        print(f"Processing: {file_path}")
        result = model.transcribe(file_path)
        transcription = result['text'].strip()

        if not transcription:
            return "No transcription generated."

        output_file = os.path.join(OUTPUT_FOLDER, os.path.splitext(os.path.basename(file_path))[0] + ".txt")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(transcription)

        return transcription
    except Exception as e:
        return f"Error: {e}"

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    """Render the webpage and handle file uploads."""
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        
        file = request.files['file']
        if file.filename == '':
            return "No selected file"
        
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Transcribe the uploaded file
        transcription = transcribe_file(file_path)
        return render_template('index.html', transcription=transcription)

    return render_template('index.html', transcription="")

@app.route('/api/transcribe', methods=['POST'])
def transcribe_api():
    """API endpoint to transcribe uploaded media files."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    transcription = transcribe_file(file_path)
    return jsonify({'transcription': transcription})

if __name__ == '__main__':
    app.run(debug=True)
