from flask import Flask, request, jsonify, render_template
from executor import run_code

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
def run():
    data = request.json
    code = data.get("code", "")
    language = data.get("language", "python")
    print("LANGUAGE:", language)
    output = run_code(code, language)

    return jsonify({"output": output})

if __name__ == "__main__":
    app.run(debug=True)
