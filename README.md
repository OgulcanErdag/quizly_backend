# Quizly Backend

![Quizzy Logo](/logoheader.png)

AI-Powered Quiz Generator from YouTube Videos

Quizly is a full-stack web application that automatically transforms YouTube videos into interactive quizzes using AI.  
Users simply paste a video link, and Quizly handles everything from audio extraction and transcription to quiz generation and playback.

---

## 🚀 Features

- 🎥 **YouTube Video Processing**

  - Supports both `watch?v=` and `shorts/` URLs
  - Robust handling of YouTube format changes via `yt-dlp`

- 🧠 **AI-Generated Quizzes**

  - Automatic quiz generation based on video content
  - Exactly **10 multiple-choice questions**
  - One correct answer per question
  - Valid JSON output for safe parsing

- 🎧 **Audio Transcription**

  - Uses OpenAI Whisper for accurate speech-to-text
  - Optimized for CPU environments (FP32 fallback)

- 🖥️ **Interactive Frontend**

  - Quiz overview and history
  - Live quiz navigation (next / previous questions)
  - Score calculation and result screen

- 🔐 **Authentication**
  - JWT-based authentication
  - Protected quiz endpoints

---

## 🧱 Tech Stack

### Backend

- **Python**
- **Django & Django REST Framework**
- **JWT Authentication**
- **yt-dlp** (YouTube audio extraction)
- **Whisper** (speech-to-text)
- **Google Gemini API** (quiz generation)

### Frontend

- **Vanilla JavaScript**
- **HTML / CSS**
- Modular architecture (API, auth, quiz, overview, library)

---

## ⚙️ Environment Variables

Create a `.env` file in the backend root:

```bash
SECRET_KEY=your_django_secret_key
DEBUG=True

GEMINI_API_KEY=your_gemini_api_key

ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOW_CREDENTIALS=True
CORS_ALLOWED_ORIGINS=http://localhost:4200,http://127.0.0.1:5500
CSRF_TRUSTED_ORIGINS=http://localhost:4200,http://127.0.0.1:5500
```

## Running the Project Locally

### Backend

```bash
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend

Serve the frontend using any static server (e.g. Live Server, nginx, or python):

```bash
python -m http.server 5500
```

### 🧠 How It Works

User submits a YouTube URL

Audio is downloaded via yt-dlp

Audio is transcribed with Whisper

Transcript is sent to Gemini AI

AI returns structured quiz JSON

Quiz is stored and rendered instantly in the frontend

### ⚠️ Notes

YouTube formats can change frequently — keeping yt-dlp up to date is recommended

Shorts and standard YouTube URLs are handled automatically

Video embedding uses the official YouTube embed format

📌 Project Status
✔ Core functionality complete
✔ Frontend & backend fully integrated
✔ Ready for deployment

### 📄 License

This project is for educational and portfolio purposes.

---

### 👤 Author

Ogulcan Erdag  
Full-Stack & DevOps Engineer
