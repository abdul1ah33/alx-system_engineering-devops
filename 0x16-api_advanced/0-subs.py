#!/usr/bin/python3
import requests
from time import sleep

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://www.reddit.com/"
    }

    for attempt in range(3):  # Retry up to 3 times
        try:
            print(f"Sending request to {url}")
            response = requests.get(url, headers=headers, allow_redirects=False, timeout=10)
            if response.status_code == 200:
                data = response.json().get("data")
                if data and "subscribers" in data:
                    return data["subscribers"]
                else:
                    print("No 'subscribers' field found in the response.")
                    return 0
            elif response.status_code == 403:
                print("Request was forbidden. You may be blocked or need to update your User-Agent.")
                return 0
            elif response.status_code == 404:
                print("Subreddit not found (404).")
                return 0
            else:
                print(f"Unexpected status code: {response.status_code}")
                return 0
        except requests.Timeout:
            print("Request timed out. Retrying...")
            sleep(5)  # Wait 5 seconds before retrying
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return 0

    print("Failed to retrieve data after multiple attempts.")
    return 0

