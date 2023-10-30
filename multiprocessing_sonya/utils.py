import requests
import multiprocessing
import argparse


def download_image(url: str)->None:
    response = requests.get(url)
    name = url.split("/")[-1]
    with open(name, "wb") as f:
        f.write(response.content)
    print(f"Image {name} downloaded successfully")


def main(urls: list) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("urls", nargs="+", help="List of image URLs")
    args = parser.parse_args()

    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    pool.map(download_image, args.urls)

    pool.close()
    pool.join()
    #python main.py https://kartinki.pics/pics/uploads/posts/2022-07/thumbs/1658296079_68-kartinkin-net-p-adskaya-gonchaya-grimm-art-oboi-73.jpg https://chakiris.club/uploads/posts/2022-11/1668605594_chakiris-club-p-adskaya-gonchaya-dnd-oboi-10.png https://kartinki.pics/pics/uploads/posts/2022-07/1658295978_8-kartinkin-net-p-adskaya-gonchaya-grimm-art-oboi-9.jpg https://kartinkin.net/pics/uploads/posts/2022-07/1658296325_62-kartinkin-net-p-adskaya-gonchaya-sverkhestestvennoe-art-ob-65.jpg https://krasivosti.pro/uploads/posts/2023-07/1688424066_krasivosti-pro-p-koshki-raznikh-tsvetov-oboi-54.jpg https://u.9111s.ru/uploads/202205/27/f2cd4d70a1ff2a2655a42dd69f56235b.jpg