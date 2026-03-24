import json
import os
from flask import Flask, render_template, redirect, url_for, flash
# Importing the function we built in scraper.py
from scraper import fetch_all_jobs

app = Flask(__name__)
app.secret_key = 'supersecretjobkey' # Needed for flashing messages

DATA_FILE = os.path.join('data', 'jobs.json')

def load_jobs():
    """Reads the local JSON database."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

@app.route('/')
def index():
    """Main dashboard view."""
    jobs = load_jobs()
    return render_template('index.html', jobs=jobs)

@app.route('/scrape')
def scrape():
    """Triggers the Apify scraper and updates the JSON file."""
    print("🚀 Scrape triggered from web UI...")
    
    # 1. Run the scraper function from scraper.py
    new_jobs = fetch_all_jobs()
    
    # 2. Ensure data directory exists
    if not os.path.exists('data'):
        os.makedirs('data')
        
    # 3. Save the fresh results
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(new_jobs, f, indent=4, ensure_ascii=False)
        
    print(f"✅ Successfully updated {len(new_jobs)} jobs.")
    return redirect(url_for('index'))

if __name__ == '__main__':
    # host='0.0.0.0' allows access from other devices on your Wi-Fi
    app.run(debug=True, host='0.0.0.0', port=5000)