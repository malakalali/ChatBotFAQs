# ChatbotFAQs 🤖

A comprehensive Python-based FAQ chatbot system that uses natural language processing to intelligently match user questions with predefined answers. Built with modern NLP techniques and multiple interface options.

## ✨ Features

- **📚 FAQ Management**: Structured storage of 20+ question-answer pairs
- **🧠 Text Preprocessing**: Advanced NLP preprocessing using NLTK and SpaCy
- **🎯 Smart Matching**: TF-IDF vectorization with cosine similarity for intelligent matching
- **💬 Multiple Interfaces**: Command-line, web, and Streamlit interfaces
- **📊 Real-time Analytics**: Session statistics and similarity scores
- **🎨 Modern UI**: Beautiful, responsive interfaces with chat history
- **🔧 Easy Setup**: Simple installation and configuration

## Project Structure

```
ChatbotFAQs/
├── venv/                 # Virtual environment
├── faqs.py              # FAQ data storage
├── preprocess.py        # Text preprocessing functions
├── processed_faqs.py    # Preprocessed FAQ data
├── matcher.py           # Question matching algorithm
├── test_matcher.py      # Matching system tests
├── chatbot_demo.py      # Simple chatbot demo
├── chatbot_interface.py # Enhanced command-line interface
├── web_chatbot.py       # Web-based chatbot interface
├── streamlit_app.py     # Streamlit chat interface
├── demo_chatbot.py      # Demo script with examples
├── test_streamlit.py    # Streamlit functionality test
├── templates/           # Web interface templates
│   └── index.html      # Web chatbot interface
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## 🚀 Quick Start

### Installation

1. **Clone or download the project**
   ```bash
   cd ChatbotFAQs
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download SpaCy language model**
   ```bash
   python -m spacy download en_core_web_sm
   ```

### 🎯 One-Click Demo

Want to see it in action immediately? Run:
```bash
python demo_chatbot.py
```

## 💬 Usage

### 🎮 Interactive Interfaces

**🌟 Recommended: Streamlit Interface**
```bash
streamlit run streamlit_app.py
```
✨ Modern web interface with chat history, session statistics, and example questions

**🖥️ Web Interface**
```bash
python web_chatbot.py
```
🌐 Then open http://localhost:5000 for a beautiful web interface

**💻 Command-Line Interface**
```bash
python chatbot_interface.py
```
📊 Features: Conversation history, session statistics, help system

**🎯 Quick Demo**
```bash
python demo_chatbot.py
```
⚡ Shows the chatbot answering predefined questions with similarity scores

### 🔧 Programmatic Usage

**Load and Use FAQs**
```python
from faqs import faqs
from matcher import FAQMatcher

# Initialize the matcher
matcher = FAQMatcher()

# Ask a question
answer = matcher.get_answer("How do I reset my password?")
print(answer)

# Get detailed match information
match = matcher.get_best_match("What are your business hours?")
if match:
    print(f"Answer: {match['answer']}")
    print(f"Similarity: {match['similarity_score']:.3f}")
```

**Text Preprocessing**
```python
from preprocess import preprocess_text

# Preprocess any text
processed = preprocess_text("How can I reset my password?")
print(processed)  # Output: reset password
```

## 📦 Dependencies

- **🧠 NLTK**: Natural Language Toolkit for text processing and tokenization
- **🔍 SpaCy**: Advanced NLP library for text analysis and lemmatization
- **🤖 scikit-learn**: Machine learning library for TF-IDF vectorization and cosine similarity
- **🌐 Flask**: Web framework for the web-based chatbot interface
- **📊 Streamlit**: Modern web framework for the Streamlit chat interface
- **🐍 Python 3.9+**: Required for compatibility with all dependencies

## 🚀 Development Status

- ✅ **Step 1**: FAQ collection and storage (20+ questions)
- ✅ **Step 2**: Text preprocessing with NLTK and SpaCy
- ✅ **Step 3**: Question matching algorithm (TF-IDF + Cosine Similarity)
- ✅ **Step 4**: Multiple chatbot interfaces (CLI, Web, Streamlit)
- ✅ **Step 5**: Streamlit chat UI with modern design

🎉 **Project Complete!** All features implemented and tested.

## 🎯 Example Questions

The chatbot can answer questions about:

- **🔐 Account Management**: Password reset, account updates, login issues
- **📦 Order Processing**: Order tracking, cancellation, shipping status
- **🛍️ Customer Service**: Contact methods, business hours, support channels
- **📋 Policies**: Return policy, warranty information, privacy policy
- **💳 Payment & Shipping**: Payment methods, shipping times, international delivery
- **🔧 Technical Support**: Website issues, installation services, troubleshooting

## 🧪 Testing

Run comprehensive tests to verify functionality:

```bash
# Test the matching system
python test_matcher.py

# Test preprocessing functionality
python test_preprocessing.py

# Test Streamlit components
python test_streamlit.py

# Run demo with examples
python demo_chatbot.py
```

## 🤝 Contributing

Feel free to contribute by:
- 📝 Adding more FAQs to `faqs.py`
- 🧠 Improving preprocessing algorithms in `preprocess.py`
- 🎯 Enhancing matching logic in `matcher.py`
- 🎨 Improving UI/UX in interface files
- 🧪 Adding more test cases

## 📄 License

This project is open source and available under the MIT License.

---

**Built with ❤️ using Python, NLTK, SpaCy, scikit-learn, Flask, and Streamlit**
