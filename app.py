from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/increment", methods=["POST"])
def plusone():
    req = request.form
    res = {"count": int(req["count"])+1}
    return jsonify(res)
    
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080, debug = True)