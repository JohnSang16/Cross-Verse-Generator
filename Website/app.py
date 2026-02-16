import random
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Predefined Bible verses for specific situations/moods
mood_verses = {
    "depression": [
        "Psalm 34:18 - The Lord is close to the brokenhearted and saves those who are crushed in spirit.",
        "Isaiah 41:10 - Do not fear, for I am with you; do not be dismayed, for I am your God.",
        "Matthew 11:28 - Come to me, all you who are weary and burdened, and I will give you rest."
    ],
    "poverty": [
        "Matthew 6:26 - Look at the birds of the air; they do not sow or reap or store away in barns, and yet your heavenly Father feeds them.",
        "Philippians 4:19 - And my God will meet all your needs according to the riches of his glory in Christ Jesus.",
        "2 Corinthians 9:8 - And God is able to bless you abundantly, so that in all things at all times, having all that you need, you will abound in every good work."
    ],
    "fear": [
        "2 Timothy 1:7 - For God gave us a spirit not of fear but of power and love and self-control.",
        "Psalm 23:4 - Even though I walk through the darkest valley, I will fear no evil, for you are with me.",
        "Isaiah 41:10 - So do not fear, for I am with you; do not be dismayed, for I am your God."
    ],
    "joy": [
        "Nehemiah 8:10 - Do not grieve, for the joy of the Lord is your strength.",
        "Psalm 16:11 - You make known to me the path of life; you will fill me with joy in your presence.",
        "Romans 15:13 - May the God of hope fill you with all joy and peace as you trust in him."
    ],
    "loneliness":[
        "Matthew 28:20: And surely I am with you always, to the very end of the age.", 
        "Psalm 23:4: Even though I walk through the darkest valley, I will fear no evil, for you are with me; your rod and your staff, they comfort me.", 
        "Isaiah 41:10: So do not fear, for I am with you; do not be dismayed, for I am your God. I will strengthen you and help you; I will uphold you with my righteous right hand.",
          ],
    'tiredness': [
        "Matthew 11:28-29 Come to me, all you who are weary and burdened, and I will give you rest.Take my yoke upon you and learn from me, for I am gentle and humble in heart, and you will find rest for your souls.",
        "Psalm 62:1  “Truly my soul finds rest in God; my salvation comes from him.",
        "Jeremiah 31:25  “I will refresh the weary and satisfy the faint.",
        "Psalm 46:1  “God is our refuge and strength,  an ever-present help in trouble."
    ]
}

# Mapping similar moods to a common group
mood_aliases = {
    "anxious":"fear",
    "anxiety": "fear",
    "fear": "fear",
    "nervous": "fear",
    "worry": "fear",
    "stress": "fear",
    "happiness":"joy",
    "happy": "joy",
    "alone" : "loneliness",
    "poor" : "poverty",
    "sad" : "depression",
    "down" : "depression",
    "blue" : "depression",
    "sadness" : "depression",  
    "depressed" : "depression",
    "tired": "tiredness",
    "weary": "tiredness",
    "exhausted" : "tiredness"

}

# List of random Bible verses (for when there is no specific mood)
random_bible_verses = [
    "John 3:16 - For God so loved the world...",
    "Philippians 4:13 - I can do all things through Christ...",
    "Romans 8:28 - And we know that in all things God works for the good..."
]

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/get-random-verse')
def get_random_verse():
    return jsonify({"verse": random.choice(random_bible_verses)})

@app.route('/get-verse-for-situation')
def get_verse_for_situation():
    # Get the 'season' parameter from the query string (user's input)
    mood = request.args.get('mood', '').lower()

    # Check if the input matches any mood alias
    mapped_season = mood_aliases.get(mood, mood)  # If it's in aliases, use the mapped one

    # Find the corresponding list of verses
    verses = mood_verses.get(mapped_season)
    
    if verses:
        # Randomly select a verse from the corresponding list
        return jsonify({"verse": random.choice(verses)})  # Return a random verse for the given mood
    else:
        return jsonify({"verse": "Sorry, I couldn't find a verse for that. Try a different emotion or situation."})  # Error message for invalid input

if __name__ == '__main__':
    app.run(debug=True)
