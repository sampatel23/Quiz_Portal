import streamlit as st
import requests

st.set_page_config(
    page_title="Quiz Portal",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Quiz Portal")

st.write("Available Quizzes")

response = requests.get("http://127.0.0.1:5000/quizzes")

quizzes = response.json()

for quiz in quizzes:

    st.subheader(quiz["title"])

    st.write(f"Difficulty : {quiz['difficulty']}")

    st.write(f"Duration : {quiz['duration']} minutes")

    if st.button("Start Quiz", key=quiz["id"]):

        st.session_state["quiz_id"] = quiz["id"]

        st.switch_page("pages/Quiz.py")

    st.divider()