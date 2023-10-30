import requests
import multiprocessing
import argparse


def download_image(url: str)->None:
    response = requests.get(url)
    name = url.split("/")[-1]
    with open(name, "wb") as f:
        f.write(response.content)
    print(f"Image {name} downloaded successfully")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("urls", nargs="+", help="List of image URLs")
    args = parser.parse_args()

    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    pool.map(download_image, args.urls)

    pool.close()
    pool.join()