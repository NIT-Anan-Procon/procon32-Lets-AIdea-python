import glob
import random
import string

import requests


def image(url):
    image_name = random_name()

    response = requests.get(url)
    image = response.content
    with open(image_name, "wb") as file:
        file.write(image)
    return image_name


def random_name():
    randlst = [random.choice(string.ascii_letters + string.digits) for i in range(10)]
    image_name = "./../catr/png/"
    image_name += "".join(randlst) + ".png"
    return judge_name(image_name)


def judge_name(image_name):
    files = glob.glob("./../catr/png/*")
    for file_name in files:
        if file_name == image_name:
            random_name()
            break
        else:
            return image_name
