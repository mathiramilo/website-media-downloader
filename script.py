import argparse
import concurrent.futures
import logging
import os
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from tenacity import retry, stop_after_attempt, wait_fixed
from tqdm import tqdm

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")


# Function to download a file
@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def download_file(url, folder, pbar):
    local_filename = os.path.join(folder, url.split("/")[-1])

    # Skip file if it already exists
    if os.path.exists(local_filename):
        logging.info(f"File {local_filename} already exists, skipping.")
        pbar.update(1)
        return local_filename

    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        logging.info(f"Downloaded {url} to {local_filename}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to download {url}: {e}")
    pbar.update(1)
    return local_filename


# Function to parse the HTML and download media
def download_media_from_website(base_url, folder="downloaded_media"):
    if not os.path.exists(folder):
        os.makedirs(folder)

    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, "html.parser")

    media_tags = soup.find_all(["img", "audio", "video", "a"])
    media_urls = []
    for tag in media_tags:
        url = tag.get("src") or tag.get("href")
        if url:
            full_url = urljoin(base_url, url)
            if any(
                full_url.endswith(ext)
                for ext in [
                    ".jpg",
                    ".jpeg",
                    ".png",
                    ".gif",
                    ".bmp",
                    ".svg",
                    ".mp4",
                    ".mp3",
                    ".wav",
                    ".pdf",
                    ".doc",
                    ".docx",
                    ".ppt",
                    ".pptx",
                    ".xls",
                    ".xlsx",
                ]
            ):
                media_urls.append(full_url)

    with tqdm(total=len(media_urls)) as pbar:
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = [
                executor.submit(download_file, url, folder, pbar) for url in media_urls
            ]
            concurrent.futures.wait(futures)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download all media items from a specified website"
    )
    parser.add_argument(
        "url", type=str, help="The URL of the website to download media from"
    )
    parser.add_argument("folder", type=str, help="The folder to save downloaded media")

    args = parser.parse_args()

    try:
        download_media_from_website(args.url, args.folder)
    except Exception as e:
        logging.critical(f"An error occurred: {e}")
