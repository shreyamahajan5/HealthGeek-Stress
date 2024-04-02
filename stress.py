import streamlit as st

def reverse_score(score):
    """Reverse the score for questions 4, 5, 7, and 8."""
    return 4 - score

def calculate_pss_score(answers):
    """Calculate the PSS score."""
    reversed_indices = [3, 4, 6, 7]
    total_score = 0
    for i, ans in enumerate(answers):
        if i in reversed_indices:
            ans = reverse_score(ans)
        total_score += ans
    return total_score

def determine_stress_level(score):
    """Determine the stress level based on the PSS score."""
    if score <= 13:
        return "Low stress"
    elif 14 <= score <= 26:
        return "Moderate stress"
    else:
        return "High stress"

def main():
    st.sidebar.title("About Perceived Stress Scale (PSS)")
    st.sidebar.write("""
    The Perceived Stress Scale (PSS) is a classic stress assessment instrument developed in 1983. It helps measure individual stress levels based on feelings and thoughts over the last month.
    """)

    st.title("Perceived Stress Scale (PSS) Determination App")
    st.write("For each question, choose from the following alternatives:\n"
             "0 - never\n"
             "1 - almost never\n"
             "2 - sometimes\n"
             "3 - fairly often\n"
             "4 - very often\n\n\n")
    st.header("Answer the following questions to determine your perceived stress level.")

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
        "In the last month, how often have you felt difficulties were piling up so high that you could not overcome them?\n"
    ]

    answers = []
    for i, question in enumerate(questions):
        answer = st.slider(f"{i+1}. {question}", min_value=0, max_value=4, step=1)
        answers.append(answer)

    if st.button("Calculate PSS Score"):
        total_score = calculate_pss_score(answers)
        stress_level = determine_stress_level(total_score)
        st.write(f"Your total PSS score is: {total_score}")
        st.write(f"Your stress level is: {stress_level}")

        st.subheader("Mental Health Practices to Manage Stress:")
        if stress_level == "Low stress":
            st.write("- Practice relaxation techniques such as deep breathing, meditation, or yoga.")
            st.write("- Maintain a healthy lifestyle with regular exercise and a balanced diet.")
            st.write("- Engage in hobbies or activities that you enjoy.")
            st.write("- Seek social support from friends and family.")
        elif stress_level == "Moderate stress":
            st.write("- In addition to the practices for low stress, consider seeking professional help or counseling.")
            st.write("- Prioritize tasks and practice time management.")
            st.write("- Limit exposure to stressful situations or triggers.")
            st.write("- Take breaks and engage in stress-relieving activities throughout the day.")
        else:
            st.write("- Seek professional help or counseling to develop coping strategies.")
            st.write("- Practice self-care and prioritize your mental health.")
            st.write("- Consider lifestyle changes to reduce overall stress levels.")
            st.write("- Connect with a support group or community for additional support.\n\n")
        
        st.write("Note: It's always better to seek professional help if you're experiencing high levels of stress.")

if __name__ == "__main__":
    main()
