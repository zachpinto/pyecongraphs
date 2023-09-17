import requests
import os


# Base directory where you want to start saving the files
BASE_PATH = "/Users/pintoza/Desktop/dev/pyecongraphs/data/external/"

# Read URLs from the urls.txt file
with open("yml_links.txt", "r") as file:
    urls = [line.strip() for line in file if line.strip()]


# Function to download and save content from a URL
# Function to download and save content from a URL
def download_and_save(url, base_path):
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Extracting the directory structure from the URL
        sections = url.split("/topics/")[-1].split("/")
        category, subcategory, filename = sections[0], sections[1], sections[-1]

        # Creating the full save path
        save_path = os.path.join(base_path, category, subcategory)

        # Ensure the directory exists
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # Saving the content
        with open(os.path.join(save_path, filename), 'w') as file:
            file.write(response.text)
        print(f"Downloaded {filename} to {save_path}")
    except requests.HTTPError as e:
        print(f"Error downloading {url}: {e}")
    except Exception as e:
        print(f"Unexpected error downloading {url}: {e}")


# Download and save each file
for url in urls:
    download_and_save(url, BASE_PATH)

print("All files downloaded!")
