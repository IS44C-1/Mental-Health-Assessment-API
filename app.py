from flask import Flask
from routes import assessment_bp

app = Flask(__name__)

app.register_blueprint(assessment_bp)

@app.route("/health")
def app_health():
    return {"health": "OK"}

if __name__ == '__main__':
    app.run(debug=True)