import streamlit as st
import pandas as pd
from datetime import datetime
from matcher import FAQMatcher
import time

# Page configuration
st.set_page_config(
    page_title="FAQ Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border-left: 4px solid;
    }
    
    .user-message {
        background-color: #e3f2fd;
        border-left-color: #2196f3;
        margin-left: 2rem;
    }
    
    .bot-message {
        background-color: #f3e5f5;
        border-left-color: #9c27b0;
        margin-right: 2rem;
    }
    
    .similarity-score {
        background-color: #e8f5e8;
        color: #2e7d32;
        padding: 0.25rem 0.5rem;
        border-radius: 15px;
        font-size: 0.8rem;
        display: inline-block;
        margin-top: 0.5rem;
    }
    
    .matched-question {
        background-color: #fff3e0;
        color: #f57c00;
        padding: 0.25rem 0.5rem;
        border-radius: 15px;
        font-size: 0.8rem;
        display: inline-block;
        margin-top: 0.5rem;
    }
    
    .example-button {
        background-color: #f0f0f0;
        border: 1px solid #ddd;
        border-radius: 20px;
        padding: 0.5rem 1rem;
        margin: 0.25rem;
        cursor: pointer;
        transition: all 0.3s;
    }
    
    .example-button:hover {
        background-color: #667eea;
        color: white;
    }
    
    .stats-container {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #dee2e6;
    }
    
    .stTextInput > div > div > input {
        border-radius: 25px;
        border: 2px solid #e1e5e9;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 0.2rem rgba(102, 126, 234, 0.25);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'matcher' not in st.session_state:
    st.session_state.matcher = FAQMatcher()
if 'session_start' not in st.session_state:
    st.session_state.session_start = datetime.now()

# Header
st.markdown("""
<div class="main-header">
    <h1>🤖 FAQ Chatbot</h1>
    <p>Ask me anything about our services - I'm here to help!</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("📊 Session Info")
    
    # Session statistics
    session_duration = datetime.now() - st.session_state.session_start
    total_questions = len(st.session_state.chat_history)
    
    if total_questions > 0:
        successful_matches = sum(1 for msg in st.session_state.chat_history if msg.get('similarity_score', 0) > 0)
        success_rate = (successful_matches / total_questions) * 100
        avg_score = sum(msg.get('similarity_score', 0) for msg in st.session_state.chat_history) / total_questions
    else:
        success_rate = 0
        avg_score = 0
        successful_matches = 0
    
    st.metric("Questions Asked", total_questions)
    st.metric("Success Rate", f"{success_rate:.1f}%")
    st.metric("Avg Similarity", f"{avg_score:.3f}")
    st.metric("Session Duration", str(session_duration).split('.')[0])
    
    st.divider()
    
    # Clear chat button
    if st.button("🗑️ Clear Chat History", type="secondary"):
        st.session_state.chat_history = []
        st.rerun()
    
    st.divider()
    
    # Example questions
    st.header("💡 Example Questions")
    example_questions = [
        "How can I reset my password?",
        "What are your business hours?",
        "How do I track my order?",
        "What is your return policy?",
        "Do you ship internationally?",
        "How can I contact customer support?",
        "What payment methods do you accept?",
        "How long does shipping take?",
        "Can I cancel my order?",
        "Do you offer discounts for bulk orders?"
    ]
    
    for question in example_questions:
        if st.button(question, key=f"example_{question}"):
            st.session_state.example_question = question
            st.rerun()

# Main chat area
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Display chat history
    for message in st.session_state.chat_history:
        if message['role'] == 'user':
            st.markdown(f"""
            <div class="chat-message user-message">
                <strong>👤 You:</strong><br>
                {message['content']}
                <br><small style="color: #666;">{message['timestamp']}</small>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="chat-message bot-message">
                <strong>🤖 Assistant:</strong><br>
                {message['content']}
                {f'<br><span class="similarity-score">Similarity: {message.get("similarity_score", 0):.3f}</span>' if message.get('similarity_score') else ''}
                {f'<br><span class="matched-question">Matched: {message.get("matched_question", "")}</span>' if message.get('matched_question') else ''}
                <br><small style="color: #666;">{message['timestamp']}</small>
            </div>
            """, unsafe_allow_html=True)

# Input area
st.divider()

# Handle example question from sidebar
if 'example_question' in st.session_state:
    question = st.session_state.example_question
    del st.session_state.example_question
    
    # Add user message
    st.session_state.chat_history.append({
        'role': 'user',
        'content': question,
        'timestamp': datetime.now().strftime('%H:%M:%S')
    })
    
    # Get bot response
    match = st.session_state.matcher.get_best_match(question, threshold=0.1)
    
    if match:
        response = match['answer']
        similarity_score = match['similarity_score']
        matched_question = match['question']
    else:
        response = "I'm sorry, I couldn't find a relevant answer. Please try rephrasing your question."
        similarity_score = 0
        matched_question = None
    
    # Add bot message
    st.session_state.chat_history.append({
        'role': 'assistant',
        'content': response,
        'similarity_score': similarity_score,
        'matched_question': matched_question,
        'timestamp': datetime.now().strftime('%H:%M:%S')
    })
    
    st.rerun()

# Chat input
with st.container():
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Text input
        user_input = st.text_input(
            "Ask your question:",
            placeholder="Type your question here...",
            key="user_input",
            label_visibility="collapsed"
        )
        
        # Send button
        col_a, col_b, col_c = st.columns([1, 1, 1])
        with col_b:
            send_button = st.button("Send", type="primary", use_container_width=True)
        
        # Handle user input
        if send_button and user_input.strip():
            # Add user message
            st.session_state.chat_history.append({
                'role': 'user',
                'content': user_input.strip(),
                'timestamp': datetime.now().strftime('%H:%M:%S')
            })
            
            # Show thinking indicator
            with st.spinner("🤖 Thinking..."):
                time.sleep(0.5)  # Simulate processing time
                
                # Get bot response
                match = st.session_state.matcher.get_best_match(user_input.strip(), threshold=0.1)
                
                if match:
                    response = match['answer']
                    similarity_score = match['similarity_score']
                    matched_question = match['question']
                else:
                    response = "I'm sorry, I couldn't find a relevant answer. Please try rephrasing your question."
                    similarity_score = 0
                    matched_question = None
                
                # Add bot message
                st.session_state.chat_history.append({
                    'role': 'assistant',
                    'content': response,
                    'similarity_score': similarity_score,
                    'matched_question': matched_question,
                    'timestamp': datetime.now().strftime('%H:%M:%S')
                })
            
            # Rerun to update the interface
            st.rerun()

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.8rem;">
    <p>💡 Tip: Try asking questions in your own words or click example questions from the sidebar!</p>
    <p>Powered by TF-IDF and Cosine Similarity 🤖</p>
</div>
""", unsafe_allow_html=True)
