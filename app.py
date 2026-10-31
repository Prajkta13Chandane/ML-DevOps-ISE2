from flask import Flask, request, jsonify
from sklearn.linear_model import LogisticRegression
import numpy as np

app = Flask(__name__)

# Sample training dataset
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

# Train the ML model
model = LogisticRegression()
model.fit(X, y)


@app.route("/")
def home():
    return """
    <h1>Student Pass Prediction System</h1>
    <form action="/predict" method="get">
        <label>Enter study hours:</label>
        <input type="number" name="hours"
               min="0" max="24" step="0.5" required>
        <button type="submit">Predict</button>
    </form>
    <p><a href="/health">Check Application Health</a></p>
    """


@app.route("/predict")
def predict():
    hours = request.args.get("hours", type=float)

    if hours is None:
        return jsonify({"error": "Enter study hours"}), 400

    if not np.isfinite(hours) or not 0 <= hours <= 24:
        return jsonify({
            "error": "Hours must be between 0 and 24"
        }), 400

    prediction = int(model.predict([[hours]])[0])

    result = "Pass" if prediction == 1 else "Fail"

    return jsonify({
        "study_hours": hours,
        "prediction": result
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "Student Pass Prediction System"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)