from flask import Flask, request, jsonify  # flaskを使って実装

import sys
sys.path.append('../')
from url_image.url_image import image

# import sys
# sys.path.append('../')
from catr import predict

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # jsonの文字化け防止


@app.route("/")
def NGword():
    url = request.json["url"]
    image(url)
    return jsonify(predict.pre())


if __name__ == "__main__":
    app.run(port=5000, debug="True")
