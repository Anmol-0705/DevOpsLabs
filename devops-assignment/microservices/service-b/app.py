from flask import Flask
app = Flask(__name__)

@app.route("/service-b")
def service_b():
    return "Service B Response"

app.run(host="0.0.0.0", port=5002)
