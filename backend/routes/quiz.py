from flask import Blueprint, jsonify, request
from bson.errors import InvalidId

from services.quiz_service import (
    get_all_quizzes,
    get_quiz_by_id,
    submit_quiz
)

quiz_bp = Blueprint("quiz", __name__)


@quiz_bp.route("/quizzes", methods=["GET"])
def get_quizzes():

    quizzes = get_all_quizzes()

    return jsonify(quizzes)


@quiz_bp.route("/quiz/<quiz_id>", methods=["GET"])
def get_quiz(quiz_id):

    try:

        quiz = get_quiz_by_id(quiz_id)

        if not quiz:
            return jsonify({"error": "Quiz not found"}), 404

        return jsonify(quiz)

    except InvalidId:

        return jsonify({"error": "Invalid Quiz ID"}), 400
    
@quiz_bp.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    
    quiz_id = data.get("quiz_id")

    answers = data.get("answers")

    result = submit_quiz(quiz_id, answers)

    if result is None:
        return jsonify({"error": "Quiz not found"}), 404

    return jsonify(result) 