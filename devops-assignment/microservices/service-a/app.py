from flask import Flask
app = Flask(__name__)

@app.route("/service-a")
def service_a():
    return "Service A Response"

app.run(host="0.0.0.0", port=5001)
