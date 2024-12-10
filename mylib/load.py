import requests
import os

def extract_data(file_path, url="https://raw.githubusercontent.com/nogibjj/Eric_Ortega_Rodriguez_Mini_Project_11/main/data/avengers.csv"):
    """
    Download the data file from the specified URL if it does not exist locally.

    Args:
        file_path (str): Path to save the file locally.
        url (str): URL of the data file to download.

    Returns:
        str: Path to the local file if successful, None otherwise.
    """
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

if __name__ == "__main__":
    # Define the file path and the URL
    file_path = "data/avengers.csv"
    extract_data(file_path)
