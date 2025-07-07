# Flask AI app for prediction
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = "Team A wins" if data.get('goalsA', 0) > data.get('goalsB', 0) else "Draw"
    return jsonify({'prediction': prediction, 'confidence': '88%'})

if __name__ == '__main__':
    app.run(port=5000)
