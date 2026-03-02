from Flask import Flask, jsonify

app = Flask(__name__) #name of the flask app is app

@app.route('/analyze-speech', methods=['POST']) #endpoint for checking the speech recording
def analyze_speech():
  return jsonify({
    "status": "success",
    "analysis_type": "speech",
    "risk_score": "0.45",
    "details": {"jitter": 0.02, "shimmer": 0.03}
  })

@app.route('/analyze-movement', methods=['POST'])
def analyze_movement(): #endpoint for looking at the video recording
    return jsonify({
        "status": "success",
        "analysis_type": "movement",
        "risk_score": 0.32,
        "details": {"tremor_amplitude": 0.15}
    })

@app.route('/analyze-imaging', methods=['POST'])
def analyze_imaging(): #endpoint for looking at scans
    return jsonify({
        "status": "success",
        "analysis_type": "imaging",
        "risk_score": 0.12,
        "details": {"atrophy_index": 0.05}
    })

if __name__ == '__main__': #start server
    app.run(debug=True, port=5000)
