import requests
import json

dataset_id = "4apg-4kt9"
base_url = "https://data.ny.gov/resource/"
api_url = f"{base_url}{dataset_id}.json"

try:
    response = requests.get(api_url)
    response.raise_for_status()  # Raise an exception for bad status codes

    data = response.json()
    # Now 'data' is a list of dictionaries, where each dictionary
    # represents a row in the dataset.
    print(json.dumps(data, indent=2)) # Pretty print the JSON output

    # You can now work with the 'data' list to analyze the metrics.
    # For example, to see the column names of the first row:
    if data:
        print("\nColumn Names:")
        print(data[0].keys())

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")