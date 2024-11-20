import requests
import time
from datetime import datetime

# Function to monitor the API health
def check_api_health(api_url, max_response_time=2):
    try:
        response = requests.get(api_url)
        response_time = response.elapsed.total_seconds()
        
        # Print basic information
        print(f"Checked {api_url}: Status Code {response.status_code}, Response Time: {response_time}s")
        
        # Print additional health information
        print("Time of Response:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("Request Method:", response.request.method)
        print("Response Headers:", response.headers)
        content_length = response.headers.get('Content-Length', 'N/A')
        print(f"Content Length: {content_length}")
        
        # Check for API health
        if response.status_code != 200:
            print(f"API at {api_url} is down!")
        elif response_time > max_response_time:
            print(f"API at {api_url} is slow!")
        else:
            print(f"API at {api_url} is healthy and performing well.")
        
        
    except requests.exceptions.RequestException as e:
        print(f"Error checking {api_url}: {e}")

# Function to monitor multiple APIs
def monitor_apis(api_urls, interval=60):
    while True:
        for api_url in api_urls:
            check_api_health(api_url)
        time.sleep(interval)

# List of APIs to monitor
api_urls = ["https://github.com/anayakgit"]

# Start monitoring
monitor_apis(api_urls, interval=60)  # Check every 60 seconds
