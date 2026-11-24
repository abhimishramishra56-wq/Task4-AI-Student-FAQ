import streamlit as st

st.set_page_config(page_title="AI Student FAQ Assistant", page_icon="🤖")

st.title("🤖 AI Student FAQ Assistant")

st.write("Welcome! Ask questions about Artificial Intelligence, Python, and Data Science.")

st.info("This is a beginner-friendly FAQ assistant.")

question = st.text_input("💬 Enter your question:")

answers = {
    "what is ai": "AI stands for Artificial Intelligence. It enables machines to perform tasks that require human intelligence.",
    "what is artificial intelligence": "Artificial Intelligence is the ability of machines to perform tasks that normally require human intelligence.",
    "what is machine learning": "Machine Learning is a branch of AI that allows computers to learn patterns from data.",
    "what is data science": "Data Science involves collecting, analyzing, and interpreting data to extract useful information.",
    "what is python": "Python is a simple and popular programming language used in AI, Data Science, automation, and web development.",
    "what is nlp": "NLP stands for Natural Language Processing. It helps computers understand and process human language.",
    "what is deep learning": "Deep Learning is a branch of Machine Learning that uses multi-layered neural networks.",
    "what is chatbot": "A chatbot is a computer program designed to communicate with users through text or conversation.",
    "what is algorithm": "An algorithm is a step-by-step procedure used to solve a problem.",
    "what is data": "Data is a collection of facts, values, or information used for analysis and decision-making.",
    "what is computer vision": "Computer Vision is a field of AI that enables computers to analyze and understand images and videos.",
    "what is neural network": "A Neural Network is a computing model inspired by how biological brains process information."
}

if st.button("Get Answer"):
    if question.strip():
        key = question.lower().strip().rstrip("?.!")
        
        if key in answers:
            st.success(answers[key])
        else:
            st.warning("Sorry, I don't know this question yet. Please try a suggested question.")
    else:
        st.error("Please enter a question first.")

st.subheader("📚 Try These Questions")

st.write("""
- What is AI?
- What is Python?
- What is Data Science?
- What is Machine Learning?
- What is NLP?
- What is Deep Learning?
- What is Computer Vision?
- What is Neural Network?
""")

st.caption("Beginner AI Project | Task 4")