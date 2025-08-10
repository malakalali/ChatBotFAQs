#!/usr/bin/env python3
"""
Test script for Streamlit app functionality
This script tests the core components without running the full Streamlit interface.
"""

from matcher import FAQMatcher
from datetime import datetime

def test_streamlit_functionality():
    """Test the core functionality that would be used in the Streamlit app."""
    print("🧪 Testing Streamlit App Functionality")
    print("=" * 50)
    
    # Initialize matcher (same as in Streamlit app)
    matcher = FAQMatcher()
    
    # Test questions (same as example questions in Streamlit app)
    test_questions = [
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
    
    # Simulate chat history (like st.session_state.chat_history)
    chat_history = []
    session_start = datetime.now()
    
    print("📝 Testing Question Processing:")
    print("-" * 40)
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n{i}. Testing: '{question}'")
        
        # Simulate the processing that happens in Streamlit app
        timestamp = datetime.now().strftime('%H:%M:%S')
        
        # Add user message to history
        user_message = {
            'role': 'user',
            'content': question,
            'timestamp': timestamp
        }
        chat_history.append(user_message)
        
        # Get bot response (same as in Streamlit app)
        match = matcher.get_best_match(question, threshold=0.1)
        
        if match:
            response = match['answer']
            similarity_score = match['similarity_score']
            matched_question = match['question']
        else:
            response = "I'm sorry, I couldn't find a relevant answer. Please try rephrasing your question."
            similarity_score = 0
            matched_question = None
        
        # Add bot message to history
        bot_message = {
            'role': 'assistant',
            'content': response,
            'similarity_score': similarity_score,
            'matched_question': matched_question,
            'timestamp': timestamp
        }
        chat_history.append(bot_message)
        
        print(f"   ✅ Response: {response[:80]}...")
        print(f"   📊 Similarity: {similarity_score:.3f}")
        if matched_question:
            print(f"   🔗 Matched: {matched_question}")
    
    # Test session statistics (same as in Streamlit sidebar)
    session_duration = datetime.now() - session_start
    total_questions = len([msg for msg in chat_history if msg['role'] == 'user'])
    
    if total_questions > 0:
        successful_matches = sum(1 for msg in chat_history if msg.get('similarity_score', 0) > 0)
        success_rate = (successful_matches / total_questions) * 100
        avg_score = sum(msg.get('similarity_score', 0) for msg in chat_history) / len(chat_history)
    else:
        success_rate = 0
        avg_score = 0
        successful_matches = 0
    
    print(f"\n📊 Session Statistics (Streamlit Sidebar):")
    print("-" * 40)
    print(f"   Questions Asked: {total_questions}")
    print(f"   Success Rate: {success_rate:.1f}%")
    print(f"   Average Similarity: {avg_score:.3f}")
    print(f"   Session Duration: {session_duration}")
    print(f"   Total Messages: {len(chat_history)}")
    
    print(f"\n✅ Streamlit functionality test completed!")
    print(f"💡 The Streamlit app should work correctly with these components.")
    print(f"🌐 Run 'streamlit run streamlit_app.py' to start the web interface.")

if __name__ == "__main__":
    test_streamlit_functionality()
