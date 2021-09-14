import sys

from flask import Flask, jsonify, request  # flaskを使って実装

sys.path.append("../")
import sys

from url_image.url_image import image

sys.path.append("../")
from catr import predict

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # jsonの文字化け防止


@app.route("/test")
def NGword():
    url = request.json["url"]
    image(url)
    return jsonify(predict.pre())


if __name__ == "__main__":
    app.run(port=5000, debug="True")
