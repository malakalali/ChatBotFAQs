from flask import Flask, render_template, request, jsonify
from matcher import FAQMatcher
from datetime import datetime
import json

app = Flask(__name__)
matcher = FAQMatcher()

@app.route('/')
def index():
    """Main page with chatbot interface."""
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_question():
    """Handle question requests."""
    try:
        data = request.get_json()
        question = data.get('question', '').strip()
        
        if not question:
            return jsonify({
                'success': False,
                'error': 'Please provide a question.'
            })
        
        # Get the best match
        match = matcher.get_best_match(question, threshold=0.1)
        
        if match:
            response = {
                'success': True,
                'answer': match['answer'],
                'similarity_score': round(match['similarity_score'], 3),
                'matched_question': match['question'],
                'user_question': question,
                'timestamp': datetime.now().strftime('%H:%M:%S')
            }
        else:
            response = {
                'success': False,
                'error': "I'm sorry, I couldn't find a relevant answer. Please try rephrasing your question.",
                'user_question': question,
                'timestamp': datetime.now().strftime('%H:%M:%S')
            }
        
        return jsonify(response)
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Sorry, something went wrong: {str(e)}'
        })

@app.route('/examples')
def get_examples():
    """Get example questions."""
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
        "Do you offer discounts for bulk orders?"
    ]
    return jsonify({'examples': examples})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
