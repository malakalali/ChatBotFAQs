#!/usr/bin/env python3
"""
FAQ Chatbot Demo
This script demonstrates the chatbot functionality with predefined questions.
"""

from matcher import FAQMatcher
import time

def demo_chatbot():
    """Run a demonstration of the chatbot."""
    print("🤖 FAQ Chatbot Demo")
    print("=" * 50)
    print()
    
    # Initialize the matcher
    matcher = FAQMatcher()
    
    # Demo questions
    demo_questions = [
        "I forgot my password, how do I reset it?",
        "What time are you open?",
        "Where is my order?",
        "Can I return this item?",
        "Do you ship to Europe?",
        "How do I contact customer service?",
        "What credit cards do you accept?",
        "When will my order arrive?",
        "I need to cancel my order",
        "Do you have bulk discounts?"
    ]
    
    print("📝 Demo Questions and Answers:")
    print("-" * 50)
    
    for i, question in enumerate(demo_questions, 1):
        print(f"\n{i}. 👤 Question: {question}")
        
        # Simulate thinking
        print("   🤖 Thinking...", end="", flush=True)
        time.sleep(0.5)
        print("\r", end="", flush=True)
        
        # Get answer
        answer = matcher.get_answer(question)
        print(f"   🤖 Answer: {answer}")
        
        # Show match details if available
        match = matcher.get_best_match(question)
        if match:
            print(f"   📊 Similarity Score: {match['similarity_score']:.3f}")
            print(f"   🔗 Matched: '{match['question']}'")
        
        print("   " + "-" * 40)
    
    print(f"\n✅ Demo completed! The chatbot answered {len(demo_questions)} questions.")
    print("\n💡 You can now run the interactive chatbot:")
    print("   • Command line: python chatbot_interface.py")
    print("   • Web interface: python web_chatbot.py")
    print("   • Simple demo: python chatbot_demo.py")

if __name__ == "__main__":
    demo_chatbot()
