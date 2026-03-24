import os
import re
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

def parse_experience(text):
    if not text: return "Not specified"
    
    # 1. Look for numbers (3+ years, 5 yrs, etc.)
    match = re.search(r'(\d+)\+?\s*(?:year|yr)s?', text, re.IGNORECASE)
    if match:
        return f"{match.group(1)}+ Years"
    
    # 2. Look for Seniority keywords if no number is found
    text_lower = text.lower()
    if any(word in text_lower for word in ['senior', 'sr.', 'lead', 'principal']):
        return "Senior Level"
    if any(word in text_lower for word in ['junior', 'jr.', 'entry', 'graduate']):
        return "Junior/Entry"
    if 'intern' in text_lower:
        return "Internship"
        
    return "Mid-Level / Not Specified"

def fetch_all_jobs():
    countries = ["Germany", "Netherlands", "Luxembourg"]
    titles = ["Software Engineer", ".NET Developer", "C# Developer"]
    
    # Create a single massive Google query
    # Example: (site:linkedin.com/jobs) "Software Engineer" (Germany OR Netherlands)
    query = f'site:linkedin.com/jobs (".NET" OR "C#" OR "Software Engineer") ("Germany" OR "Netherlands" OR "Luxembourg") after:2026-03-23'
    
    run_input = {
        "queries": query,
        "maxPagesPerQuery": 1,
        "resultsPerPage": 40,
    }

    print(f"🚀 Scraping jobs for {countries}...")
    
    try:
        run = client.actor("apify/google-search-scraper").call(run_input=run_input)
        raw_results = client.dataset(run["defaultDatasetId"]).list_items().items[0].get('organicResults', [])
        
        cleaned_jobs = []
        for item in raw_results:
            description = item.get('description', '')
            
            job_data = {
                "title": item.get('title').split('|')[0].strip(), # Clean up the title
                "link": item.get('url'),
                "snippet": description,
                "experience": parse_experience(description)
            }
            cleaned_jobs.append(job_data)
            
        return cleaned_jobs
    except Exception as e:
        print(f"❌ Error: {e}")
        return []

if __name__ == "__main__":
    all_jobs = fetch_all_jobs()
    print(f"\n--- CLEANED RESULTS ({len(all_jobs)}) ---")
    for job in all_jobs[:10]:
        print(f"Title: {job['title']}")
        print(f"Exp:   {job['experience']}")
        print(f"URL:   {job['link']}\n")

    import json
    if not os.path.exists('data'):
        os.makedirs('data')
        
    with open('data/jobs.json', 'w', encoding='utf-8') as f:
        json.dump(all_jobs, f, indent=4, ensure_ascii=False)
        
    print("✅ Saved results to data/jobs.json")