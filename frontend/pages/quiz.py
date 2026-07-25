import streamlit as st
import requests

st.title("Quiz")

if "quiz_id" not in st.session_state:

    st.error("No quiz selected.")

    st.stop()

quiz_id = st.session_state["quiz_id"]

response = requests.get(
    f"http://127.0.0.1:5000/quiz/{quiz_id}"
)

quiz = response.json()

st.header(quiz["title"])

st.write(f"Difficulty : {quiz['difficulty']}")

st.write(f"Duration : {quiz['duration']} minutes")

st.divider()

for i, question in enumerate(quiz["questions"], start=1):

    st.subheader(f"Question {i}")

    st.write(question["question"])

    st.radio(

        "Choose an answer",

        question["options"],

        key=f"q{i}"

    )

    st.divider()