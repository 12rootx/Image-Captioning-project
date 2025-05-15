import gdown
import zipfile
import os

# URLs and output paths
files = {
    "Flickr8k_Dataset.zip": "https://drive.google.com/uc?id=1hG7oCfO7lOajOUmThTHry5COVqwxbKHU",
    "Flickr8k_text.zip": "https://drive.google.com/uc?id=1WTjo_InLaB23RUzIpPKrsm4ZxrEjbpQZ"
}

os.makedirs("data", exist_ok=True)

for filename, url in files.items():
    output = f"data/{filename}"
    print(f"Downloading {filename}...")
    gdown.download(url, output, quiet=False)

    print(f"Unzipping {filename}...")
    with zipfile.ZipFile(output, 'r') as zip_ref:
        zip_ref.extractall("data/")

