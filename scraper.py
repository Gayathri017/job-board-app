import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

def fetch_linkedin_jobs():
    # Prepare the Actor input based on your requirements
    run_input = {
        "searchTerms": ["Software Engineer", "Backend Developer", ".NET Developer", "C# Developer"],
        "location": "Germany", # We can loop through [Germany, Netherlands, Luxembourg] later
        "publishedAt": "24h",
        "maxPages": 1, 
        "limit": 50,
        "proxy": { "useApifyProxy": True }
    }

    print("🚀 Starting LinkedIn Scraper (this may take a minute)...")
    
    # Run the Actor and wait for it to finish
    run = client.actor("apify/linkedin-jobs-scraper").call(run_input=run_input)

    # Fetch results from the run's dataset
    print(f"✅ Scrape finished! Fetching results from dataset...")
    dataset_items = client.dataset(run["defaultDatasetId"]).list_items().items
    
    return dataset_items

if __name__ == "__main__":
    jobs = fetch_linkedin_jobs()
    print(f"Found {len(jobs)} jobs!")
    if jobs:
        print(f"Sample Job: {jobs[0].get('title')} at {jobs[0].get('companyName')}")