import json
from flask import Flask, request, jsonify  # flaskを使って実装

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # jsonの文字化け防止


@app.route("/NGword", methods=["GET"])
def NGword():
    url = request.json["url"]
    return jsonify("あいうえお")


if __name__ == "__main__":
    app.run(port=8080, debug=True)
