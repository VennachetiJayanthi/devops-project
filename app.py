import random
from flask import Flask, render_template
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/dashboard")
def dashboard():
    fake_pods = ["pod-1", "pod-2", "pod-3"]
    hostname = random.choice(fake_pods)

    cpu = random.randint(10, 90)
    requests = random.randint(100, 1000)

    return render_template("dashboard.html",
                           hostname=hostname,
                           cpu=cpu,
                           requests=requests)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)