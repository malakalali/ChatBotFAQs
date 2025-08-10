from matcher import FAQMatcher
import time
from datetime import datetime

class ChatbotInterface:
    def __init__(self):
        """Initialize the chatbot interface."""
        self.matcher = FAQMatcher()
        self.conversation_history = []
        self.session_start = datetime.now()
        
    def display_welcome(self):
        """Display welcome message and instructions."""
        print("🤖" + "="*60 + "🤖")
        print("           Welcome to the FAQ Chatbot!")
        print("🤖" + "="*60 + "🤖")
        print()
        print("💡 I can help you with questions about:")
        print("   • Account management (password reset, account updates)")
        print("   • Order processing (tracking, cancellation, shipping)")
        print("   • Customer support (contact methods, business hours)")
        print("   • Policies (returns, warranties, privacy)")
        print("   • Payment and shipping options")
        print("   • Technical support and website issues")
        print()
        print("📝 Commands:")
        print("   • Type 'help' to see example questions")
        print("   • Type 'history' to see conversation history")
        print("   • Type 'stats' to see session statistics")
        print("   • Type 'quit', 'exit', or 'bye' to end the conversation")
        print()
        print("🔍 Ask me anything!")
        print("-" * 70)
        
    def get_user_input(self):
        """Get and validate user input."""
        try:
            user_input = input("\n👤 You: ").strip()
            return user_input
        except KeyboardInterrupt:
            return "quit"
        except EOFError:
            return "quit"
            
    def process_command(self, command):
        """Process special commands."""
        command = command.lower()
        
        if command in ['quit', 'exit', 'bye']:
            return self.handle_exit()
        elif command == 'help':
            return self.show_help()
        elif command == 'history':
            return self.show_history()
        elif command == 'stats':
            return self.show_stats()
        elif command == '':
            print("🤖 Please ask a question or type 'help' for examples.")
            return True
        else:
            return self.handle_question(command)
            
    def handle_question(self, question):
        """Handle a user question."""
        print(f"\n🤖 Processing your question...")
        
        # Get the best match
        match = self.matcher.get_best_match(question, threshold=0.1)
        
        # Record in conversation history
        self.conversation_history.append({
            'timestamp': datetime.now(),
            'question': question,
            'answer': match['answer'] if match else "No relevant answer found",
            'similarity_score': match['similarity_score'] if match else 0,
            'matched_question': match['question'] if match else None
        })
        
        if match:
            print(f"\n✅ Found a relevant answer!")
            print(f"📊 Similarity Score: {match['similarity_score']:.3f}")
            print(f"🔗 Matched Question: '{match['question']}'")
            print(f"\n💬 Answer:")
            print(f"   {match['answer']}")
        else:
            print(f"\n❌ I couldn't find a relevant answer.")
            print(f"💡 Try rephrasing your question or type 'help' for examples.")
            
        return True
        
    def show_help(self):
        """Show help with example questions."""
        print("\n🤖 Here are some example questions you can ask:")
        print("-" * 50)
        
        examples = [
            "How can I reset my password?",
            "What are your business hours?",
            "How do I track my order?",
            "What is your return policy?",
            "Do you ship internationally?",
            "How can I contact customer support?",
            "What payment methods do you accept?",
            "How long does shipping take?",
            "Can I cancel my order?",
            "Do you offer discounts for bulk orders?",
            "What warranty do you provide?",
            "How do I update my account information?",
            "Are your products environmentally friendly?",
            "Can I get a refund instead of a replacement?",
            "Do you have a loyalty program?"
        ]
        
        for i, example in enumerate(examples, 1):
            print(f"  {i:2d}. {example}")
            
        print(f"\n💡 You can also ask questions in your own words!")
        print(f"   For example: 'I forgot my password' or 'Where is my package?'")
        return True
        
    def show_history(self):
        """Show conversation history."""
        if not self.conversation_history:
            print("\n🤖 No conversation history yet.")
            return True
            
        print(f"\n📚 Conversation History ({len(self.conversation_history)} questions):")
        print("-" * 60)
        
        for i, entry in enumerate(self.conversation_history, 1):
            timestamp = entry['timestamp'].strftime("%H:%M:%S")
            score = entry['similarity_score']
            print(f"\n{i}. [{timestamp}] (Score: {score:.3f})")
            print(f"   Q: {entry['question']}")
            if entry['matched_question']:
                print(f"   → Matched: {entry['matched_question']}")
            print(f"   A: {entry['answer'][:100]}...")
            
        return True
        
    def show_stats(self):
        """Show session statistics."""
        session_duration = datetime.now() - self.session_start
        total_questions = len(self.conversation_history)
        
        if total_questions > 0:
            avg_score = sum(entry['similarity_score'] for entry in self.conversation_history) / total_questions
            successful_matches = sum(1 for entry in self.conversation_history if entry['similarity_score'] > 0)
            success_rate = (successful_matches / total_questions) * 100
        else:
            avg_score = 0
            success_rate = 0
            
        print(f"\n📊 Session Statistics:")
        print("-" * 30)
        print(f"   Session Duration: {session_duration}")
        print(f"   Total Questions: {total_questions}")
        print(f"   Average Similarity Score: {avg_score:.3f}")
        print(f"   Success Rate: {success_rate:.1f}%")
        print(f"   Successful Matches: {successful_matches}")
        
        return True
        
    def handle_exit(self):
        """Handle exit command."""
        session_duration = datetime.now() - self.session_start
        total_questions = len(self.conversation_history)
        
        print(f"\n🤖 Thank you for using the FAQ Chatbot!")
        print(f"📊 Session Summary:")
        print(f"   • Duration: {session_duration}")
        print(f"   • Questions Asked: {total_questions}")
        print(f"   • Have a great day! 👋")
        
        return False
        
    def run(self):
        """Run the chatbot interface."""
        self.display_welcome()
        
        while True:
            try:
                user_input = self.get_user_input()
                should_continue = self.process_command(user_input)
                
                if not should_continue:
                    break
                    
            except Exception as e:
                print(f"\n🤖 Sorry, something went wrong: {e}")
                print("   Please try again.")

def main():
    """Main function to run the chatbot."""
    chatbot = ChatbotInterface()
    chatbot.run()

if __name__ == "__main__":
    main()
