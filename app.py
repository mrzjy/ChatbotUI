from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    query = request.args.get('msg')
    response = "this is an answer"
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=54321)