
import requests
import os

# Extracting data from GitHub
def extract_data(file_path, url="https://raw.githubusercontent.com/nogibjj/Eric_Ortega_Rodriguez_Mini_Project_11/main/data/avengers.csv"):
    if os.path.exists(file_path):
        print(f"Local file found: {file_path}")
        return file_path

    print("Local file not found. Falling back to URL...")
    
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Request data from URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f"File downloaded successfully: {file_path}")
        return file_path
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
        return None

# Example usage
file_path = "data/avengers.csv"
extract_data(file_path)
