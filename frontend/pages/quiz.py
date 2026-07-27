import streamlit as st
import requests

st.title("Quiz")

# -----------------------------
# Check if quiz was selected
# -----------------------------
if "quiz_id" not in st.session_state:
    st.error("No quiz selected.")
    st.stop()

quiz_id = st.session_state["quiz_id"]

# -----------------------------
# Get quiz from backend
# -----------------------------
response = requests.get(
    f"http://127.0.0.1:5000/quiz/{quiz_id}"
)

quiz = response.json()

st.header(quiz["title"])
st.write(f"Difficulty : {quiz['difficulty']}")
st.write(f"Duration : {quiz['duration']} minutes")

st.divider()

# -----------------------------
# Display Questions
# -----------------------------
for i, question in enumerate(quiz["questions"], start=1):

    st.subheader(f"Question {i}")

    st.write(question["question"])

    st.radio(
        "Choose an answer",
        question["options"],
        key=f"q{i}"
    )

    st.divider()

# -----------------------------
# Submit Button
# -----------------------------
if st.button("Submit Quiz"):

    answers = {}

    for i in range(len(quiz["questions"])):

        answers[str(i)] = st.session_state.get(f"q{i+1}")

    payload = {

        "quiz_id": quiz_id,

        "answers": answers

    }

    response = requests.post(

        "http://127.0.0.1:5000/submit",

        json=payload

    )

    result = response.json()

    # st.write(result)

    # Save result in session
    st.session_state["result"] = result

    # Move to Result page
    st.switch_page("pages/result.py")