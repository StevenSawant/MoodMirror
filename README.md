# MoodMirror 🎭🪞

A Flask-based web app that helps users log their daily moods, write short notes, and receive personalized motivational quotes and YouTube playlists — all powered by MongoDB and the YouTube Data API.

---

## ✨ Features

- 📝 Log your daily mood (Happy, Sad, Anxious, Excited, etc.)
- 🗒️ Add an optional journal entry
- 💬 Get a motivational quote based on your mood
- 🎵 View a YouTube playlist suggestion dynamically fetched using the YouTube Data API
- 📊 See your past mood logs in a timeline
- ⚡ AJAX-based form submission for smooth user experience
- 🔐 API keys secured using `.env` and `python-dotenv`

---

## 🔧 Tech Stack

| Layer        | Tool / Framework             |
|-------------|-------------------------------|
| Frontend     | HTML, CSS, JavaScript (jQuery) |
| Backend      | Flask                         |
| Database     | MongoDB (via Flask-PyMongo)   |
| API          | YouTube Data API v3           |
| Environment  | `python-dotenv`, `requests`   |

---

## 🚀 Getting Started

### 🔨 Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/MoodMirror.git
   cd MoodMirror
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # or venv/bin/activate on macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the project root:
   ```
   MONGO_URI=mongodb://localhost:27017/moodmirror
   SECRET_KEY=your_flask_secret_key
   YOUTUBE_API_KEY=your_youtube_api_key
   ```

5. **Run the app**
   ```bash
   python app.py
   ```

6. **Open in browser**
   [http://localhost:5000]

---

## 📁 Project Structure

```
MoodMirror/
│
├── app.py                  # Main Flask app
├── config.py               # Config and env loader
├── requirements.txt        # Python dependencies
├── .env                    # API keys and secrets (not pushed)
│
├── templates/              # HTML templates
│   ├── base.html
│   ├── index.html
│   └── history.html
│
├── static/                 # CSS & static files
│   └── styles.css
```

---

## 🛡️ Security Notes

- Make sure `.env` is listed in your `.gitignore`.
- Never push API keys or secrets to public repositories.

---

## 💡 Future Enhancements

- Mood analytics graph with Chart.js 📊
- User authentication & login system 🔐
- Dark/light theme toggle 🌙☀️

---

## 👨‍💻 Author

**Steven Datta Sawant**  
2026 B.Tech. Student — MoodMirror Project  
Open for feedback & collaboration on GitHub!

---
