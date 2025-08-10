from faqs import faqs
from preprocess import preprocess_faqs

# Preprocess all FAQs and store them
processed_faqs = preprocess_faqs(faqs)

# Example of how to access preprocessed data
def get_processed_faqs():
    """
    Get the list of FAQs with preprocessed questions.
    
    Returns:
        list: List of FAQ dictionaries with 'processed_question' field
    """
    return processed_faqs

def get_faq_by_index(index):
    """
    Get a specific FAQ by index.
    
    Args:
        index (int): Index of the FAQ
        
    Returns:
        dict: FAQ dictionary with original and processed question
    """
    if 0 <= index < len(processed_faqs):
        return processed_faqs[index]
    return None

# Print summary of processed FAQs
if __name__ == "__main__":
    print(f"Total FAQs processed: {len(processed_faqs)}")
    print("\nSample processed FAQs:")
    print("-" * 50)
    
    for i, faq in enumerate(processed_faqs[:3]):
        print(f"FAQ {i+1}:")
        print(f"  Original: {faq['question']}")
        print(f"  Processed: {faq['processed_question']}")
        print(f"  Answer: {faq['answer'][:100]}...")
        print()
