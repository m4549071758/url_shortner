from flask import Flask, render_template, redirect, jsonify, request
from models.models import Urls, db_session
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(24)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def shorten():
    data = request.json

    url = data.url

    token = secrets.token_urlsafe(3)
    new_url = Urls(url, token)

    db_session.add(new_url)
    db_session.commit()

    response = {
        "url": f"https://YOUR_SERVER_DOMAIN/{token}",
        "message": "URL HAS SHORTENED!"
    }
    return jsonify(response)

@app.route("/<token>", methods=["GET"])
def shorten_redirect(token):
    url = Urls.query.filter_by(token=token).first()
    if url:
        return redirect(url)
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)