import streamlit as st
import random

# Set page config
st.set_page_config(page_title="ECO EDU AGENT", page_icon="🌿", layout="centered")

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'quiz_index' not in st.session_state:
    st.session_state.quiz_index = 0
if 'quiz_data' not in st.session_state:
    st.session_state.quiz_data = random.sample([
        {
            "question": "What does PET stand for?",
            "options": ["Polyethylene Terephthalate", "Plastic Environmental Type", "Poly Extra Trash"],
            "answer": "Polyethylene Terephthalate"
        },
        {
            "question": "Which plastic is used in milk jugs?",
            "options": ["HDPE", "PVC", "PET"],
            "answer": "HDPE"
        },
        {
            "question": "Which plastic is found in straws and ketchup bottles?",
            "options": ["PP", "LDPE", "PET"],
            "answer": "PP"
        },
        {
            "question": "Which type of plastic is Styrofoam?",
            "options": ["PS", "PET", "PVC"],
            "answer": "PS"
        },
        {
            "question": "Which plastic type is the hardest to recycle?",
            "options": ["Other (7)", "HDPE", "PP"],
            "answer": "Other (7)"
        }
    ], 4)
if 'selected_option' not in st.session_state:
    st.session_state.selected_option = None
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# Navigation handler
def go_to(page_name):
    st.session_state.page = page_name

# Pages
def welcome():
    st.title("🌿 Welcome, Agent!")
    st.subheader("This is ECO EDU AGENT 🕵️‍♂️🌍")
    st.markdown("You're about to begin your journey to learn about plastics, recycling, and protecting our planet.")
    st.markdown("Are you ready to learn?")
    if st.button("🚀 Start Learning"):
        go_to("learn")

def learn():
    st.header("📚 Learn About Plastic Types")
    plastic_info = {
        "1 - PET (Polyethylene Terephthalate)": {
            "Examples": "Water bottles, soft drink containers",
            "Recyclable": "Yes",
            "Decomposition": "450 years",
            "Alternative": "Glass or metal bottles"
        },
        "2 - HDPE (High-Density Polyethylene)": {
            "Examples": "Milk jugs, detergent bottles",
            "Recyclable": "Yes",
            "Decomposition": "100 years",
            "Alternative": "Stainless steel containers"
        },
        "3 - PVC (Polyvinyl Chloride)": {
            "Examples": "Pipes, toys",
            "Recyclable": "No",
            "Decomposition": "1000 years",
            "Alternative": "Silicone, rubber"
        },
        "4 - LDPE (Low-Density Polyethylene)": {
            "Examples": "Plastic bags, wraps",
            "Recyclable": "Sometimes",
            "Decomposition": "500 years",
            "Alternative": "Cloth bags, beeswax wraps"
        },
        "5 - PP (Polypropylene)": {
            "Examples": "Straws, yogurt cups",
            "Recyclable": "Yes",
            "Decomposition": "20-30 years",
            "Alternative": "Bamboo, reusable containers"
        },
        "6 - PS (Polystyrene)": {
            "Examples": "Styrofoam, takeaway boxes",
            "Recyclable": "No",
            "Decomposition": "500 years",
            "Alternative": "Paper, cardboard, glass"
        },
        "7 - Other": {
            "Examples": "Baby bottles, CDs",
            "Recyclable": "No",
            "Decomposition": "Varies",
            "Alternative": "Glass, bioplastics"
        }
    }

    for type_name, details in plastic_info.items():
        with st.expander(type_name):
            st.markdown(f"""
- **Examples**: {details['Examples']}
- **Recyclable**: {details['Recyclable']}
- **Decomposition Time**: {details['Decomposition']}
- **Natural Alternatives**: {details['Alternative']}
""")

    if st.button("🧠 Start Quiz"):
        go_to("quiz")

def quiz():
    index = st.session_state.quiz_index
    question_data = st.session_state.quiz_data[index]

    st.header(f"🧠 Question {index + 1}")
    st.write(question_data["question"])

    st.session_state.selected_option = st.radio(
        "Choose one:",
        question_data["options"],
        index=None,
        key=f"radio_q{index}"
    )

    if st.button("✅ Submit Answer") and not st.session_state.submitted:
        if st.session_state.selected_option is None:
            st.warning("Please select an option.")
        else:
            st.session_state.submitted = True
            if st.session_state.selected_option == question_data["answer"]:
                st.success("Correct! ✅")
                st.session_state.score += 1
            else:
                st.error(f"Wrong. ❌ The correct answer is: **{question_data['answer']}**")

    if st.session_state.submitted:
        if st.button("➡️ Next"):
            st.session_state.quiz_index += 1
            st.session_state.submitted = False
            st.session_state.selected_option = None

            if st.session_state.quiz_index >= len(st.session_state.quiz_data):
                go_to("result")

def result():
    st.header("🎉 Mission Complete!")
    total = len(st.session_state.quiz_data)
    st.markdown(f"Your score: **{st.session_state.score} / {total}**")

    if st.session_state.score == total:
        st.success("🏅 Perfect! You’re an Eco Expert!")
    elif st.session_state.score >= total // 2:
        st.info("👍 Good job! You’re getting there.")
    else:
        st.warning("😕 Try again to improve your score.")

    if st.button("🔁 Retry Quiz"):
        st.session_state.quiz_index = 0
        st.session_state.score = 0
        st.session_state.selected_option = None
        st.session_state.submitted = False
        st.session_state.quiz_data = random.sample(st.session_state.quiz_data + [
            # Optionally add more new questions here
        ], len(st.session_state.quiz_data))
        go_to("quiz")

    if st.button("🏠 Back to Home"):
        st.session_state.score = 0
        st.session_state.quiz_index = 0
        go_to("welcome")

# App controller
if st.session_state.page == 'welcome':
    welcome()
elif st.session_state.page == 'learn':
    learn()
elif st.session_state.page == 'quiz':
    quiz()
elif st.session_state.page == 'result':
    result()
