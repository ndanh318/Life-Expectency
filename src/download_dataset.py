import requests
import zipfile
from pathlib import Path
import os

url = "https://s.net.vn/hvt2"
def download_and_unzip(url):
    # setup data path
    path = Path("../data/")
    data_path = path / "sources"

    # checking directory
    if data_path.is_dir():
        print("{} directory is existed!".format(data_path))
    else:
        print("Can not find {} directory, create one...".format(data_path))
        data_path.mkdir(parents=True, exist_ok=True)

        # download data
        with open(path / "sources.zip", "wb") as f:
            request = requests.get(url)
            print("Download data...")
            f.write(request.content)

        # unzip data
        with zipfile.ZipFile(path / "sources.zip", "r") as zip_ref:
            print("Unzipping data...")
            zip_ref.extractall(data_path)

    return data_path

if __name__ == '__main__':
    download_and_unzip(url)