import streamlit as st

def reverse_score(score):
    return 4 - score

def calculate_pss_score(answers):
    reversed_indices = [3, 4, 6, 7]  # Indices of questions to reverse score
    total_score = 0
    for i, ans in enumerate(answers):
        if i in reversed_indices:
            ans = reverse_score(ans)
        total_score += ans
    return total_score

def determine_stress_level(score):
    if score <= 13:
        return "Low stress"
    elif 14 <= score <= 26:
        return "Moderate stress"
    else:
        return "High stress"

def main():
    st.title("Perceived Stress Scale (PSS) Determination App")
    st.write("Answer the following questions to determine your perceived stress level.")

    questions = [
        "In the last month, how often have you been upset because of something that happened unexpectedly?",
        "In the last month, how often have you felt that you were unable to control the important things in your life?",
        "In the last month, how often have you felt nervous and stressed?",
        "In the last month, how often have you felt confident about your ability to handle your personal problems?",
        "In the last month, how often have you felt that things were going your way?",
        "In the last month, how often have you found that you could not cope with all the things that you had to do?",
        "In the last month, how often have you been able to control irritations in your life?",
        "In the last month, how often have you felt that you were on top of things?",
        "In the last month, how often have you been angered because of things that happened that were outside of your control?",
        "In the last month, how often have you felt difficulties were piling up so high that you could not overcome them?"
    ]

    answers = []
    for i, question in enumerate(questions):
        answer = st.selectbox(f"{i+1}. {question}", options=[0, 1, 2, 3, 4])
        answers.append(answer)

    if st.button("Calculate PSS Score"):
        total_score = calculate_pss_score(answers)
        stress_level = determine_stress_level(total_score)
        st.write(f"Your total PSS score is: {total_score}")
        st.write(f"Your stress level is: {stress_level}")

if __name__ == "__main__":
    main()
