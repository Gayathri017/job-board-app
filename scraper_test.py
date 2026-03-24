import os
from dotenv import load_dotenv
from apify_client import ApifyClient

# 1. Load your API token from the .env file
load_dotenv()
token = os.getenv("APIFY_API_TOKEN")

if not token:
    print("❌ Error: APIFY_API_TOKEN not found in .env file!")
else:
    client = ApifyClient(token)

    def test_connection():
        try:
            # Try to list your actors to verify the token is valid
            actors = client.actors().list()
            print("✅ Connection Successful!")
            print(f"Verified token for account. You have access to {actors.total} actors.")
        except Exception as e:
            print(f"❌ Connection Failed: {e}")

    if __name__ == "__main__":
        test_connection()