import pathlib
import random
import string

import requests


def image(url):
    image_name = judge_name()

    response = requests.get(url)
    image = response.content
    with open(image_name, "wb") as file:
        file.write(image)
    return image_name


def random_name():
    randlst = [random.choice(string.ascii_letters + string.digits) for i in range(10)]
    image_name = "".join(randlst) + ".png"
    return image_name


def judge_name():
    files = pathlib.Path("../catr/png/").glob("*.png")
    image_name = random_name()
    i = 1
    while i == 1:
        for file_name in files:
            if file_name.name == image_name:
                image_name = random_name()
                i = 1
                break
            else:
                i = 0

    image_name_dec = "./../catr/png/" + image_name
    return image_name_dec
