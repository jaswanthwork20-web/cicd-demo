from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/hello")
def hello():
    return jsonify({
        "message": "Hello Manjula Menon, How are you doing?Im doing good Jaswanth",
        "status": "success"
    })


@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)