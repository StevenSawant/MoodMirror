from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
from config import MONGO_URI, SECRET_KEY
from datetime import datetime
import random
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['MONGO_URI'] = MONGO_URI
app.config['SECRET_KEY'] = SECRET_KEY
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY') # api key
mongo = PyMongo(app)

quotes_by_mood = {
    'Happy': ["Keep spreading happiness!", "Smile, it's contagious!"],
    'Sad': ["This too shall pass.", "Courage doesn't always roar."],
    'Anxious': ["Breathe. You're doing great.", "One step at a time."],
    'Excited': ["Embrace the thrill!", "Ride the wave of energy!"]
}

# playlists_by_mood = {
#     'Happy': 'https://www.youtube.com/watch?v=ZbZSe6N_BXs',
#     'Sad': 'https://www.youtube.com/watch?v=ho9rZjlsyYY',
#     'Anxious': 'https://www.youtube.com/watch?v=2OEL4P1Rz04',
#     'Excited': 'https://www.youtube.com/watch?v=QJO3ROT-A4E'
# }

def get_youtube_playlist_url(mood):
    search_query = f"{mood} mood music playlist"
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q={search_query}&key={YOUTUBE_API_KEY}&type=playlist"
    
    response = requests.get(url)
    data = response.json()
    
    if 'items' in data and len(data['items']) > 0:
        playlist_id = data['items'][0]['id']['playlistId']
        return f"https://www.youtube.com/playlist?list={playlist_id}"
    
    return "https://www.youtube.com"



@app.route('/')
def home():
    logs = mongo.db.moods.find().sort('date', -1)
    return render_template('index.html', logs=logs)

@app.route('/log', methods=['POST'])
def log_mood():
    data = request.json
    mood = data.get('mood')
    note = data.get('note')
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    mongo.db.moods.insert_one({'mood': mood, 'note': note, 'date': date})

    quote = random.choice(quotes_by_mood.get(mood, ["You're doing great!"]))
    playlist = get_youtube_playlist_url(mood)
    
    return jsonify({'quote': quote, 'playlist': playlist})

if __name__ == '__main__':
    app.run(debug=True)