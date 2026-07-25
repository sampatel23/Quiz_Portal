from database.mongodb import question_collection
from bson import ObjectId


def get_all_quizzes():

    quizzes = []

    for quiz in question_collection.find():

        quizzes.append({
            "id": str(quiz["_id"]),
            "title": quiz["title"],
            "difficulty": quiz["difficulty"],
            "duration": quiz["duration"]
        })

    return quizzes


def get_quiz_by_id(quiz_id):

    quiz = question_collection.find_one(
        {"_id": ObjectId(quiz_id)}
    )

    if quiz:

        quiz["_id"] = str(quiz["_id"])

        # Remove answers before sending to frontend
        for question in quiz["questions"]:
            question.pop("answer", None)

    return quiz

def submit_quiz(quiz_id, answers):

    quiz = question_collection.find_one(
        {"_id": ObjectId(quiz_id)}
    )

    if not quiz:
        return None

    score = 0

    total_questions = len(quiz["questions"])

    for index, question in enumerate(quiz["questions"]):

        correct_answer = question["answer"]

        user_answer = answers.get(str(index))

        if user_answer == correct_answer:
            score += 1

    return {
        "score": score,
        "total": total_questions
    }