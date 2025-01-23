from flask import Flask, render_template, jsonify
import threading

app = Flask(__name__)

# Variable to track request count
request_count = 0
lock = threading.Lock()

@app.route("/")
def home():
    global request_count
    with lock:
        request_count += 1
    return "Welcome to the test server!"

@app.route("/monitor")
def monitor():
    return render_template("monitor.html")

@app.route("/get_count")
def get_count():
    global request_count
    with lock:
        return jsonify({"count": request_count})

if __name__ == "__main__":
    app.run(debug=True)
