import re
import nltk
import spacy
import ssl
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Handle SSL certificate issues for NLTK downloads
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Download required NLTK data
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    """
    Preprocess text for FAQ matching by:
    - Lowercasing
    - Tokenizing
    - Removing stopwords
    - Removing punctuation and special characters
    - Lemmatizing words
    
    Args:
        text (str): Input text to preprocess
        
    Returns:
        str: Preprocessed text
    """
    if not text or not isinstance(text, str):
        return ""
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters and punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Tokenize using simple split
    tokens = text.split()
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    
    # Lemmatize words
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    # Join tokens back into string
    processed_text = ' '.join(tokens)
    
    return processed_text

def preprocess_faqs(faqs_list):
    """
    Preprocess all FAQ questions and add processed versions to the data structure.
    
    Args:
        faqs_list (list): List of FAQ dictionaries
        
    Returns:
        list: Updated FAQ list with preprocessed questions
    """
    processed_faqs = []
    
    for faq in faqs_list:
        processed_faq = faq.copy()
        processed_faq['processed_question'] = preprocess_text(faq['question'])
        processed_faqs.append(processed_faq)
    
    return processed_faqs

def get_preprocessed_question(faq):
    """
    Get the preprocessed version of a FAQ question.
    
    Args:
        faq (dict): FAQ dictionary
        
    Returns:
        str: Preprocessed question text
    """
    if 'processed_question' in faq:
        return faq['processed_question']
    else:
        return preprocess_text(faq['question'])
