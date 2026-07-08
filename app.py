import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
from prompts import PERSONA
import base64

def get_base64(file_path):
    with open(file_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def get_ai_response(user_prompt):
    prompt = f"""
{PERSONA}

{user_prompt}
"""

    response = model.generate_content(prompt)
    return response.text


st.set_page_config(
    page_title="ChefMate AI",
    page_icon="🍳",
    layout="wide"
)

hero_img = get_base64("assets/hero.jpg")

st.markdown("""
<style>

.main .block-container{
    padding-top:2rem;
    padding-left:3rem;
    padding-right:3rem;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

div.stButton > button{

background:#FF9800;

color:white;

border:none;

border-radius:12px;

height:55px;

width:100%;

font-size:18px;

font-weight:600;

}

div.stButton > button:hover{

background:#ffb74d;

color:black;

}

</style>

""",unsafe_allow_html=True)

st.sidebar.title("🍳 ChefMate AI")

st.sidebar.markdown("""
### 👩‍🍳 AI Buddy

**Lavanya**

Your friendly AI Cooking Tutor.

---

### Features

📖 Explain Concepts

🍳 Real-life Examples

❓ Generate Quizzes

✅ Evaluate Answers

🎓 Complete Learning Sessions

💬 Ask Cooking Questions
""")

st.markdown(f"""
<style>

.hero {{
    background-image:
        linear-gradient(rgba(0,0,0,0.60), rgba(0,0,0,0.60)),
        url("data:image/jpeg;base64,{hero_img}");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;

    border-radius:25px;
    padding:160px 50px;
    color:white;
    text-align:center;
    margin-bottom:35px;
}}

.hero-content{{
    position:relative;
    z-index:2;
}}

.badge-container{{
    display:flex;
    gap:15px;
    justify-content:center;
    flex-wrap:wrap;
    margin-top:25px;
}}

.badge{{
    background:#FF9800;
    color:white;
    padding:12px 24px;
    border-radius:30px;
    font-size:18px;
    font-weight:600;
}}

</style>

<div class="hero">
<div class="hero-content">

<h1>🍳 ChefMate AI</h1>

<h3>Your Personal AI Learning Buddy</h3>

<p>
Learn cooking through interactive lessons,
real-life examples,
AI quizzes,
and personalized feedback powered by Gemini AI.
</p>

<div class="badge-container">
<span class="badge">📖 Learn</span>
<span class="badge">🍳 Practice</span>
<span class="badge">❓ Quiz</span>
<span class="badge">✅ Feedback</span>
</div>

</div>
</div>

""", unsafe_allow_html=True)

st.markdown("<div style='max-width:1100px; margin:auto;'>", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<div style='
background:#18273d;
padding:25px;
border-radius:20px;
border-left:6px solid #FF9800;
margin-bottom:30px;
'>

<h2 style='color:white;'>👩‍🍳 Meet Lavanya</h2>

<p style='color:white;font-size:18px;'>

Hi! I'm <b>Lavanya</b>, your AI Cooking Tutor.<br><br>

🍳 Learn recipes step-by-step<br>
📖 Understand cooking concepts<br>
💡 Real-life cooking examples<br>
❓ Interactive quizzes<br>
✅ Personalized feedback<br>
🌱 Healthy cooking tips

</p>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

topics = [
    "Dal Tadka",
    "Rice Cooking",
    "Roti Making",
    "Kitchen Safety",
    "Knife Skills",
    "Vegetable Curry",
    "Healthy Cooking",
    "Food Hygiene",
    "Indian Breakfast",
    "Spices & Seasoning"
]

col1,col2=st.columns(2)

with col1:

    topic=st.selectbox(
        "📚 Choose Cooking Topic",
        topics
    )

with col2:

    level=st.selectbox(
        "🎯 Skill Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

col1, col2 = st.columns(2)

with col1:

    explain = st.button("📖 Explain Concept")

    example = st.button("🍳 Real-life Example")

    quiz = st.button("❓ Generate Quiz")

with col2:

    feedback = st.button("✅ Check My Answer")

    lesson = st.button("🎓 Complete Learning Session")

st.markdown("---")

st.header("💬 Ask Lavanya Anything")

question = st.text_area(
    "Ask any cooking question"
)

ask = st.button("Ask Lavanya")

if explain:
    with st.spinner("Lavanya is preparing your lesson..."):
        response = get_ai_response(
            f"""
            Explain the topic '{topic}' to a {level.lower()} learner.

            Include:
            1. Introduction
            2. Ingredients or tools needed (if applicable)
            3. Step-by-step explanation
            4. Common beginner mistakes
            5. Healthy cooking tips
            6. End with one review question.
            """
        )

    st.markdown("## 📖 Explanation")
    st.success(response)

if example:
    with st.spinner("Lavanya is preparing a real-life example..."):
        response = get_ai_response(
            f"""
Provide one simple real-life cooking example for the topic '{topic}' suitable for a {level.lower()} learner.

Include:
- A relatable kitchen scenario
- Why this concept is important
- One common beginner mistake
- One practical tip
"""
        )

    st.markdown("## 🍳 Real-life Example")
    st.success(response)

if quiz:
    with st.spinner("Lavanya is creating your quiz..."):
        response = get_ai_response(
            f"""
Generate 5 multiple-choice questions on '{topic}' for a {level.lower()} learner.

Each question should have:
- Four options (A, B, C, D)
- Correct answer
- Short explanation
"""
        )

    st.markdown("## ❓ Quiz")
    st.success(response)

student_answer = st.text_area(
    "✍️ Enter your answer for evaluation"
)

if feedback:
    if student_answer.strip() == "":
        st.warning("Please enter your answer first.")
    else:
        with st.spinner("Lavanya is reviewing your answer..."):
            response = get_ai_response(
                f"""
The topic is '{topic}'.

Student's answer:
{student_answer}

Evaluate the answer.

Provide:
- Positive feedback
- Corrections (if any)
- Suggestions for improvement
- Encourage the learner
"""
            )

        st.markdown("## ✅ Feedback")
        st.success(response)

if lesson:
    with st.spinner("Lavanya is preparing your complete lesson..."):
        response = get_ai_response(
            f"""
Teach '{topic}' to a {level.lower()} learner.

Structure the lesson as follows:

1. Introduction
2. Explanation
3. Step-by-step guide
4. Real-life example
5. Healthy cooking tips
6. Three practice questions
7. A short quiz
8. Lesson summary
"""
        )

    st.markdown("## 🎓 Complete Learning Session")
    st.success(response)

if ask:
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Lavanya is thinking..."):
            response = get_ai_response(
                f"""
Answer the following cooking question as Lavanya, the AI Cooking Tutor.

Question:
{question}

Respond in simple English.
Provide practical cooking guidance.
If the question is related to health or medical advice, politely recommend consulting a qualified healthcare professional.
"""
            )

        st.markdown("## 💬 Lavanya's Answer")
        st.success(response)

st.markdown("---")

st.markdown("""

<center>

### 🍳 ChefMate AI

Powered by Streamlit + Google Gemini

Made with ❤️ by Lavanya Ajit Dive

</center>

""",unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)