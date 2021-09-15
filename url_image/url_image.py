import random
import string

import requests


def image(url):
    randlst = [random.choice(string.ascii_letters + string.digits) for i in range(10)]
    image_name = "./../catr/png/"
    image_name += "".join(randlst) + ".png"
    response = requests.get(url)
    image = response.content
    with open(image_name, "wb") as file:
        file.write(image)
    return image_name
