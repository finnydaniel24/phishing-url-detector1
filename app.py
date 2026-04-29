from flask import Flask, render_template, request
import pickle
from feature_extraction import extract_features

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""

    if request.method == "POST":
        url = request.form["url"]

        features = extract_features(url)
        prediction = model.predict([features])[0]

        if prediction == 0:
            result = "Safe"
        else:
            result = "Malicious"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
