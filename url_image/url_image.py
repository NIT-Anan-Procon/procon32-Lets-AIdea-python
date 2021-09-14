import requests


def image(url):
    file_name = "./../catr/png/image.png"
    response = requests.get(url)
    image = response.content
    with open(file_name, "wb") as file:
        file.write(image)
