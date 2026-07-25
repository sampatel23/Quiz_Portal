from flask import Blueprint, jsonify
from database.mongodb import question_collection
from bson import ObjectId
from bson.errors import InvalidId

quiz_bp = Blueprint("quiz", __name__)


@quiz_bp.route("/quizzes", methods=["GET"])
def get_quizzes():

    quizzes = []

    for quiz in question_collection.find():

        quizzes.append({
            "id": str(quiz["_id"]),
            "title": quiz["title"],
            "difficulty": quiz["difficulty"],
            "duration": quiz["duration"]
        })

    return jsonify(quizzes)


@quiz_bp.route("/quiz/<quiz_id>", methods=["GET"])
def get_quiz(quiz_id):

    try:
        quiz = question_collection.find_one(
            {"_id": ObjectId(quiz_id)}
        )

        if not quiz:
            return jsonify({"error": "Quiz not found"}), 404

        quiz["_id"] = str(quiz["_id"])

        return jsonify(quiz)

    except InvalidId:
        return jsonify({"error": "Invalid Quiz ID"}), 400