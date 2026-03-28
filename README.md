🚀 AI-Powered LinkedIn Job Tracker
A dynamic web application that scrapes the latest Software Engineering, .NET, and C# job openings across Germany, Netherlands, and Luxembourg using Google Search automation and the Apify API.

✨ Features
Smart Scraping: Bypasses LinkedIn's anti-scraping walls by utilizing the apify/google-search-scraper.

Experience Detection: Uses Regex logic to identify seniority levels (Junior, Mid, Senior) from job snippets.

One-Click Refresh: A built-in "Refresh" button triggers a live cloud scrape and updates the local database.

Clean UI: Responsive dashboard built with Bootstrap 5.

🛠️ Tech Stack
Backend: Python / Flask

Scraping Engine: Apify SDK (Google Search Actor)

Frontend: HTML5, CSS3 (Bootstrap 5), JavaScript

Data Storage: JSON (File-based database)

🚀 Getting Started
1. Prerequisites
Python 3.x installed.

An Apify Account and API Token.

2. Installation
Bash
git clone https://github.com/Gayathri017/job-board-app.git
cd job-board-app
python -m venv venv
# Activate venv (Windows):
.\venv\Scripts\Activate
# Install dependencies:
pip install flask apify-client python-dotenv

3. Environment Variables
Create a .env file in the root directory:

Code snippet
APIFY_API_TOKEN=your_actual_token_here

4. Running the App
Bash
python app.py
Visit http://127.0.0.1:5000 in your browser.

Screenshot
<img width="1919" height="944" alt="Screenshot 2026-03-28 092641" src="https://github.com/user-attachments/assets/74e56c51-d5be-4581-b8ae-472469093dab" />


📁 Project Structure
app.py: The Flask server and web routes.

scraper.py: Logic for connecting to Apify and parsing job data.

templates/: HTML files for the frontend dashboard.

data/: Stores the jobs.json file.
