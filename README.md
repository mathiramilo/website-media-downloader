# Website Media Downloader

## Description

Python script designed to download all media files from a specified website. The script supports concurrent downloads, shows a progress bar, and accepts command-line arguments to specify the target website and output folder. It handles various file types including images, videos, audio files, PDFs, and common office documents.

## Live Demo

## Features

- **Concurrent Downloads**: Utilizes Python's `concurrent.futures` to download multiple files simultaneously, improving efficiency and speed.
- **Progress Bar**: Displays a progress bar using `tqdm` to show the status of ongoing downloads.
- **Retry Mechanism**: Implements a retry mechanism using `tenacity` to handle temporary failures during file downloads.
- **Command-Line Arguments**: Accepts arguments to specify the target website URL and the folder where the downloaded files will be saved.

## Installation

1. **Clone the Repository** (if applicable):

```sh
git clone https://github.com/yourusername/media_scraper.git
cd media_scraper
```

2. **Install Required Libraries:**

Ensure you have the necessary Python libraries installed. You can install them using pip:

```sh
pip install -r requirements.txt
```

## Usage

To run the script, use the following command:

```sh
python script.py <url> <output>
```

- `<url>`: The URL of the website to download media files from.
- `<output>`: The folder where the downloaded files will be saved.

For example:

```sh
python script.py https://example.com website_media
```

## Adding the Script to Your PATH

### For Unix-based Systems (Linux/macOS)

1. Add Shebang (at the top of the script):

   ```python
   #!/usr/bin/env python
   ```

2. Make the Script Executable:

   ```sh
   chmod +x script.py
   ```

3. Move the Script to a Directory in Your PATH:

   ```sh
   sudo mv script.py /usr/local/bin/webmd
   ```

Now you can run the script from anywhere using:

```sh
webmd <url> <output>
```

### For Windows

1. Create a Batch File:

Create a file named webmd.bat with the following content:

```batch
@echo off
python "C:\path\to\script.py" %*
```

2. Add the Directory Containing the Batch File to Your PATH:

   - Open the Start menu and search for "Environment Variables."
   - Edit the Path variable and add the directory where the .bat file is located.

Now you can run the script from anywhere using:

```sh
webmd <url> <output>
```
