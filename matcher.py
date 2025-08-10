from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from preprocess import preprocess_text
from processed_faqs import get_processed_faqs

class FAQMatcher:
    def __init__(self, faqs=None):
        """
        Initialize the FAQ matcher with TF-IDF vectorization.
        
        Args:
            faqs (list): List of FAQ dictionaries. If None, loads from processed_faqs
        """
        if faqs is None:
            self.faqs = get_processed_faqs()
        else:
            self.faqs = faqs
            
        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words='english',
            ngram_range=(1, 2),
            max_features=1000
        )
        
        # Prepare FAQ questions for vectorization
        self.faq_questions = [faq['processed_question'] for faq in self.faqs]
        
        # Fit the vectorizer on FAQ questions
        self.faq_vectors = self.vectorizer.fit_transform(self.faq_questions)
        
    def get_best_match(self, user_question, threshold=0.1):
        """
        Find the best matching FAQ for a user question.
        
        Args:
            user_question (str): Raw user question
            threshold (float): Minimum similarity threshold (0-1)
            
        Returns:
            dict: Best matching FAQ with similarity score, or None if below threshold
        """
        if not user_question or not user_question.strip():
            return None
            
        # Preprocess user question
        processed_question = preprocess_text(user_question)
        
        if not processed_question:
            return None
            
        # Vectorize user question
        user_vector = self.vectorizer.transform([processed_question])
        
        # Calculate cosine similarity
        similarities = cosine_similarity(user_vector, self.faq_vectors).flatten()
        
        # Find best match
        best_index = np.argmax(similarities)
        best_score = similarities[best_index]
        
        # Check if similarity is above threshold
        if best_score >= threshold:
            best_faq = self.faqs[best_index].copy()
            best_faq['similarity_score'] = best_score
            best_faq['user_question'] = user_question
            best_faq['processed_user_question'] = processed_question
            return best_faq
        else:
            return None
    
    def get_top_matches(self, user_question, top_k=3, threshold=0.05):
        """
        Get top k matching FAQs for a user question.
        
        Args:
            user_question (str): Raw user question
            top_k (int): Number of top matches to return
            threshold (float): Minimum similarity threshold
            
        Returns:
            list: List of top matching FAQs with similarity scores
        """
        if not user_question or not user_question.strip():
            return []
            
        # Preprocess user question
        processed_question = preprocess_text(user_question)
        
        if not processed_question:
            return []
            
        # Vectorize user question
        user_vector = self.vectorizer.transform([processed_question])
        
        # Calculate cosine similarity
        similarities = cosine_similarity(user_vector, self.faq_vectors).flatten()
        
        # Get top k indices
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        # Filter by threshold and create results
        matches = []
        for idx in top_indices:
            score = similarities[idx]
            if score >= threshold:
                faq = self.faqs[idx].copy()
                faq['similarity_score'] = score
                faq['user_question'] = user_question
                faq['processed_user_question'] = processed_question
                matches.append(faq)
        
        return matches
    
    def get_answer(self, user_question, threshold=0.1):
        """
        Get the answer for a user question.
        
        Args:
            user_question (str): Raw user question
            threshold (float): Minimum similarity threshold
            
        Returns:
            str: Answer text or "I'm sorry, I couldn't find a relevant answer."
        """
        match = self.get_best_match(user_question, threshold)
        
        if match:
            return match['answer']
        else:
            return "I'm sorry, I couldn't find a relevant answer. Please try rephrasing your question."

def get_best_match(user_question, faqs=None, threshold=0.1):
    """
    Convenience function to get the best matching FAQ.
    
    Args:
        user_question (str): Raw user question
        faqs (list): Optional list of FAQs
        threshold (float): Minimum similarity threshold
        
    Returns:
        dict: Best matching FAQ or None
    """
    matcher = FAQMatcher(faqs)
    return matcher.get_best_match(user_question, threshold)
