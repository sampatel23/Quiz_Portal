import streamlit as st

st.set_page_config(
    page_title="Quiz Result",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 Quiz Result")

# -----------------------------
# Check if result exists
# -----------------------------
if "result" not in st.session_state:

    st.error("No result found.")

    st.stop()

result = st.session_state["result"]

st.success("Quiz Submitted Successfully!")

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Score",
        f"{result['score']} / {result['total_questions']}"
    )

    st.metric(
        "Correct Answers",
        result["correct_answers"]
    )

with col2:

    st.metric(
        "Percentage",
        f"{result['percentage']}%"
    )

    st.metric(
        "Wrong Answers",
        result["wrong_answers"]
    )

st.divider()

if result["status"] == "Pass":

    st.success("🎉 Congratulations! You Passed!")

else:

    st.error("❌ Better Luck Next Time!")

st.divider()

if st.button("🏠 Back to Home"):

    # Remove old data
    st.session_state.pop("quiz_id", None)
    st.session_state.pop("result", None)

    st.switch_page("home.py")