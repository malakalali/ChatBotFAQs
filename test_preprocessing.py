from faqs import faqs
from preprocess import preprocess_text, preprocess_faqs

def test_preprocessing():
    print("Testing text preprocessing functionality...\n")
    
    # Test individual text preprocessing
    test_texts = [
        "How can I reset my password?",
        "What are your business hours?",
        "Do you ship internationally?",
        "Can I get a refund instead of a replacement?"
    ]
    
    print("Original Text -> Preprocessed Text:")
    print("-" * 50)
    for text in test_texts:
        processed = preprocess_text(text)
        print(f"'{text}' -> '{processed}'")
    
    print("\n" + "="*60 + "\n")
    
    # Test FAQ preprocessing
    print("Processing all FAQs...")
    processed_faqs = preprocess_faqs(faqs)
    
    print(f"Total FAQs processed: {len(processed_faqs)}")
    print("\nSample processed FAQs:")
    print("-" * 50)
    
    for i, faq in enumerate(processed_faqs[:5]):
        print(f"FAQ {i+1}:")
        print(f"  Original: {faq['question']}")
        print(f"  Processed: {faq['processed_question']}")
        print()
    
    return processed_faqs

if __name__ == "__main__":
    processed_faqs = test_preprocessing()
