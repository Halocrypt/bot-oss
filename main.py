import threading
from bot import init
from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/<data>")
def hello(data=None):
    return f"Provided data: {data}" if data else "Hello world"


run = lambda: app.run(host="0.0.0.0", port=8080)

threading.Thread(target=run, daemon=True).start()
init()
