import streamlit as st
from chatbot import chat_with_gemini
from file_utils import extract_text_from_pdfs

# Set page config
st.set_page_config(page_title="AI Chatbot", layout="wide")

# Sidebar - File Upload
st.sidebar.header("📂 Upload PDFs for Context")
uploaded_files = st.sidebar.file_uploader("Choose PDFs", accept_multiple_files=True, type=["pdf"])

# Extract text from PDFs
pdf_text = extract_text_from_pdfs(uploaded_files) if uploaded_files else ""

# Main UI
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🧠 AI Chatbot</h1>", unsafe_allow_html=True)

# Chat Interface
st.markdown("<h4 style='color: #555;'>Ask a question based on PDFs or general topics:</h4>", unsafe_allow_html=True)
user_input = st.text_input("Enter your question...", key="input_text", help="Type and press send.")

# Send button
if st.button("Send 🚀"):
    if user_input:
        brief, long = chat_with_gemini(user_input, pdf_text)
        st.markdown(f"<h5 style='color: #4CAF50;'>💡 Brief Answer:</h5> <p>{brief}</p>", unsafe_allow_html=True)
        st.markdown(f"<h5 style='color: #FF9800;'>📖 Detailed Answer:</h5> <p>{long}</p>", unsafe_allow_html=True)
    else:
        st.warning("Please enter a question!")
