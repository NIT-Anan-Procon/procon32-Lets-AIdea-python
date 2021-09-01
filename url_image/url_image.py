import requests


def image(url):
    # url = "https://news.walkerplus.com/article/148584/844539_615.jpg"
    file_name = "./png/sample.png"
    response = requests.get(url)
    image = response.content
    with open(file_name, "wb") as file:
        file.write(image)
