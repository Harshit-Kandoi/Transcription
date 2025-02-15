# **🎙️ Transcription Service**
A **speech-to-text** transcription tool using OpenAI's **Whisper** model.  

- **🌐 Web Interface** (`app.py`): Upload audio/video files and transcribe them via a **Flask-based web app**.  
- **💻 Local Transcription** (`transcript.py`): Run transcription on local files inside the `media` folder.  

---

## **🚀 Features**
✅ Supports **audio & video** formats (`.mp3`, `.wav`, `.mp4`, `.avi`, `.mkv`).  
✅ Uses **OpenAI Whisper** (`small` model) for high accuracy.  
✅ Web interface with **upload & progress tracking**.  
✅ Auto-saves transcriptions as `.txt` files.  

---

## **📌 Installation**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/Harshit-Kandoi/Transcription.git
cd Transcription
```

### **2️⃣ Set Up Virtual Environment (Optional)**
```sh
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

---

## **🌐 Running the Web App (Flask)**
1️⃣ Start the Flask app:
```sh
python app.py
```
2️⃣ Open your browser and go to:  
   **http://127.0.0.1:5000/**  
3️⃣ Upload an **audio/video file** and wait for the transcription to complete.  

---

## **💻 Running Local Transcription**
1️⃣ Place your **audio/video files** inside the `media/` folder.  
2️⃣ Run the script:
```sh
python transcript.py
```
3️⃣ Transcriptions will be saved in the `outputs/` folder as `.txt` files.

---

## **📂 Project Structure**
```
📁 Transcription/
│── 📁 media/          # Store input audio/video files (for local transcription)
│── 📁 outputs/        # Stores transcribed text files
│── 📁 static/         # Static assets (icons, CSS, etc.)
│── 📁 templates/      # HTML templates for the web app
│── 📁 uploads/        # Uploaded files via Flask app
│── 📜 app.py          # Flask web app for transcription
│── 📜 transcript.py   # Local transcription script
│── 📜 requirements.txt # Required Python dependencies
│── 📜 .gitignore      # Ignoring unnecessary files
│── 📜 README.md       # Project documentation
```

---

## **🛠️ Technologies Used**
- **Python**  
- **Flask** (for the web interface)  
- **Whisper AI** (for speech-to-text transcription)  
- **JavaScript + HTML + CSS** (for frontend UI)  

---

## **📝 License**
This project is **open-source** under the **MIT License**.  

🚀 **Enjoy transcribing!** Let me know if you need any modifications. 😊
