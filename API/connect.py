import json
from flask import Flask, request, jsonify  # flaskを使って実装

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # jsonの文字化け防止


@app.route("/~kurabuchi/procon32_Lets_AIdea_python/API/connect.py")
def NGword():
    url = request.json["url"]
    sample = {
        'url':url,
        'word':'あいうえお'
    }
    return jsonify(sample)


if __name__ == "__main__":
    app.run(port=5000, debug="True")
