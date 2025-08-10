from matcher import FAQMatcher

def run_chatbot():
    """
    Run an interactive chatbot demo.
    """
    print("🤖 Welcome to the FAQ Chatbot!")
    print("=" * 50)
    print("Ask me any question about our services.")
    print("Type 'quit' or 'exit' to end the conversation.")
    print("Type 'help' to see example questions.")
    print("-" * 50)
    
    # Initialize the matcher
    matcher = FAQMatcher()
    
    # Example questions for help
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
    
    while True:
        try:
            # Get user input
            user_input = input("\n👤 You: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("🤖 Chatbot: Goodbye! Have a great day!")
                break
            
            # Check for help command
            if user_input.lower() == 'help':
                print("\n🤖 Chatbot: Here are some example questions you can ask:")
                for i, question in enumerate(example_questions, 1):
                    print(f"  {i}. {question}")
                continue
            
            # Skip empty input
            if not user_input:
                print("🤖 Chatbot: Please ask a question!")
                continue
            
            # Get the best match
            match = matcher.get_best_match(user_input, threshold=0.1)
            
            if match:
                print(f"\n🤖 Chatbot: {match['answer']}")
                print(f"\n📊 Match Details:")
                print(f"   Original Question: {match['question']}")
                print(f"   Similarity Score: {match['similarity_score']:.3f}")
            else:
                print("\n🤖 Chatbot: I'm sorry, I couldn't find a relevant answer.")
                print("   Try rephrasing your question or type 'help' for examples.")
                
        except KeyboardInterrupt:
            print("\n\n🤖 Chatbot: Goodbye! Have a great day!")
            break
        except Exception as e:
            print(f"\n🤖 Chatbot: Sorry, something went wrong: {e}")
            print("   Please try again.")

def quick_test():
    """
    Run a quick test of the chatbot with predefined questions.
    """
    print("🧪 Quick Test of FAQ Chatbot")
    print("=" * 40)
    
    matcher = FAQMatcher()
    
    test_questions = [
        "I forgot my password",
        "What time do you open?",
        "Where is my package?",
        "Can I return this?",
        "Do you ship to Europe?",
        "How do I call customer service?",
        "What cards do you take?",
        "When will my order arrive?",
        "I need to cancel my order",
        "Do you have bulk discounts?"
    ]
    
    for question in test_questions:
        print(f"\n👤 Q: {question}")
        answer = matcher.get_answer(question)
        print(f"🤖 A: {answer}")
        print("-" * 40)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        quick_test()
    else:
        run_chatbot()
