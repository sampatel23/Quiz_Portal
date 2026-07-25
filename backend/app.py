from flask import Flask

from routes.quiz import quiz_bp

app = Flask(__name__)

app.register_blueprint(quiz_bp)

@app.route("/")
def home():
    return "Quiz Portal Backend Running 🚀"

if __name__ == "__main__":
    app.run(debug=True)