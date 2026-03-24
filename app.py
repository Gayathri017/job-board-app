import json
import os
from flask import Flask, render_template

app = Flask(__name__)

# Helper function to load the scraped data
def load_jobs():
    file_path = os.path.join('data', 'jobs.json')
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    jobs = load_jobs()
    return render_template('index.html', jobs=jobs)

if __name__ == '__main__':
    # Running on 0.0.0.0 so you can see it on your phone later!
    app.run(debug=True, host='0.0.0.0', port=5000)